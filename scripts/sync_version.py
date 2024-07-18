"""
Syncs SDK version (here) with API version and updates the pyproject.toml version
https://docs.substrate.run/versioning
"""

import toml


def ok(message):
    print("\033[32m✓\033[0m", message)


SDK_VERSION = "2.1.3"

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

# Write the API Version (as a formatted date) to the following. This is used by the
# SDK client to select which API version to use and should be in sync with the types
# used in the SDK.
version_file = "substrate/_version.py"
with open(version_file, "w") as f:
    version_file_content = f'__version__ = "{new_version}"'
    f.write(version_file_content)
    ok(f"Updated {version_file} content to {version_file_content}")
