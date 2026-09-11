# Dunder methods __builtins__, __init__
message = "Python: Everything is an object!"
print(message)

result = type(message)
print("result: ", result)

'''
In Python, there are built-in tools:
(1)TYPES -> int, float, str, list, dict, tuple, set, bool
(2)FUNCTIONS -> print(), len(), type(), input(), range(), sum(), min(), max(), sorted()
(3)EXCEPTIONS -> True, False, None, ValueError, TypeError, IndexError, KeyError, ZeroDivisionError
'''

print(dir(__builtins__))  # List all built-in functions and types