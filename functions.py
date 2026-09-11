'''FUNCTIONS
(1) Define vs Call
(2) Parameters vs Arguments
(3) Keyword vs Default Arguments
(4) Scope
'''

print("=========Define vs Call=========")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - parameter
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)


print("=========Keyword vs Default Arguments=========")

# DEFINE
def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"

 
# CALL
result3 = give_greet(name="Justin", age=28)
print("result3:", result3)

result4 = give_greet("John")
print("result4:", result4)

print("=========Scope=========")
b = 100  # 3

# DEFINE
def calculate(a):  # 2
    c = a * b  # 1
    print(f"the c value: {c}")


# CALL
calculate(5)