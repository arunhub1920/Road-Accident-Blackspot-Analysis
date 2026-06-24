import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
input_path= r"C:\Users\HP\Downloads\blackspots.csv"


df = pd.read_csv(input_path)

X = df[['Latitude', 'Longitude', 'Accident_Count', 'Deaths']]
y = df['Blackspot']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Model trained successfully")


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ✅ CSV path (your path)
df = pd.read_csv(r"C:\Users\HP\Downloads\blackspots.csv")

# ✅ Scatter plot
sns.scatterplot(
    x='Longitude',
    y='Latitude',
    hue='Blackspot',
    data=df
)

plt.title("Accident Blackspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

