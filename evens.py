def even_evens(l):
    count = 0
    for n in l:
        if n%2 == 0:
            count += 1
    if count == 0:
        return False
            
    if count %2 == 0:
        return True
    else: 
        return False
        
    
    
assert even_evens([]) == False, "Empty list should return False"
assert even_evens([3]) == False, "Only odd numbers should return False"
assert even_evens([3, 6, 8]) == True, "Two even numbers should return True"
assert even_evens([2, 5, 4, 6]) == False, "Three even numbers should return False"

print("All tests pass")

