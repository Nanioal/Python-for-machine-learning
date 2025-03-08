import re

email_text = "Contact us at support@example.com or at helpdesk@mysite.org."
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Using re.finditer()
matches = re.finditer(pattern, email_text)
emails = [match.group() for match in matches]

print(emails)
