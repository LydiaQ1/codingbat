def make_chocolate(small, big, goal):
    """We want make a package of goal kilos of chocolate. We have small bars (1 kilo each)
    and big bars (5 kilos each). Return the number of small bars to use, assuming we always
    use big bars before small bars. Return -1 if it can't be done."""
    total = small + (5*big) 

    if total == goal:  
        return small       

    if total < goal:   
        return -1
   
    if big*5 < goal and (goal - big*5) <= small:    
        return goal - (big*5)                       

    else:
        rem = goal % 5       
        if rem == small:     
            return small 
        if rem > small:     
            return -1               
        else:
            return rem    

print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))
  