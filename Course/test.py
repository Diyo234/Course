import re

def extract_between_strings(text, start, end):
    pattern = re.compile(re.escape(start) + '(.*?)' + re.escape(end), re.DOTALL)
    match = pattern.search(text)
    if match:
        return match.group(1)
    else:
        return None

def replace_between_strings(text, start, end, replacement):
    pattern = re.compile(re.escape(start) + '(.*?)' + re.escape(end), re.DOTALL)
    return pattern.sub(lambda match: start + replacement + end, text)

print(replace_between_strings("Hello, my name is John", "Hello, my name ", "John", " not "))
