"""
API DATA FETCHER
Author: Harsha
Date: November 26, 2025
Purpose: Fetch real data from internet API - Day 10
"""

import requests
import pandas as pd

print("="*60)
print("API DATA FETCHER - Real Internet Data!")
print("="*60)

# API URL - Free public API (no key needed!)
API_URL = "https://jsonplaceholder.typicode.com/users"

# STEP 1: FETCH data from API
print("\n📡 Fetching data from API...")
print(f"API: {API_URL}")

try:
    response = requests.get(API_URL)
    
    # Check if request was successful
    if response.status_code == 200:
        print("✅ Data fetched successfully!")
        
        # Convert JSON to Python data
        users_data = response.json()
        print(f"   Retrieved {len(users_data)} users")
    else:
        print(f"❌ Error: Status code {response.status_code}")
        exit()
        
except Exception as e:
    print(f"❌ Error fetching data: {e}")
    exit()

# STEP 2: TRANSFORM - Convert to DataFrame
print("\n🔄 Converting to DataFrame...")
df = pd.DataFrame(users_data)
print("✅ Conversion complete!")

print("\n📊 Data Preview:")
print(df[['id', 'name', 'email', 'phone']].head())

# STEP 3: ANALYZE - Extract insights
print("\n📈 ANALYZING DATA...")

# Analysis 1: Total users
print(f"\n👥 Total Users: {len(df)}")

# Analysis 2: Email domains
print("\n📧 EMAIL DOMAINS:")
df['domain'] = df['email'].str.split('@').str[1]
domain_counts = df['domain'].value_counts()
for domain, count in domain_counts.items():
    print(f"   {domain}: {count} users")

# Analysis 3: Companies
print("\n🏢 COMPANIES:")
companies = df['company'].apply(lambda x: x['name'] if isinstance(x, dict) else x)
print(f"   {len(companies.unique())} unique companies")

# STEP 4: LOAD - Save to CSV
print("\n💾 Saving data...")

# Save main data
df[['id', 'name', 'username', 'email', 'phone']].to_csv('users_data.csv', index=False)
print("✅ Saved: users_data.csv")

# Save summary
summary = pd.DataFrame({
    'Metric': ['Total Users', 'Unique Domains', 'Unique Companies'],
    'Value': [len(df), df['domain'].nunique(), companies.nunique()]
})
summary.to_csv('api_summary.csv', index=False)
print("✅ Saved: api_summary.csv")

print("\n" + "="*60)
print("✅ API DATA FETCH COMPLETE!")
print("="*60)
print("\n💡 You just fetched REAL data from the internet!")