import os
import sys
import json

from util import jq_list, aggregate, current_dir, sample_question

from substrate import Box, Substrate, ComputeText, sb

substrate = Substrate(api_key=os.environ.get("SUBSTRATE_API_KEY"))
models = [
    "Mistral7BInstruct",
    "Mixtral8x7BInstruct",
    "Llama3Instruct8B",
    "Llama3Instruct70B",
]
decider = "Llama3Instruct70B"

max_tokens = 800
opts = {"cache_age": 60 * 60 * 24 * 7}
num_layers = 3
question = sys.argv[1] if len(sys.argv) > 1 else sample_question


def get_mixture(q, prev=None):
    prompt = sb.concat(aggregate, "\n\nquestion: ", q, "\n\nprevious:\n\n", prev) if prev else q
    return Box(value=[ComputeText(prompt=prompt, model=m, max_tokens=max_tokens, **opts).future.text for m in models])


def main():
    layers = [get_mixture(question)]

    def last_layer():
        return sb.jq(layers[-1].future.value, jq_list)

    for _ in range(num_layers - 1):
        layers.append(get_mixture(question, last_layer()))

    final = ComputeText(prompt=sb.concat(aggregate, "\n\n", last_layer()), model=decider, max_tokens=max_tokens, **opts)

    box = Box(value={"layers": [l.future.value for l in layers], "final": final.future.text})
    res = substrate.run(box)
    json_out = res.get(box).value

    with open(os.path.join(current_dir, "index.html"), "r") as f:
        html_template = f.read()

    html = (
        html_template.replace('"{{ individual }}"', json.dumps(json_out["layers"], indent=2))
        .replace('"{{ question }}"', json.dumps(question))
        .replace('"{{ summaries }}"', f'[{json.dumps(json_out["final"])}]')
    )

    with open("moa.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
    print("꩜ Done. View by running `open moa.html`")
