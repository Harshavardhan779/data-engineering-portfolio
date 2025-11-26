"""
SALES DATA ANALYSIS PIPELINE
Author: Harsha
Purpose: My first data engineering project
"""

import pandas as pd
from datetime import datetime

print("="*60)
print("SALES DATA ANALYSIS PIPELINE")
print("="*60)
print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d')}")
print("="*60)

# STEP 1: EXTRACT - Load Data
print("\n📥 EXTRACTING DATA...")
df = pd.read_csv('sales_data.csv')
print(f"✅ Loaded {len(df)} records")
print("\nFirst 3 rows:")
print(df.head(3))

# STEP 2: TRANSFORM - Process Data
print("\n🔄 TRANSFORMING DATA...")
df['revenue'] = df['quantity'] * df['price']
print("✅ Added revenue column")

# STEP 3: ANALYZE - Generate Insights
print("\n📈 ANALYZING DATA...")

# Analysis 1: Total Revenue
total_revenue = df['revenue'].sum()
print(f"\n💰 TOTAL REVENUE: ₹{total_revenue:,.0f}")

# Analysis 2: Top Products by Revenue
print("\n🏆 TOP PRODUCTS BY REVENUE:")
top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
for i, (product, revenue) in enumerate(top_products.items(), 1):
    print(f"   {i}. {product}: ₹{revenue:,.0f}")

# Analysis 3: Revenue by City
print("\n🌆 REVENUE BY CITY:")
city_revenue = df.groupby('customer_city')['revenue'].sum().sort_values(ascending=False)
for city, revenue in city_revenue.items():
    print(f"   {city}: ₹{revenue:,.0f}")

# Analysis 4: Average Transaction
avg_transaction = df['revenue'].mean()
print(f"\n📊 AVERAGE TRANSACTION: ₹{avg_transaction:,.0f}")

# Analysis 5: Best Seller by Units
best_seller_qty = df.groupby('product')['quantity'].sum().sort_values(ascending=False)
print(f"\n⭐ BEST SELLER BY UNITS:")
print(f"   {best_seller_qty.index[0]}: {best_seller_qty.iloc[0]} units")

# STEP 4: LOAD - Save Results
print("\n💾 SAVING RESULTS...")

summary_df = pd.DataFrame({
    'Metric': ['Total Revenue', 'Total Transactions', 'Avg Transaction', 'Total Units'],
    'Value': [
        f"₹{total_revenue:,.0f}", 
        len(df), 
        f"₹{avg_transaction:,.0f}",
        df['quantity'].sum()
    ]
})

summary_df.to_csv('sales_summary.csv', index=False)
print("✅ Saved: sales_summary.csv")

print("\n" + "="*60)
print("✅ PIPELINE COMPLETE!")
print("="*60)