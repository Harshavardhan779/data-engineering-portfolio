# API Data Fetcher

Fetches real user data from a public API and analyzes it.

## What It Does
- Fetches data from JSONPlaceholder API (test API)
- Converts JSON response to pandas DataFrame
- Analyzes email domains and companies
- Saves data to CSV files

## Key Concepts
- **API calls**: Making HTTP requests
- **JSON parsing**: Converting API response to usable data
- **Error handling**: Checking if request succeeded
- **Data transformation**: JSON → DataFrame → CSV

## Technologies
- Python
- requests library (HTTP calls)
- pandas (data processing)
- JSONPlaceholder API (free test API)

## Files
- `fetch_users.py` - Main script
- `users_data.csv` - Fetched user data
- `api_summary.csv` - Analysis summary

## What I Learned
- How APIs work (requesting data over internet)
- HTTP status codes (200 = success)
- JSON data format
- requests library usage
- Real-world data fetching

## Author
Harsha - November 27, 2025  
Day 10 of Data Engineering Journey

---

*First time fetching real data from internet! 🌐*