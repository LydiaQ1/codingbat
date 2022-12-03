def string_bits(str):
    """Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo"."""
    newstri = ""
    for i in range(len(str)):
        if i % 2 == 0:
            newstri = newstri + str[i]
    return newstri

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))