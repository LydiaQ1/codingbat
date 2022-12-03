def string_splosion(str):
    """Given a non-empty string like "Code" return a string like "CCoCodCode"."""
    newstri = ""
    for i in range(len(str)):
        newstri += str[:i+1]
    return newstri

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))