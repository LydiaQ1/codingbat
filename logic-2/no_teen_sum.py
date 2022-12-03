def fix_teen(n):
    """Write a separate helper "def fix_teen(n):"that takes in an int value and
    returns that value fixed for the teen rule. In this way, you avoid repeating the teen
    code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum()."""
    teen = False
    if n >= 13 and n < 15:
        teen = True
    elif n > 16 and n <= 19:
        teen = True
    else:
        teen = False
    return teen
 
def no_teen_sum(a, b, c):
    """Given 3 int values, a b c, return their sum. However,
    if any of the values is a teen -- in the range 13..19 inclusive -- then
    that value counts as 0, except 15 and 16 do not count as a teens. """
    if fix_teen(a):
        a = 0
    if fix_teen(b):
        b = 0
    if fix_teen(c):
        c = 0
    return  a + b + c

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))
