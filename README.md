Project Overview
This project is developed as part of the internship assignment for Akaike Technologies. The goal is to build an API-based system that classifies support team emails into categories and masks personally identifiable information (PII) in the email content.

2. Problem Statement
Given an incoming email with a subject and body, the system should:

Detect and mask any personally identifiable information (PII)
Classify the email into predefined categories (e.g., complaint, query, return, etc.)
Return the results in a strictly defined JSON format

3. Model Details
Model Used: Logistic Regression (or specify your actual model)
Vectorizer: TfidfVectorizer
Training Data: Custom labeled dataset with email samples

5. System Pipeline
Input: Accepts JSON with subject and body
Combine Text: Concatenates subject and body into one string
PII Masking: Detects and replaces PII using regular expressions and named entity recognition (NER)
Text Cleaning: Lowercasing, removing stopwords, special characters, etc.
Vectorization: Transforms text using TfidfVectorizer
Classification: Predicts the category using the trained model
Output: Returns a structured JSON response

7. PII Detection & Masking
Types of PII detected include:

Phone Numbers
Email Addresses
Aadhar Numbers
Dates
Expiry Numbers
Each entity is replaced with a corresponding placeholder like [phone], [aadhar_num], etc., and recorded in a list with position, classification, and original text.

## API Endpoints

- **POST /classify**
  - Input: Email body as a string.
  - Output: JSON with masked entities and email category.
  - 
  - 

## Deployment on Hugging Face

Follow the instructions below to deploy the application on Hugging Face Spaces.
hugging face deployements links:https://huggingface.co/spaces/priyaDP/akaike_email_classifier1
