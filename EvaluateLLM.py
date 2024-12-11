from evaluate import evaluator
from datasets import load_dataset
from ctransformers import AutoModelForCausalLM

# Evaluation Stuff
task_evaluator = evaluator("text-classification")
data = load_dataset("imdb", split="test[:2]")

# Model Stuff
model_path = r'C:\PythonParaphanalia\Models\mistral-7b-instruct-v0.2.Q4_K_M.gguf'
llm = AutoModelForCausalLM.from_pretrained(model_path, model_type='mistral')

# Evaluate!
results = task_evaluator.compute(
    model_or_pipeline=llm,
    data=data,
    metric="accuracy",
    label_mapping={"LABEL_0": 0.0, "LABEL_1": 1.0},
    strategy="bootstrap",
    n_resamples=10,
    random_state=0
)