import os
import subprocess

import toml

# NOTE: Merged with API version to produce the full SDK version string
# https://docs.substrate.run/versioning
SDK_VERSION = "0.0.1"


def ok(message):
    print("\033[32m✓\033[0m", message)


def exec_sync(command):
    subprocess.check_call(command, shell=True)


# Copy files from substratecore
src_dir = "../substrate/sb_models/substratecore"
dest_dir = "substrate/core"
excluded_files = [
    "versions.py",
    "jina_versions.py",
    "mistral_versions.py",
    "stablediffusion_versions.py",
    "deprecated_models.py",
    "__pycache__",
    "*.md",
]
exclude_args = " ".join(f"--exclude='{pattern}'" for pattern in excluded_files)
cmd = f"rsync -av {exclude_args} {src_dir}/ {dest_dir}/"
exec_sync(cmd)
ok(f"Copied files from {src_dir} to {dest_dir}")

# Replace substratecore absolute imports with relative imports
for root, _, files in os.walk(dest_dir):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                content = f.read()
            # Calculate the relative path to handle nested directories
            relative_path = os.path.relpath(dest_dir, root).replace(os.path.sep, ".")
            content = content.replace("sb_models.substratecore.", relative_path)
            with open(file_path, "w") as f:
                f.write(content)
            ok(f"Replaced imports in {file_path}")

# Copy codegen files
src_dir = "../substrate/codegen/python/src"
dest_dir = "substrate"
cmd = f"rsync -av {src_dir}/ {dest_dir}/"
exec_sync(cmd)
os.rename(os.path.join(dest_dir, "init.py"), os.path.join(dest_dir, "__init__.py"))

# Update version
version_path = os.path.join(src_dir, "GEN_VERSION")
with open(version_path, "r") as f:
    content = f.read()
    datestr = content.split(".")[0]

# Split the SDK_VERSION and insert the datestring
major_version, *rest = SDK_VERSION.split(".")
new_version = f"{major_version}{datestr}.{'.'.join(rest)}"
toml_content = None
toml_path = "pyproject.toml"
with open(toml_path, "r") as f:
    toml_content = toml.load(f)
    toml_content["tool"]["poetry"]["version"] = new_version
    with open(toml_path, "w") as f:
        toml.dump(toml_content, f)
    ok(f"Updated version to {new_version} in {toml_path}")
