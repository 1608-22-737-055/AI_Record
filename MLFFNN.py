
# Multi-Layer Feed Forward Neural Network (MLFFNN)

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize the Multi-layer Feed Forward Neural Network (MLPClassifier)
mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=1000, activation='relu', solver='adam', random_state=42)

# Train the model
mlp.fit(X_train, y_train)

# Predict on the test set
y_pred = mlp.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=data.target_names)

print("Accuracy:", accuracy)
print("Classification Report:\n", report)


# # Explanation
# This code trains a Multi-Layer Feed Forward Neural Network (MLFFNN) on the Iris dataset and evaluates its performance.

# 1. Data Loading: The Iris dataset is loaded using load_iris() from scikit-learn.
# 2. Data Split: The dataset is split into training and test sets using train_test_split().
# 3. Feature Standardization: The features are standardized using StandardScaler() to improve model performance.
# 4. MLPClassifier Initialization: An MLFFNN is initialized with a single hidden layer of 50 neurons, ReLU activation, Adam solver, and a random state of 42.
# 5. Model Training: The model is trained on the training data using fit().
# 6. Prediction: The trained model predicts the labels for the test data using predict().
# 7. Evaluation: The accuracy of the model is evaluated using accuracy_score(), and a classification report is generated using classification_report().

# The output shows the accuracy of the model and a classification report, which provides detailed metrics for each class.