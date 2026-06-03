import sys
import subprocess

def _ensure_package(pkg_name):
	try:
		return __import__(pkg_name)
	except ImportError:
		print(f"Package '{pkg_name}' not found. Attempting to install...")
		subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
		return __import__(pkg_name)

pd = _ensure_package('pandas')
np = _ensure_package('numpy')
_ensure_package('matplotlib')
import matplotlib.pyplot as plt
sns = _ensure_package('seaborn')

#Step 1: Load dataset
df = pd.read_csv("Accident_Information.csv")

print("Dataset Loaded Successfully")

#Step 2: Display Dataset Shape
print("\nDataset Shape:")
print(df.shape)

#Step 3: Display First 5 Records
print("\nFirst 5 Records:")
print(df.head())

#Step 4: Display Column Names
print("\nColumn Names:")
print(df.columns.tolist())

#Step 5: Dataset Information
print("\nDataset Information:")
print(df.info())

#Step 6: Check Missing Values
print("\nMissing Values:")
missing = df.isnull().sum()
print(missing[missing > 0])

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

#Step 7: Check Target Classes
print("\nAccident Severity Values:")
print(df['Accident_Severity'].unique())

#Step 8: Check Weather Values
print("\nWeather Conditions:")
print(df['Weather_Conditions'].unique())

#Step 9: Check Road Surface Values
print("\nRoad Surface Conditions:")
print(df['Road_Surface_Conditions'].unique())

#Step 10: Check Light Conditions Values
print("\nLight Conditions:")
print(df['Light_Conditions'].unique())

#Step 11: Severity Distribution Plot
plt.figure(figsize=(8,5))

sns.countplot(
    x='Accident_Severity',
    data=df
)

plt.title("Accident Severity Distribution")
plt.tight_layout()
plt.show()

#Step 12: Create 50K Sample for EDA
# Create sample dataset for faster analysis
eda_df = df.sample(n=50000, random_state=42)

print("EDA Sample Shape:")
print(eda_df.shape)

#Step 13: Weather Conditions vs Severity
weather_severity = pd.crosstab(
    eda_df['Weather_Conditions'],
    eda_df['Accident_Severity']
)

print("\nWeather vs Severity:")
print(weather_severity)

weather_severity.plot(
    kind='bar',
    figsize=(12,6)
)

plt.title("Weather Conditions vs Accident Severity")
plt.xlabel("Weather Conditions")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()

#Step 14: Road Surface Conditions vs Severity
road_severity = pd.crosstab(
    eda_df['Road_Surface_Conditions'],
    eda_df['Accident_Severity']
)

print("\nRoad Surface vs Severity:")
print(road_severity)

road_severity.plot(
    kind='bar',
    figsize=(10,6)
)

plt.title("Road Surface Conditions vs Accident Severity")
plt.xlabel("Road Surface Conditions")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()

#Step 15: Light Conditions vs Severity
light_severity = pd.crosstab(
    eda_df['Light_Conditions'],
    eda_df['Accident_Severity']
)

print("\nLight Conditions vs Severity:")
print(light_severity)

light_severity.plot(
    kind='bar',
    figsize=(10,6)
)

plt.title("Light Conditions vs Accident Severity")
plt.xlabel("Light Conditions")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()

#Step 16: Speed Limit vs Severity
plt.figure(figsize=(8,5))

sns.boxplot(
    x='Accident_Severity',
    y='Speed_limit',
    data=eda_df
)

plt.title("Speed Limit vs Accident Severity")
plt.xlabel("Accident Severity")
plt.ylabel("Speed Limit")
plt.tight_layout()
plt.show()

#Step 17: Urban vs Rural Analysis
urban_severity = pd.crosstab(
    eda_df['Urban_or_Rural_Area'],
    eda_df['Accident_Severity']
)

print("\nUrban/Rural vs Severity:")
print(urban_severity)

urban_severity.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Urban/Rural Area vs Accident Severity")
plt.tight_layout()
plt.show()

#Step 18: Save the 50K Dataset for M2
eda_df.to_csv(
    "accident_50k.csv",
    index=False
)

print("\n50K Sample Dataset Saved Successfully")