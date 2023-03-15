from typing import List

from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

from .tasks import TaskType


def make_classification_prompt(examples: List[dict]) -> FewShotPromptTemplate:
    unique_labels = set([example["label"] for example in examples])

    task_instruction = "Classify the text into one of the following labels:\n"
    for label in unique_labels:
        task_instruction += f"- {label}\n"

    example_prompt = PromptTemplate(input_variables=["text", "label"], template="text: {text}\nlabel: {label}")
    prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix=task_instruction,
        suffix="text: {input}",
        input_variables=["input"],
    )
    return prompt


def select_prompt_maker(task: TaskType):
    if task == TaskType.TEXT_CLASSIFICATION.value:
        return make_classification_prompt
    raise ValueError(f"Task {task} is not supported.")
