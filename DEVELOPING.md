# Development

## Releasing the SDK

(in the context of a new PR for this version)

```sh
make sync           # sync codegen
# Bump the version in scripts/sync_version.
# Use a minor version bump unless there are breaking SDK changes.
make sync-version
poetry run python examples/basic.py # use the local package in this script
```

(make sure CI passes, do some spot checking e.g. in examples/basic.py)

```sh
make clean          # clean
make dist           # build
make publish        # publish
```

(validate this version)

```sh
cd examples/notebooks
make ensure     # if you're here for the first time
make update     # upgrade to the latest substrate version
# You should see:
# Updating substrate (120240502.0.3 -> 220240509.0.0)
poetry run marimo edit basic.py      # run the basic notebook
```

## Setting up local development

```sh
# install deps
make develop

# install lint pre-commit hook
poetry run pre-commit install
```

- create a `.pypirc` in your home dir to publish (see `.pypirc.example`)
