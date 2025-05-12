# %pip install --upgrade --quiet huggingface_hub
# %pip install --upgrade langchain

from transformers import pipeline
sentiment_analyzer = pipeline("sentiment-analysis")
sentences = [
"The product quality is amazing! I'm very satisfied.",
"I had a terrible experience with customer service.",
"The delivery was quick, but the packaging was damaged.",
"Absolutely love this! Best purchase I've made.",
"Not worth the money, very disappointed."
]
results = sentiment_analyzer(sentences)
for sentence, result in zip(sentences, results):
  print(f"Sentence: {sentence}\nSentiment: {result['label']}, Confidence: {result['score']:.2f}\n")
