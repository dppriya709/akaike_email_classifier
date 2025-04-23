# Email Classifier API

This project provides an API that performs PII masking and classifies emails into categories.

## Setup Instructions

1. Clone the repository.
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the FastAPI app locally:
    ```bash
    uvicorn app:app --reload
    ```

## API Endpoints

- **POST /classify**
  - Input: Email body as a string.
  - Output: JSON with masked entities and email category.

## Deployment on Hugging Face

Follow the instructions below to deploy the application on Hugging Face Spaces.
