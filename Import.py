from datasets import load_dataset
data = load_dataset(
    "meta-llama/Meta-Llama-3.1-8B-evals",
    name="Meta-Llama-3.1-8B-evals__agieval_english__details",
    split="latest"
    )