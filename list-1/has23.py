def has23(nums):
    """Given an int array length 2, return True if it contains a 2 or a 3."""
    if nums[0] == 2 or nums[1] == 2:
        return True
    if nums[0] == 3 or nums[1] == 3:
     return True
    else:
        return False

print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))