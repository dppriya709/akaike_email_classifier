Email Classifier & PII Masking System - README

🔍 Project Overview

This project was developed as part of the internship assignment for Akaike Technologies. It builds an API that processes support team emails to:

Detect and mask Personally Identifiable Information (PII)

Classify emails into predefined categories (e.g., complaint, query, return)

✅ Step-by-Step Breakdown with PIMTs

Step 1: Define the Problem

Problem: Manual email handling is inefficient and unsafe.

Input: JSON with subject and body.

Output: JSON with:

Masked content

PII details (type, position, original)

Email category (e.g., Complaint)

Step 2: Collect and Preprocess Data

Problem: No labeled dataset

Input: Email dataset

Methods:

Collect real or synthetic emails

Annotate manually or semi-automatically

Tools: nltk, spaCy, regex

Preprocessing Includes:

Lowercasing

Stopword removal

Removing special characters and extra numbers

Step 3: Build the PII Masking System

Methods:

Regex patterns for phone, email, Aadhar, dates

spaCy for NER (e.g., names, locations)

Tools: re, spaCy

Masking: Replace with placeholders like [email], [phone_number]

Step 4: Build the Classification Model

Vectorization: TfidfVectorizer

Model: LogisticRegression (or similar)

Pipeline:

Train/test split (80/20)

Model training and evaluation

Step 5: Integrate Everything

Pipeline:

Input JSON →

PII Masking →

Text Cleaning →

Vectorization →

Classification →

JSON Output

Step 6: Build the API

Framework: FastAPI or Flask

Endpoint: POST /classify

Deployment:

Local for testing

Cloud (e.g., Hugging Face Spaces)

Step 7: Testing and Evaluation

Methods:

Unit tests for masking and classification

Confusion matrix, F1 score for model

Real-world email testing

🚀 API Sample Usage

Endpoint: POST /classify

## API Endpoints

- **POST /classify**
  - Input: Email body as a string.
  -''' {
  "input_email_body": "Dear Support Team, I am writing to complain about the delay in receiving my order. My order number is 1234567890, and my tracking number is A1234B5678. I placed the order on 15th March 2025, but it still hasn't arrived. Please help resolve this issue. My contact number is +1-800-123-4567, and my email is johndoe@example.com. Looking forward to your prompt reply. Regards, John Doe"
}'''
  - Output: JSON with masked entities and email category.
  - {
  "input_email_body": "Dear Support Team, I am writing to complain about the delay in receiving my order. My order number is 1234567890, and my tracking number is A1234B5678. I placed the order on 15th March 2025, but it still hasn't arrived. Please help resolve this issue. My contact number is +1-800-123-4567, and my email is johndoe@example.com. Looking forward to your prompt reply. Regards, John Doe",
  "list_of_masked_entities": [
    {
      "position": [
        0,
        11
      ],
      "classification": "full_name",
      "entity": "Dear Support"
    },
    {
      "position": [
        374,
        385
      ],
      "classification": "full_name",
      "entity": "John Doe"
    },
    {
      "position": [
        305,
        312
      ],
      "classification": "email",
      "entity": "johndoe@example.com."
    },
    {
      "position": [
        101,
        115
      ],
      "classification": "phone_number",
      "entity": "1234567890"
    },
    {
      "position": [
        279,
        287
      ],
      "classification": "cvv_no",
      "entity": "800"
    },
    {
      "position": [
        283,
        291
      ],
      "classification": "cvv_no",
      "entity": "123"
    }
  ],
  "masked_email": "[full_name] Team, I am writing to complain about the delay in receiving my order. My order number is [phone_number], and my tracking number is A1234B5678. I placed the order on 15th March 2025, but it still hasn't arrived. Please help resolve this issue. My contact number is +1-[cvv[cvv_no]]-123-4567, and my email is [email] Looking forward to your prompt reply. Regards, J[full_name]",
  "category_of_the_email": "Problem"
}
  - 
Accepts email content and returns classification with PII masking. Request Body:

  - Response headers
 content-length: 1301 
 content-type: application/json 
 date: Thu,24 Apr 2025 12:00:27 GMT 
 server: uvicorn 
  - 

## Deployment on Hugging Face

Follow the instructions below to deploy the application on Hugging Face Spaces.
hugging face deployements links:https://huggingface.co/spaces/priyaDP/akaike_email_classifier1
Github repository:https://github.com/dppriya709/akaike_email_classifier.git
Fast UGI:http://127.0.0.1:8000/docs




Conclusion
This system is a lightweight and production-ready solution for automating email triaging and PII protection in customer support communications. The API strictly adheres to the format required by Akaike Technologies for automated evaluation.
