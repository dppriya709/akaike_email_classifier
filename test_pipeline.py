from app import process_email_pipeline

email_text = "Hello, my name is John Doe. My email is john.doe@example.com and my phone number is 9876543210. I have an issue with my billing."

result = process_email_pipeline(email_text)

print(result)
