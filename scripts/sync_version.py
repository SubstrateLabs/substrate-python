"""
Syncs SDK version (here) with API version and updates the pyproject.toml version
https://docs.substrate.run/versioning
"""

import toml


def ok(message):
    print("\033[32m✓\033[0m", message)


SDK_VERSION = "1.0.5"

# Update version
version_path = "substrate/GEN_VERSION"
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
