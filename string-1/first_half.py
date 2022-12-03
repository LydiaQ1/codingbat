def first_half(str):
    """Given a string of even length, return the first half. So the string "WooHoo" yields "Woo"."""
    length = len(str)
    return str[0:length/2]

print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))
