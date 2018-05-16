# def count_upper_case(message):
# 	count = 0
# 	for c in message:
# 		if c.isupper():
# 			count += 1
# 	return count

def count_upper_case(message):
    # return sum([1 for c in message if c.isupper()])
    return len([c for c in message if c.isupper()])
    

assert count_upper_case("") == 0, "Empty String should return 0"
assert count_upper_case("A") == 1, "A should return 1"
assert count_upper_case("12345") == 0, "int should return 0"
assert count_upper_case("I am a Good Guy") == 3, "I am a Good Guy should return 3"
assert count_upper_case("ddddddd") == 0, "ddddddd should return 0"
print("All tests pass")
# print(count_upper_case("Abcd"))


