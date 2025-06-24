# Assignment Seven:
# Use the provided data.csv to plot histograms for 'Duration' and 'Pulse' columns with a smooth curve.
# Name: ______________________
# Date: ______________________

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('data.csv')

# Set up the plot
plt.figure(figsize=(12, 5))

# Duration Distribution
plt.subplot(1, 2, 1)
sns.histplot(df['Duration'], kde=True, bins=20, color='skyblue')
plt.title('Duration Distribution')
plt.xlabel('Duration')
plt.ylabel('Count')

# Pulse Distribution
plt.subplot(1, 2, 2)
sns.histplot(df['Pulse'], kde=True, bins=20, color='steelblue')
plt.title('Pulse Distribution')
plt.xlabel('Pulse')
plt.ylabel('Count')

plt.tight_layout()
plt.show() 