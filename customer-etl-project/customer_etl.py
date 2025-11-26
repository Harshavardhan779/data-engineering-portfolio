"""
CUSTOMER DATA ETL PIPELINE
Author: Harsha
Date: November 25, 2025
Purpose: Clean and process messy customer data
"""

import pandas as pd
import numpy as np

print("="*60)
print("CUSTOMER DATA ETL PIPELINE")
print("="*60)

# ============================================
# STEP 1: EXTRACT - Load Raw Data
# ============================================
print("\n📥 EXTRACTING customer data...")
df = pd.read_csv('customer_data.csv')
print(f"✅ Loaded {len(df)} customer records")

print("\n📊 Raw Data Sample:")
print(df.head(3))

print("\n⚠️ Data Quality Issues:")
print(f"   Missing values per column:")
print(df.isnull().sum())

# ============================================
# STEP 2: TRANSFORM - Clean Data
# ============================================
print("\n🔄 CLEANING DATA...")

# Clean 1: Fill missing ages with average age
avg_age = df['age'].mean()
df['age'].fillna(avg_age, inplace=True)
print(f"✅ Filled missing ages with average: {avg_age:.0f}")

# Clean 2: Fill missing cities with "Unknown"
df['city'].fillna('Unknown', inplace=True)
print("✅ Filled missing cities with 'Unknown'")

# Clean 3: Fill missing purchase amounts with 0
df['purchase_amount'].fillna(0, inplace=True)
print("✅ Filled missing purchase amounts with 0")

# Clean 4: Fill missing names with "Anonymous"
df['name'].fillna('Anonymous', inplace=True)
print("✅ Filled missing names with 'Anonymous'")

# Clean 5: Fill missing emails with "no-email@example.com"
df['email'].fillna('no-email@example.com', inplace=True)
print("✅ Filled missing emails")

# Clean 6: Drop rows with missing registration_date (critical field)
df.dropna(subset=['registration_date'], inplace=True)
print(f"✅ Removed rows with missing registration dates")
print(f"   Remaining records: {len(df)}")

# ============================================
# STEP 3: ANALYZE - Generate Insights
# ============================================
print("\n📈 ANALYZING CLEANED DATA...")

# Analysis 1: Customer statistics by status
print("\n👥 CUSTOMERS BY STATUS:")
status_counts = df['status'].value_counts()
for status, count in status_counts.items():
    print(f"   {status}: {count} customers")

# Analysis 2: Average purchase by city
print("\n💰 AVERAGE PURCHASE BY CITY:")
city_avg = df.groupby('city')['purchase_amount'].mean().round(2)
for city, avg in city_avg.items():
    print(f"   {city}: ₹{avg:,.2f}")

# Analysis 3: Age distribution
print("\n📊 AGE STATISTICS:")
print(f"   Average age: {df['age'].mean():.1f} years")
print(f"   Youngest: {df['age'].min():.0f} years")
print(f"   Oldest: {df['age'].max():.0f} years")

# Analysis 4: Top spenders
print("\n🏆 TOP 3 SPENDERS:")
top_spenders = df.nlargest(3, 'purchase_amount')[['name', 'city', 'purchase_amount']]
for idx, row in top_spenders.iterrows():
    print(f"   {row['name']} ({row['city']}): ₹{row['purchase_amount']:,.0f}")

# ============================================
# STEP 4: LOAD - Save Clean Data
# ============================================
print("\n💾 SAVING CLEANED DATA...")

# Save cleaned data
df.to_csv('customer_data_clean.csv', index=False)
print("✅ Saved: customer_data_clean.csv")

# Save summary report
summary = pd.DataFrame({
    'Metric': [
        'Total Customers (After Cleaning)',
        'Active Customers',
        'Inactive Customers',
        'Total Purchase Value',
        'Average Purchase',
        'Average Age'
    ],
    'Value': [
        len(df),
        len(df[df['status'] == 'active']),
        len(df[df['status'] == 'inactive']),
        f"₹{df['purchase_amount'].sum():,.0f}",
        f"₹{df['purchase_amount'].mean():,.2f}",
        f"{df['age'].mean():.1f} years"
    ]
})
summary.to_csv('customer_summary.csv', index=False)
print("✅ Saved: customer_summary.csv")

print("\n" + "="*60)
print("✅ ETL PIPELINE COMPLETE!")
print("="*60)
print(f"\nCleaned {len(df)} customer records successfully!")