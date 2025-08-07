import random
from textblob import TextBlob
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_reviews(reviews):
    if not reviews:
        return "Neutral"
    blob = TextBlob(reviews)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    return "Neutral"

def calculate_eco_score(text):
    keywords = ["eco", "biodegradable", "sustainable", "organic", "recyclable", "plant-based", "compostable"]
    count = sum(1 for k in keywords if k in text.lower())
    base_score = 50 + count * 10
    return min(100, base_score)


