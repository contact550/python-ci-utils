import re

def count_char(string, char):
    if not isinstance(char, str) or len(char) != 1:
        return 0
    return string.count(char)

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return bool(re.match(pattern, email))
