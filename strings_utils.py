import re

def count_char(string, char):
    # Если это не строка или не один символ - возвращаем 0
    if not isinstance(string, str) or not isinstance(char, str) or len(char) != 1:
        return 0
    return string.count(char)

def is_valid_email(email):
    # Самая простая проверка на почту
    if not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
