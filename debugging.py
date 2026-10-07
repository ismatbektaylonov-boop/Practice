'''Debugging & package
(1) Python peckages & core package
(2) Package menager & externial peckage
(3) Debbuging
'''

# import turtle

# from PIL import Image
# pillow. package orqari b is rasimning size va razmerini bera olar ekanmiz.
# import turtle
# print("===========Python peckages & core package ========== ")

# ''' Python peckages/ Modules: core,file and extrnial'''
# # core peckages https://docs.python.org/3/library
import turtle
# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pizza with Turtle")

# Turtle setup
t = turtle.Turtle()
t.speed(1)

# Draw pizza base
t.penup()
t.goto(0, -150)
t.pendown()
t.color("orange")
t.begin_fill()
t.circle(150)
t.end_fill()

# Draw cheese layer
t.penup()
t.goto(0, -130)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(130)
t.end_fill()

# Pepperoni positions
pepperoni = [
    (-50, 50), (40, 60), (-70, -20),
    (60, -10), (0, 0), (-20, -70),
    (70, -70)
]

# Draw pepperoni
t.color("red")
for x, y in pepperoni:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

# Slice lines
t.color("brown")
t.pensize(3)

for angle in [0, 60, 120]:
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    t.forward(150)

    t.penup()
    t.goto(0, 0)
    t.setheading(angle + 180)
    t.pendown()
    t.forward(150)

t.hideturtle()
turtle.done()
# import turtle

# # Maashina turtle qopheessuu
# pen = turtle.Turtle()
# screen = turtle.Screen()

# screen.bgcolor("black")  # Duubbee (background) gurraacha
# pen.color("red")         # Halluu diimaa
# pen.fillcolor("red")     # Halluu keessatti guutamu
# pen.speed(3)             # Saffisa kaasuu

# # Onnee kaasuu eegaluu
# pen.begin_fill()

# pen.left(140)
# pen.forward(113)

# # Geengoo (curve) onnee gara bitaa
# for _ in range(200):
#     pen.right(1)
#     pen.forward(1)

# pen.left(120)

# # Geengoo (curve) onnee gara mirgaa
# for _ in range(200):
#     pen.right(1)
#     pen.forward(1)

# pen.forward(112)

# pen.end_fill()

# # Qalamni akka hin mul'anne dhoksuu
# pen.hideturtle()

# # Fakkichaa erga kaasee booda akka hin cufamneef
# turtle.done()

# my_file = open("material/message.txt", "r")

# try:
#     content = my_file.read()
#     print("content:", content)
# finally:
#     my_file.close()


# with open("material/message.txt", "r") as your_file:
#     your_content = your_file.read()
#     print("your_content", your_content)

# print("DONE")

# print("========== Package menager & externial peckage ==========")
# ''' peckage meagers: pip pipenv npm yarn comproser brew'''
# # externial peckage https://pypi.org/


# with Image.open("material/mvc.jpg") as img_obj:
#     resized_img = img_obj.resize((400, 200))
#     resized_img.show()
#     resized_img.save("material/sample.jpg")

# print("=========== Debbuging ===========")
# # Debbuging. orqari biz xatolarni bir zumda topip ,jarayonni
# # huddi mashina oylayotgan singari kuchli taxlilni amalga oshirishimiz
# # mumkin bolar ekan.


# def get_summary(*args):   # DEFINE
#     total_amount = 0

#     for a in args:

#         total_amount += a

#     return total_amount


# result = get_summary(1, 2, 3, 4, 5)   # CALL
# print("result:", result)