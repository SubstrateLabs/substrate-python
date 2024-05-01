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
def __(GenerateText, RunCode, question):
    prompt = f"""
    {question.value}

    Think step by step and run Python code to check your work or solve problems before returning an answer. Print the output. The Python runtime does not have network or filesystem access, but does include the entire standard library. Read input from stdin and write output to stdout. Remember to print the output in your code. Wrap the code in your response inside a <code></code> tag.
    """
    text = GenerateText(
        {
            "prompt": prompt,
            "node": "Llama3Instruct70B",
            # "node": "Mistral7BInstruct",
        }
    )
    get_code = RunCode(
        {
            "code": """import re
    import sys

    s = sys.argv[1]
    match = re.search(r'<code>(.*?)</code>', s, re.DOTALL)
    print(match.group(1) if match else "")
    """,
            "args": [text.future.text],
        }
    )
    run_code = RunCode({"code": get_code.future.output})
    return get_code, prompt, run_code, text


@app.cell
def __(get_code, mo, run_code, substrate, text):
    res = substrate.run(text, get_code, run_code)
    viz = substrate.visualize(text, get_code, run_code)
    mo.md(f"[visualize]({viz})")
    return res, viz


@app.cell
def __(json, mo, res, run_code):
    print(json.dumps(res.json, indent=2))
    mo.md(res.get(run_code).output)
    return


if __name__ == "__main__":
    app.run()
