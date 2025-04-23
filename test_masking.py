from utils import mask_email

test_email = "Hello, my name is John Doe. My email is john.doe@example.com and phone is 9876543210."

masked, entities = mask_email(test_email)

print("Masked Email:\n", masked)
print("\nEntities:\n", entities)
