# EdTech App Review Analysis (Play Store + App Store)

## 📌 Project Overview
This project analyzes **user reviews** of popular Indian EdTech apps  
(**Unacademy, Vedantu, PhysicsWallah**) from both the **Play Store and App Store**  
to extract **product insights and pain points**.

**Key Goals:**
- Collect ~1,000 reviews per app from Play Store & App Store
- Clean and preprocess user reviews for NLP
- Perform **sentiment analysis** using VADER
- Identify **common pain points** and visualize insights
- Suggest potential **product improvements**

---

## 🗂 Dataset
- **Play Store Reviews**: Scraped with `google-play-scraper` (Python)
- **App Store Reviews**: Scraped with `app-store-scraper` (Node.js)
- Combined into `Reviews.csv` with columns:


---

## ⚙️ Tech Stack
- **Python**: `pandas`, `nltk`, `scikit-learn`, `wordcloud`, `matplotlib`
- **Node.js**: `app-store-scraper`, `csv-writer`
- **Jupyter Notebook** for analysis pipeline

---

## 📊 Analysis Pipeline
1. **Scraping Reviews**
 - Play Store → Python (`google-play-scraper`)
 - App Store → Node.js (`app-store-scraper`)
2. **Cleaning Data**
 - Remove duplicates, very short reviews, special characters
3. **Sentiment Analysis**
 - VADER (Positive / Neutral / Negative)
4. **Pain Point Extraction**
 - Word clouds of negative reviews
 - Top frequent complaint terms
 - Clustering to identify 5 key product issues

---

## 📈 Key Insights
- **PhysicsWallah**: Users frequently mention "video buffering" & "ads"
- **Vedantu**: Complaints about "app crashes" and "login issues"
- **Unacademy**: Pricing and subscription confusion dominate negative reviews

*(See visuals in the `visuals/` folder)*

---

## 🚀 How to Run

### 1️⃣ Setup Python Environment
```bash
pip install -r requirements.txt

