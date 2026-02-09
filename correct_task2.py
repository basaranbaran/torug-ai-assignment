import re

def count_valid_emails(emails):
    count = 0
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    for email in emails:
        try:
            if re.match(email_pattern, email):
                count += 1
        except TypeError:
            continue

    return count