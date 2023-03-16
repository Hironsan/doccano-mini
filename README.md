# doccano-mini

doccano-mini is a few-shot annotation tool to assist the development of applications with Large language models (LLMs). Once you annotate a few text, you can test your task (e.g. text classification) with LLMs, then download the [LangChain](https://github.com/hwchase17/langchain)'s config.

Note: This is an experimental project.

## Installation

```bash
pip install doccano-mini
```

## Usage

For this example, we will be using OpenAI’s APIs, so we need to set the environment variable in the terminal.

```bash
export OPENAI_API_KEY="..."
```

Then, we can run the server.

```bash
doccano-mini
```

Now, we can open the browser and go to `http://localhost:8501/` to see the interface.

### Step1: Annotate a few text

In this step, we will annotate a few text. We can add a new text by clicking the `+` button. Try it out by double-clicking on any cell. You'll notice you can edit all cell values.

![Step1](./docs/images/annotation.gif)

### Step2: Test your task

In this step, we will test your task. We can enter a new test to the text box and click the `Predict` button. Then, we can see the result of the test.

![Step2](./docs/images/test_new_example.jpg)

### Step3: Download the config

In this step, we will download the [LangChain](https://github.com/hwchase17/langchain)'s config. We can click the `Download` button to download it.

![Step3](./docs/images/download_config.jpg)

## Development

```bash
poetry install
streamlit run doccano_mini/app.py
```
