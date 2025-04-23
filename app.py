import joblib

from utils import mask_email

# Load the trained model
model = joblib.load("saved_models/email_classifier.pkl")

def process_email_pipeline(email_text):
    # Step 1: Mask the PII
    masked_text, entities = mask_email(email_text)

    # Step 2: Predict category using masked email
    category = model.predict([masked_text])[0]

    # Step 3: Format response
    result = {
        "input_email_body": email_text,
        "list_of_masked_entities": entities,
        "masked_email": masked_text,
        "category_of_the_email": category
    }

    return result

