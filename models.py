import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import joblib

def train_and_save_model(data_path="data/combined_emails_with_natural_pii.csv", model_path="saved_models/email_classifier.pkl"):
    # Load the dataset
    df = pd.read_csv(data_path)
    
    # Extract email and label
    X = df['email']
    y = df['type']

    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build pipeline
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', LinearSVC())
    ])

    # Train
    pipeline.fit(X_train, y_train)

    # Save model
    joblib.dump(pipeline, model_path)

    # Print accuracy (optional)
    accuracy = pipeline.score(X_test, y_test)
    print(f"Model trained with accuracy: {accuracy:.2f}")
