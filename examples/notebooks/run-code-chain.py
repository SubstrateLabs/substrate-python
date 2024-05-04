import marimo

__generated_with = "0.3.12"
app = marimo.App(width="medium")


@app.cell
def __():
    import os
    import json
    import base64
    import marimo as mo
    from substrate import Substrate, GenerateJSON, GenerateText, RunCode, sb

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    api_key = api_key or "YOUR_API_KEY"
    mo.md(f"`{api_key}`")
    return (
        GenerateJSON,
        GenerateText,
        RunCode,
        Substrate,
        api_key,
        base64,
        json,
        mo,
        os,
        sb,
    )


@app.cell
def __(Substrate, api_key):
    substrate = Substrate(
        api_key=api_key,
        backend="v1",
    )
    return substrate,


@app.cell
def __(mo):
    question = mo.ui.text(
        placeholder="Question",
        value="What is the 88th fibonacci number?",
        full_width=True,
    ).form()
    question
    return question,


@app.cell
def __(GenerateText, RunCode, question, sb):
    prompt = f"""
    {question.value or 'What is the 88th fibonacci number?'}

    Think step by step and run Python code to check your work or solve problems before returning an answer. Print the output inside json in a "result" key with json.dumps. The Python runtime does not have network or filesystem access, but does include the entire standard library. Read input from stdin and write output to stdout. Remember to print the output in your code inside json with json.dumps. Wrap the code in your response inside a <code></code> tag.
    """
    text = GenerateText(
        {
            "prompt": prompt,
            "node": "Llama3Instruct70B",
        }
    )
    run_code = RunCode(
        {
            "code": sb.jq(
                text.future.text,
                'split("<code>") | .[1] | split("</code>") | .[0]',
            )
        }
    )
    return prompt, run_code, text


@app.cell
def __(Substrate, mo, run_code, substrate, text):
    res = substrate.run(text, run_code)
    d = Substrate.serialize(text, run_code)
    viz = substrate.visualize(text, run_code)
    mo.md(f"[visualize]({viz})")
    return d, res, viz


@app.cell
def __(json, res):
    print(json.dumps(res.json, indent=2))
    # mo.md(res.get(run_code).output)
    return


if __name__ == "__main__":
    app.run()
