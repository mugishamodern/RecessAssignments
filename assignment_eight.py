# Assignment Eight: AgriSmart AI Data Science Task
# Load, clean, analyze, and export climate_action_data.csv
# Name: ______________________
# Date: ______________________

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv('climate_action_data.csv')

# 2. Inspect the data
print("\n--- DataFrame Info ---")
df.info()
print("\n--- Head ---")
print(df.head())
print("\n--- Missing Values ---")
print(df.isnull().sum())
print("\n--- Data Types ---")
print(df.dtypes)

# 3. Clean the data
# Remove duplicates
df = df.drop_duplicates()

# Replace 'error' and similar erroneous entries with NaN
df = df.replace('error', np.nan)

# Convert columns to numeric where possible
for col in df.columns:
    try:
        df[col] = pd.to_numeric(df[col])
    except:
        pass

# Handle missing values
# If a column has <10% missing, fill with median; else drop column (except 'CropType')
missing_percent = df.isnull().mean()
for col in df.columns:
    if missing_percent[col] > 0 and missing_percent[col] < 0.1 and col != 'CropType':
        df[col] = df[col].fillna(df[col].median())
    elif missing_percent[col] >= 0.1 and col != 'CropType':
        df = df.drop(columns=[col])
# Drop rows with missing CropType
if 'CropType' in df.columns:
    df = df.dropna(subset=['CropType'])

# 4. EDA
print("\n--- Descriptive Statistics ---")
print(df.describe(include='all'))

# Histograms for numeric variables
numeric_cols = df.select_dtypes(include=[np.number]).columns
plt.figure(figsize=(15, 8))
for i, col in enumerate(numeric_cols):
    plt.subplot(2, (len(numeric_cols)+1)//2, i+1)
    sns.histplot(df[col], kde=True, bins=20)
    plt.title(f"{col} Distribution")
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 5. Insights
insights = []
# Variables most influencing fertilizer recommendations (assume column 'FertilizerRecommendation' exists)
if 'FertilizerRecommendation' in df.columns:
    corr = df[numeric_cols].corr()['FertilizerRecommendation'].abs().sort_values(ascending=False)
    influencing_vars = corr.index[1:4].tolist()  # Exclude self-correlation
    insights.append(f"Variables most influencing fertilizer recommendations: {', '.join(influencing_vars)}")
else:
    insights.append("Column 'FertilizerRecommendation' not found for influence analysis.")

# Crop type with highest average soil moisture (assume 'SoilMoisture' and 'CropType' exist)
if 'SoilMoisture' in df.columns and 'CropType' in df.columns:
    avg_moisture = df.groupby('CropType')['SoilMoisture'].mean()
    top_crop = avg_moisture.idxmax()
    top_value = avg_moisture.max()
    insights.append(f"Crop type with highest average soil moisture: {top_crop} ({top_value:.2f})")
else:
    insights.append("'SoilMoisture' or 'CropType' column missing for moisture analysis.")

# Irrigation suggestions for crops with avg temp > 30°C (assume 'Temperature' and 'CropType' exist)
if 'Temperature' in df.columns and 'CropType' in df.columns:
    high_temp_crops = df.groupby('CropType')['Temperature'].mean()
    crops_above_30 = high_temp_crops[high_temp_crops > 30]
    if not crops_above_30.empty:
        for crop in crops_above_30.index:
            insights.append(f"Suggest increased irrigation for {crop} (avg temp: {crops_above_30[crop]:.2f}°C)")
    else:
        insights.append("No crops with average temperature above 30°C.")
else:
    insights.append("'Temperature' or 'CropType' column missing for irrigation suggestions.")

# 6. Export cleaned data
df.to_csv('cleaned_precision_agriculture_data.csv', index=False)

# 7. Print insights and recommendations
print("\n--- Insights and Recommendations ---")
for insight in insights:
    print("-", insight) 