"""
Salary: Polevik Alexey = 25
        Elizarev Yaroslav = 40
        Nechaev Egor = 40
"""

import turtle

t = turtle.Turtle()
t.speed(100)
t.width(2)
t.pencolor("black")


def Trngl(x, y, scale, angle):
  t.up()
  t.fillcolor("orange")
  t.goto(x, y)
  t.right(angle)
  t.down()
  t.begin_fill()
  t.forward(100*scale)
  t.left(110)
  t.forward(146.1902*scale)
  t.left(140)
  t.forward(146.1902*scale)
  t.end_fill()
  t.seth(0)
  '''
  Draws orange triangle.
  x, y - start coordinates,
  scale - triangle scale,
  angle - turning angle.
  '''
  pass


def Tail(x, y):
  t.up()
  t.fillcolor("orange")
  t.goto(x,y)
  t.down()
  t.begin_fill()
  t.left(90)
  t.forward(28.7939*7)
  t.right(100)
  t.forward(10*7)
  t.right(100)
  t.forward(28.7939*7)
  t.end_fill()
  t.seth(0)
  '''
  Draws triangle-tail.
  x, y - start coordinates.
  '''
  pass


def Trtrngl(x, y, scale):
  t.up()
  t.fillcolor("forestgreen")
  t.goto(x, y)
  t.down()
  t.begin_fill()
  t.forward(51.764*scale)
  t.left(105)
  t.forward(100*scale)
  t.left(150)
  t.forward(100*scale)
  t.end_fill()
  t.seth(0)
  '''
  Draws green triangle.
  x, y - start coordinates,
  scale - scale of the triangle.
  '''
  pass


def Crcl(x, y, size, color):
  t.up()
  t.goto(x, y)
  t.fillcolor(color)
  t.down()
  t.begin_fill()
  t.circle(size)
  t.end_fill()
  t.seth(0)
  '''
  Draws circle.
  x,y - start coordinates,
  size - size of the radius of the circle,
  color - color of filling.
  '''
  pass


def Smile(x, y, size, width):
  t.up()
  t.goto(x, y)
  t.pencolor("red")
  t.down()
  t.left(90)
  t.width(width)
  t.circle(size, -180)
  t.width(2)
  t.pencolor("black")
  t.seth(0)
  '''
  Draws red half circle.
  x, y - start coordinates,
  size - size of radius of the half circle,
  width - pen width.
  '''
  pass


def Rec(x, y, a, b, color):
  t.up()
  t.goto(x, y)
  t.fillcolor(color)
  t.down()
  t.begin_fill()
  for i in range(2):
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(90)
  t.end_fill()
  t.seth(0)
  '''
  Draws rectangle.
  x, y - start coordinates,
  a, b - sides length,
  color - color of filling.
  '''
  pass

# Sun
Crcl(300, 200, 100, 'Yellow')

# Landscape
turtle.bgcolor('RoyalBlue')
Rec(-1000, -800, 2000, 600, 'green')

# Trees
Rec(650, -200, 30, 300, 'brown')
Trtrngl(665 - 26*5, -150, 5)
Trtrngl(665 - 26*4, 0, 4)
Trtrngl(665 - 26*3, 150, 3)
Rec(-375, -200, 30, 300, 'brown')
Trtrngl(-360 - 26*5, -150, 5)
Trtrngl(-360 - 26*4, 0, 4)
Trtrngl(-360 - 26*3, 150, 3)

# Fox
Trngl(0, -200, 2, 0)
Tail(205, -185)
Trngl(115, 90, 1.7, 235)
Trngl(70, 155, 0.5, 55)
Trngl(31, 210, 0.5, 55)
Crcl(45, 106, 15, "White")
Crcl(35, 115, 5, "black")
Crcl(-5, 155, 15, "White")
Crcl(-15, 164, 5, "black")
Crcl(-128, 20, 8, "red")

# Kolobok
Crcl(-165, 40, 80, "Khaki")
Smile(-135, 90, 30, 5)
Crcl(-130, 120, 13, "blue")
Crcl(-200, 120, 13, "blue")

# Flag
Rec(-610, -200, 10, 550, 'silver')
Crcl(-605, 350, 10, 'gold')
Rec(-600, 200, 225, 50, "red")
Rec(-600, 250, 225, 50, "blue")
Rec(-600, 300, 225, 50, "white")

t.up()
t.home()
t.hideturtle()
turtle.done()