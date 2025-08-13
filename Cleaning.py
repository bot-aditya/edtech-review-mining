import pandas as pd

# Load combined CSV
df = pd.read_csv("Reviews.csv")

# Quick look at the first rows
print(df.head())

# Check data info
print(df.info())

# Check for missing values
print(df.isnull().sum())

import re

# Drop rows with missing content
df.dropna(subset=['content'], inplace=True)

# Drop duplicates based on review text
df.drop_duplicates(subset='content', inplace=True)

# Remove very short reviews
df = df[df['content'].str.len() >= 10]

# Convert to lowercase & remove non-alphabetic characters
df['clean_review'] = df['content'].apply(
    lambda x: re.sub('[^a-zA-Z ]', '', x.lower())
)

# Save cleaned data
df.to_csv("cleaned_reviews.csv", index=False)
print(f"Cleaned dataset saved. Remaining rows: {len(df)}")
