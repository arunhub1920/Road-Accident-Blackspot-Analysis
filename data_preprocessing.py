import pandas as pd

input_path = r"C:\Users\HP\Downloads\accidents_raw.csv"
output_path = r"C:\Users\HP\Downloads\accidents_cleaned.csv"

df = pd.read_csv(input_path)

df = df.dropna()

df['Date'] = pd.to_datetime(df['Date'])
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour

df.to_csv(output_path, index=False)

print(" Data cleaned successfully and saved as accidents_cleaned.csv")
