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
