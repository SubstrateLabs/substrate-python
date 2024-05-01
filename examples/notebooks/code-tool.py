import marimo

__generated_with = "0.3.12"
app = marimo.App(width="medium")


@app.cell
def __():
    import os
    import json
    import base64
    import marimo as mo
    from substrate import Substrate, GenerateJSON, RunCode, sb

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    api_key = api_key or "YOUR_API_KEY"
    mo.md(f"`{api_key}`")
    return (
        GenerateJSON,
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
def __(GenerateJSON, RunCode, question, sb):
    prompt = f"""
    {question.value}

    Think step by step and run Python code to check your work or solve problems before returning an answer. Print the output. The Python runtime does not have network or filesystem access, but does include the entire standard library. Read input from stdin and write output to stdout. Remember to print the output.
    """
    print(prompt)
    json_schema = {
        "type": "object",
        "properties": {
            "answer": {
                "type": "string",
                "description": "The answer to the question.",
            },
            "python_code": {
                "type": "string",
                "description": "Python code to check your work or solve the problem.",
            },
            "should_run_code": {
                "type": "boolean",
                "description": "Set to true if you need to run `python_code` before giving your final answer.",
            },
        },
        "required": ["answer", "python_code", "should_run_code"],
    }
    gj = GenerateJSON(
        {
            "prompt": prompt,
            "json_schema": json_schema,
            "node": "Mixtral8x7BInstruct",
            # "node": "Mistral7BInstruct",
        }
    )
    code = RunCode(
        {
            "code": sb.jq(gj.future.json_object, ".python_code"),
        }
    )
    return code, gj, json_schema, prompt


@app.cell
def __(code, gj, substrate):
    res = substrate.run(gj, code)
    return res,


@app.cell
def __(code, gj, json, res):
    print(json.dumps(res.json, indent=2))
    gj_out = res.get(gj)
    code_out = res.get(code)
    return code_out, gj_out


@app.cell
def __(gj_out, json):
    json.dumps(gj_out.json_object, indent=2)
    return


@app.cell
def __(code_out, json):
    json.dumps(code_out.dict(), indent=2)
    return


if __name__ == "__main__":
    app.run()
