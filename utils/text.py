import re

non_url_safe = ['"', '#', '$', '%', '&', '+',
                ',', '/', ':', ';', '=', '?',
                '@', '[', '\\', ']', '^', '`',
                '{', '|', '}', '~', "'"]

translate_table = {ord(char): u'' for char in non_url_safe}
non_url_safe_regex = re.compile(
    r'[{}]'.format(''.join(re.escape(x) for x in non_url_safe)))


def snake_case(text):
    return re.sub(r'([A-Z])', r'_\1', text).lower()

def kebab(s):
    return '-'.join(re.sub(r"(\s|_|-)+"," ", re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())
