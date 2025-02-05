# 4 - Machine Learning and AI with Streamlit

## ML workflow

I can train the model inside Streamlit (for small models) or train it outside/externally (scripts/notebooks/Spark) and use the pretained model

For the modeling (predicting penguin species), see:

* `penguins_ml.py`
* `penguins_ml.ipynb`

## Utilizing a pre-trained ML model

`penguins_streamlit.py`

## Training models inside Streamlit apps

It's the same thing but inside the Streamlit app...

## Integrating external ML libraries – a Hugging Face example

The `requirements.txt` includes:

```none
# Hugging Face's Transformers + Pytorch
transformers[torch]<5.0.0
```

When you run `pip install -r requirements.txt`, it will install the transformers library along with the required PyTorch version **for CPU support**. This ensures that you have everything needed to use the Hugging Face Transformers library with PyTorch.

<https://huggingface.co/docs/transformers/installation>

## Integrating external AI libraries – an OpenAI example
