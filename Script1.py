from google_play_scraper import reviews, Sort
import pandas as pd

def fetch_playstore_reviews(app_id, app_name, count=1000):
    result, _ = reviews(
        app_id,
        lang='en',
        country='in',
        count=count,
        sort=Sort.NEWEST  # ✅ Use the Enum, not a string
    )
    df = pd.DataFrame(result)
    df = df[['content', 'score', 'at']]  # keep only useful columns
    df['source'] = 'PlayStore'
    df['app'] = app_name
    return df

# App IDs from Play Store URLs
apps_playstore = {
    "Unacademy": "com.unacademyapp",
    "Vedantu": "com.vedantu.app",
    "PhysicsWallah": "xyz.penpencil.physicswala"
}

dfs_play = []
for app_name, app_id in apps_playstore.items():
    print(f"Fetching Play Store reviews for {app_name}...")
    df = fetch_playstore_reviews(app_id, app_name)
    dfs_play.append(df)

playstore_df = pd.concat(dfs_play, ignore_index=True)
playstore_df.to_csv("playstore_reviews.csv", index=False)
print("Play Store reviews saved to playstore_reviews.csv")
