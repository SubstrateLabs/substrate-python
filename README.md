# Substrate Python SDK

[![PyPI version](https://img.shields.io/pypi/v/substrate.svg)](https://pypi.org/project/substrate/)

The Substrate Python SDK is the recommended way to interact with the Substrate API from any Python application.

## Documentation

If you're just getting started, head to [docs.substrate.run](https://docs.substrate.run/).

For a detailed API reference covering the nodes available on Substrate, see [substrate.run/nodes](https://www.substrate.run/nodes).

## Installation

```sh
# install from PyPI
pip install substrate
```

## Usage

```python
from substrate import Substrate, ComputeText, sb
```

Initialize the Substrate client.

```python
substrate = Substrate(api_key=SUBSTRATE_API_KEY)
```

Generate a story using the [`ComputeText`](https://www.substrate.run/nodes#ComputeText) node.

```python
story = ComputeText(prompt="tell me a story")
```

Summarize the output of the `story` node using another `ComputeText` node. Because `story` has not yet been run, we use `sb.concat` to work with its future output.

```python
summary = ComputeText(prompt=sb.concat("summarize this story in one sentence: ", story.future.text))
```

Run the graph chaining `story` → `summary` by passing the terminal node to `substrate.run`.

```python
response = substrate.run(story, summary)
```

(To run the graph asynchronously, simply use `async_run` and `await`.)

```python
response = await substrate.async_run(story, summary)
```

Get the output of the summary node by passing it to `response.get`.

```python
summary_out = response.get(summary)
print(summary_out.text)
# Princess Lily, a kind-hearted young princess, discovers a book of spells and uses it to grant her family and kingdom happiness.
```

## Examples

To run the above example as a notebook, navigate to the `examples/notebooks` directory and run:

```sh
make ensure                         # install dependencies
poetry run marimo edit basic.py     # run the notebook
```

Many more examples are included in the `/examples` directory.
