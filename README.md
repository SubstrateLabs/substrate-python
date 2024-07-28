# Substrate Python SDK

[![PyPI version](https://img.shields.io/pypi/v/substrate.svg)](https://pypi.org/project/substrate/)

Substrate is a **powerful SDK** for building with AI, with [batteries included](https://substrate.run/nodes): language models, image generation, built-in vector storage, sandboxed code execution, and more. To use Substrate, you simply connect tasks, and then run the workflow. With this simple approach, we can create AI systems (from RAG, to agents, to multi-modal generative experiences) by simply describing the computation, with **zero additional abstractions**.

Substrate is also a **workflow execution** and **inference** engine, optimized for running compound AI workloads. Wiring together multiple inference APIs is inherently slow – whether you do it yourself, or use a framework like LangChain. Substrate lets you ditch the framework, write less code, and run compound AI fast. 

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
