def near_ten(num):
    """Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
    Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2."""
    if num % 10 <= 2 and num % 10 >= 0:
        return True
    elif num % 10 >= 8 and num % 10 <= 9:
        return True
    else:
        return False

print(near_ten(12))
print(near_ten(17))
print(near_ten(19))