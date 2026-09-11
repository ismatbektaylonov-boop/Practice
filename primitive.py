print("=========number=========")
# in Java, variable is a name storage location
# in Python, variable is a name reference

count = 100
count_type = type(count)
# print("count: ", count, "count_type: ", count_type)
print(f"count: {count}, count_type: {count_type}")

result1 = count.bit_count() # methods
print(f"result1: {result1}")

result2 = count.numerator() # state
print(f"result2: {result2}")

print("=========string=========")
# Methods: upper(), lower(), title(), find(), replace(), split(), join()

course = "AI Python FullStack"
result = type(course)
print(f"the result (1): {result}")
result = course.title()
print(f"the result (2): {result}")

result = course.upper() 
print(f"the result (3): {result}")

result = course.replace("FullStack", "MasterClass")
print(f"the result (4): {result}")
# print(course)

print("=========boolean=========")
# functions: type(), input(), print(), int(), str()
y = input("Enter a number: ")
# print("y: ", y)
result = y.isnumeric() 
print(f"the input value is numeric: {result}")

# Truthy vs Falsy values
# Truthy values: non-zero numbers, non-empty strings, non-empty lists, True
# Falsy values: 0, empty strings, empty lists, None, False

test_falsy = "" or False or 0 or None
print(f"the test_falsy: {bool(test_falsy)}")

test_truthy = "Hello" or True or 1 or [1, 2, 3]
print(f"the test_truthy: {bool(test_truthy)}")