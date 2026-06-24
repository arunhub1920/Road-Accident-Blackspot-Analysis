import os
import pandas as pd

input_path = r"C:\Users\HP\Downloads\accidents_cleaned.csv"

df = pd.read_csv(input_path)

# Group by location
blackspots = df.groupby(['Latitude', 'Longitude']).agg({
    'Accident_ID': 'count',
    'Deaths': 'sum'
}).reset_index()

blackspots.rename(columns={'Accident_ID': 'Accident_Count'}, inplace=True)

blackspots['Blackspot'] = blackspots['Accident_Count'].apply(
    lambda x: 1 if x > 5 else 0
)

# ✅ CREATE data folder if not exists
os.makedirs("data", exist_ok=True)

blackspots.to_csv("data/blackspots.csv", index=False)

print(" Blackspots identified & saved to data/blackspots.csv")
