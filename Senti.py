import pandas as pd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# -------------------------
# STEP 0: Setup
# -------------------------

# Download VADER lexicon (first time only)
nltk.download('vader_lexicon')

# Load your combined reviews CSV
df = pd.read_csv("Reviews.csv")  # Columns: content, score, source, app
print("Original dataset size:", len(df))

# -------------------------
# STEP 1: Clean & Prepare Data
# -------------------------

# Drop rows with missing content
df.dropna(subset=['content'], inplace=True)

# Drop duplicate reviews
df.drop_duplicates(subset='content', inplace=True)

# Remove very short reviews (less than 10 chars)
df = df[df['content'].str.len() >= 10]

# Clean text: lowercase + remove non-alphabetic characters
df['clean_review'] = df['content'].apply(lambda x: re.sub('[^a-zA-Z ]', '', x.lower()))

print("After cleaning, dataset size:", len(df))

# -------------------------
# STEP 2: Sentiment Analysis
# -------------------------

# Initialize VADER
sia = SentimentIntensityAnalyzer()

# Compute sentiment score (compound value from -1 to 1)
df['sentiment_score'] = df['clean_review'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Label the sentiment based on compound score
def label_sentiment(score):
    if score > 0.05:
        return 'Positive'
    elif score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment_label'] = df['sentiment_score'].apply(label_sentiment)

# -------------------------
# STEP 3: Quick Insights
# -------------------------

# Count sentiment distribution
print("\nSentiment distribution:")
print(df['sentiment_label'].value_counts())

# Count sentiment per app
print("\nSentiment distribution per app:")
print(df.groupby('app')['sentiment_label'].value_counts())

# -------------------------
# STEP 4: Save Final Dataset
# -------------------------

df.to_csv("reviews_with_sentiment.csv", index=False)
print("\n✅ Sentiment analysis complete. Saved to reviews_with_sentiment.csv")

# Final columns:
# content, score, source, app, clean_review, sentiment_score, sentiment_label
