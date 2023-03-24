import streamlit as st
from langchain.chains import LLMChain

from doccano_mini.components import (
    display_download_button,
    display_usage,
    openai_model_form,
    task_instruction_editor,
)
from doccano_mini.examples import make_classification_example
from doccano_mini.prompts import make_classification_prompt

st.title("Text Classification")
st.header("Annotate your data")
df = make_classification_example()
edited_df = st.experimental_data_editor(df, num_rows="dynamic", width=1000)
examples = edited_df.to_dict(orient="records")

prompt = make_classification_prompt(examples)
prompt = task_instruction_editor(prompt)

st.header("Test")
col1, col2 = st.columns([3, 1])
inputs = {"input": col1.text_area(label="Please enter your text.", value="", height=300)}

with col2:
    llm = openai_model_form()

with st.expander("See your prompt"):
    st.markdown(f"```\n{prompt.format(**inputs)}\n```")

if st.button("Predict"):
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(**inputs)
    st.text(response)

    chain.save("config.yaml")
    display_download_button()
display_usage()
