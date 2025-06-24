# Churn Prediction with TensorFlow
# 1. Build a TensorFlow churn model
# 2. Train and predict
# 3. Save and reload the model
# Name: ______________________
# Date: ______________________

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 1. Load and preprocess data
df = pd.read_csv('Churn.csv')

# Basic preprocessing (example: drop rows with missing values)
df = df.dropna()

# Assume 'Churn' is the target column (1=churn, 0=no churn)
# Encode categorical variables
y = df['Churn']
X = df.drop('Churn', axis=1)

for col in X.select_dtypes(include=['object']).columns:
    X[col] = LabelEncoder().fit_transform(X[col])

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 2. Build TensorFlow model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 3. Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Predict on test set
y_pred = (model.predict(X_test) > 0.5).astype(int)
print("\nSample predictions:", y_pred[:10].flatten())

# 4. Save the model
model.save('churn_model.h5')
print("Model saved as churn_model.h5")

# Reload the model and predict again
loaded_model = tf.keras.models.load_model('churn_model.h5')
reloaded_pred = (loaded_model.predict(X_test) > 0.5).astype(int)
print("\nSample predictions from reloaded model:", reloaded_pred[:10].flatten()) 