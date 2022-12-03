def without_end(str):
    """Given a string, return a version without the first and last char,
    so "Hello" yields "ell". The string length will be at least 2."""
    length = len(str)
    return str[1:length-1]

print(without_end('Hello'))
print(without_end('java'))
print(without_end('coding'))