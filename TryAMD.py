from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = 'hermes'
model_path = ''
model_type = ''

if model_name == 'mistral':
    model_path = r'C:\PythonParaphanalia\Models\mistral-7b-instruct-v0.2.Q4_K_M.gguf'
    model_type = 'mistral'
elif model_name == 'mistral-instruct':
    model_path = r'C:\PythonParaphanalia\Models\mistral-7b-v0.1.Q4_K_M.gguf'
    model_type = 'mistral'
elif model_name == 'vicuna':
    model_path = r'C:\PythonParaphanalia\Models\Wizard-Vicuna-13B-Uncensored.Q4_K_M.gguf'
    model_type = 'vicuna'
elif model_name == 'hermes':
    model_path = r'C:\PythonParaphanalia\Models\CapybaraHermes-2.5-Mistral-7B-GPTQ'
    model_type = model_name

a = 1

tokenizer = AutoTokenizer.from_pretrained(model_path)
with torch.device("cuda"):
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16)

inp = tokenizer(["Today I am in Paris and"], padding=True, return_tensors="pt").to("cuda")
res = model.generate(**inp, max_new_tokens=30)

print(tokenizer.batch_decode(res))