def makes10(a, b):
  if int(a) == 10 or int(b) == 10 or int(a) + int(b) == 10:
    return True
  else:
    return False

print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))