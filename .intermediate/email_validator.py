# email_validator.py
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    email = input("Enter an email address to validate: ")
    if is_valid_email(email):
        print("The email address is valid.")
    else:
        print("The email address is invalid.")
