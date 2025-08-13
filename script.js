const store = require('app-store-scraper');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

// Define the apps and their IDs (from your links)
const apps = [
  { name: "Unacademy", id: 1342565069 },
  { name: "Vedantu", id: 1481959104 },
  { name: "PhysicsWallah", id: 1641443555 }
];

// CSV writer setup
const csvWriter = createCsvWriter({
  path: 'appstore_reviews.csv',
  header: [
    { id: 'app', title: 'app' },
    { id: 'userName', title: 'userName' },
    { id: 'date', title: 'at' },
    { id: 'score', title: 'score' },
    { id: 'title', title: 'title' },
    { id: 'content', title: 'content' }
  ],
  append: false
});

// Function to fetch reviews
async function fetchReviews(app) {
  console.log(`Fetching reviews for ${app.name}...`);

  let allReviews = [];
  let page = 1;
  
  while (allReviews.length < 1000) { // fetch ~1000 reviews
    try {
      const reviews = await store.reviews({
        id: app.id,
        country: 'in', // Indian App Store
        page: page,
        sort: store.sort.RECENT
      });

      if (reviews.length === 0) break; // stop if no more reviews

      // Map to clean structure
      const formatted = reviews.map(r => ({
        app: app.name,
        userName: r.userName || '',
        date: r.date || '',
        score: r.score || '',
        title: r.title || '',
        content: r.text || ''
      }));

      allReviews = allReviews.concat(formatted);
      console.log(`Page ${page} fetched: Total so far ${allReviews.length}`);
      page++;

    } catch (err) {
      console.error(`Error fetching ${app.name} page ${page}:`, err.message);
      break;
    }
  }

  return allReviews.slice(0, 1000); // limit to 1000
}

// Main async function
async function main() {
  let totalReviews = [];
  for (let app of apps) {
    const reviews = await fetchReviews(app);
    totalReviews = totalReviews.concat(reviews);
  }

  // Write all reviews to CSV
  await csvWriter.writeRecords(totalReviews);
  console.log('✅ All reviews saved to appstore_reviews.csv');
}

main();
