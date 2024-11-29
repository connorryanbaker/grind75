import re

def is_palindrome(self, s: str) -> bool:
    test_string = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
    return test_string == ''.join(reversed(list(test_string)))
