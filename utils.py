import re

# Define regex patterns for each PII entity
PII_PATTERNS = {
    "full_name": r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b",
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone_number": r"\b\d{10}\b",
    "dob": r"\b\d{2}/\d{2}/\d{4}\b",
    "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/([0-9]{2})\b"
}

def mask_email(email_text):
    masked_text = email_text
    masked_entities = []

    for entity_type, pattern in PII_PATTERNS.items():
        for match in re.finditer(pattern, masked_text):
            original = match.group()
            start, end = match.start(), match.end()
            placeholder = f"[{entity_type}]"

            # Replace only the first occurrence of this entity
            masked_text = masked_text[:start] + placeholder + masked_text[end:]

            # Update the list
            masked_entities.append({
                "position": [start, start + len(placeholder)],
                "classification": entity_type,
                "entity": original
            })

    return masked_text, masked_entities
