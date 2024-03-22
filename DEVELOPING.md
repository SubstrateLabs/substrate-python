## Development

```
# install deps
make develop

# install lint pre-commit hook
poetry run pre-commit install

# sync codegen
make sync

# create a `.pypirc` in your home dir to publish (see `.pypirc.example`)
make publish
```
