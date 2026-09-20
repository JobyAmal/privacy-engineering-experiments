import re

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
ssn_pattern = r'\b(?!000|666|9\d{2})\d{3}[-\s]?(?!00)\d{2}[-\s]?(?!0000)\d{4}\b'
mob_pattern = r'\b\d{10}\b'

def masked_ssn (ssn_string):
    return f"###-##-{ssn_string[-4:]}"

def masked_email (email_string):
    return f"{email_string[:4]}*********{email_string[-8:]}"

def masked_number (number):
    return f"#####{number[-5:]}"

with open("database_dump.txt", "r") as file:
    for line in file:
        emails = re.findall(email_pattern, line)
        ssns = re.findall(ssn_pattern, line)
        mob = re.findall(mob_pattern, line)

        if emails:
                for email in emails:
                    masked = masked_email(email)
                    print("PII Alert - Email found:", masked)
        if ssns:
                for ssn in ssns:
                    masked = masked_ssn(ssn)
                    print ("PII Alert - SSN Found:", masked)

        if mob:
                for mobile in mob:
                    masked = masked_number(mobile)
                    print("PII Alert - Mobile Found:", masked)
