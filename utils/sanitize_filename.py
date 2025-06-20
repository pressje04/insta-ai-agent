import re

def safe_name(text: str):
    return re.sub(r'[^\w\-_\. ]', '_', text).replace(' ', '_').lower()