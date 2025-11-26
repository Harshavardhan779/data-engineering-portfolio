"""
WEATHER DATA ANALYZER
Author: Harsha
Date: November 24, 2025
Purpose: Simple data analysis project - Day 8
"""

import pandas as pd

print("="*50)
print("WEATHER DATA ANALYZER")
print("="*50)

# EXTRACT - Load data
print("\n📥 Loading weather data...")
df = pd.read_csv('weather_data.csv')
print(f"✅ Loaded {len(df)} weather records")

print("\n🌦️ Sample Data:")
print(df.head(3))

# TRANSFORM - Basic processing
print("\n🔄 Processing data...")

# Analysis 1: Average temperature by city
print("\n🌡️ AVERAGE TEMPERATURE BY CITY:")
avg_temp = df.groupby('city')['temperature'].mean().round(1)
for city, temp in avg_temp.items():
    print(f"   {city}: {temp}°C")

# Analysis 2: Most common weather condition
print("\n☁️ MOST COMMON CONDITIONS:")
conditions = df['condition'].value_counts()
for condition, count in conditions.items():
    print(f"   {condition}: {count} days")

# Analysis 3: Hottest day
hottest = df.loc[df['temperature'].idxmax()]
print(f"\n🔥 HOTTEST DAY:")
print(f"   {hottest['city']} on {hottest['date']}: {hottest['temperature']}°C")

# Analysis 4: Most humid city
print("\n💧 AVERAGE HUMIDITY BY CITY:")
avg_humidity = df.groupby('city')['humidity'].mean().round(1)
for city, humidity in avg_humidity.items():
    print(f"   {city}: {humidity}%")

# LOAD - Save summary
print("\n💾 Saving summary...")
summary = pd.DataFrame({
    'City': avg_temp.index,
    'Avg_Temperature': avg_temp.values,
    'Avg_Humidity': avg_humidity.values
})
summary.to_csv('weather_summary.csv', index=False)
print("✅ Summary saved to weather_summary.csv")

print("\n" + "="*50)
print("✅ ANALYSIS COMPLETE!")
print("="*50)