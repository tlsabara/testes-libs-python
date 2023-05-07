# import turtle
# from random import choice
#
# turtle.speed(50)
# turtle.bgcolor('black')
#
# for i in range(254):
#     turtle.color(choice(['yellow', 'green', 'blue', 'red']))
#     turtle.forward(i)
#     turtle.left(i+i//2)
#     turtle.hideturtle()
# turtle.done()


# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(30)
#     left(13)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

import turtle
from random import choice

turtle.speed(50)
turtle.bgcolor('black')


turtle.color(choice(['yellow', 'green', 'blue', 'red']))

#base
turtle.forward(300)
turtle.left(25)
turtle.forward(30)
turtle.left(25)
turtle.forward(30)
turtle.left(40)

# dedo 1
turtle.forward(200)
turtle.left(25)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(40)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(40)
turtle.forward(100)

#dedo 2
turtle.left(180)
turtle.forward(110)
turtle.left(25)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(40)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(40)
turtle.forward(100)

#dedo 2
turtle.left(180)
turtle.forward(180)
turtle.left(25)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(40)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(40)
turtle.forward(180)

#dedo 2
turtle.left(180)
turtle.forward(110)
turtle.left(25)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(40)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(25)
turtle.forward(20)
turtle.left(40)
turtle.forward(150)

turtle.done()