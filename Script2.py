from app_store_scraper import AppStore

# Function to fetch App Store reviews
def fetch_appstore_reviews(app_name, app_id, country="in", count=1000):
    app = AppStore(country=country, app_name=app_name, app_id=app_id)
    app.review(how_many=count)
    df = pd.DataFrame(app.reviews)
    df = df[['review', 'rating', 'date']]  # Rename to match Play Store schema
    df.rename(columns={'review': 'content', 'rating': 'score', 'date': 'at'}, inplace=True)
    df['source'] = 'AppStore'
    df['app'] = app_name
    return df

# App IDs from App Store URLs
apps_appstore = {
    "Unacademy": 1342565069,
    "Vedantu": 1481959104,
    "PhysicsWallah": 1641443555
}

# Fetch and combine all App Store reviews
dfs_app = []
for app_name, app_id in apps_appstore.items():
    print(f"Fetching App Store reviews for {app_name}...")
    df = fetch_appstore_reviews(app_name, app_id)
    dfs_app.append(df)

appstore_df = pd.concat(dfs_app, ignore_index=True)
appstore_df.to_csv("appstore_reviews.csv", index=False)
print("App Store reviews saved to appstore_reviews.csv")
