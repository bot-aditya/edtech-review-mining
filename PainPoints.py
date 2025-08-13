import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# -------------------------
# STEP 0: Load Sentiment Data
# -------------------------
df = pd.read_csv("reviews_with_sentiment.csv")  # already has sentiment_label

# Filter only negative reviews (pain points)
negative_reviews = df[df['sentiment_label'] == 'Negative']
print("Total negative reviews:", len(negative_reviews))

# -------------------------
# STEP 1: Word Cloud of Negative Reviews
# -------------------------
all_negative_text = ' '.join(negative_reviews['clean_review'])

wc = WordCloud(width=1000, height=500, background_color='white').generate(all_negative_text)

plt.figure(figsize=(15, 7))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("Most Common Words in Negative Reviews", fontsize=16)
plt.show()

# -------------------------
# STEP 2: Top Complaint Words per App
# -------------------------
from collections import Counter

def top_words(text_series, n=10):
    words = ' '.join(text_series).split()
    common = Counter(words).most_common(n)
    return common

for app_name in df['app'].unique():
    app_neg = negative_reviews[negative_reviews['app'] == app_name]['clean_review']
    print(f"\nTop complaint words for {app_name}:")
    print(top_words(app_neg, 10))

# -------------------------
# STEP 3: Optional - Cluster Negative Reviews into Themes
# -------------------------
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(negative_reviews['clean_review'])

# Choose 5 clusters for themes
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X)

negative_reviews['cluster'] = clusters

# Show top terms per cluster
terms = vectorizer.get_feature_names_out()
print("\nTop terms per cluster (potential pain point themes):")
for i in range(5):
    cluster_indices = (clusters == i)
    cluster_words = X[cluster_indices].sum(axis=0)
    top_indices = cluster_words.A[0].argsort()[-10:]
    top_terms = [terms[j] for j in top_indices]
    print(f"Cluster {i}: {top_terms}")

# -------------------------
# STEP 4: Save Clustered Negative Reviews
# -------------------------
negative_reviews.to_csv("negative_reviews_with_clusters.csv", index=False)
print("\n✅ Pain point extraction complete. Saved to negative_reviews_with_clusters.csv")
