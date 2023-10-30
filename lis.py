import turtle
t = turtle.Turtle()
def draw_hexagon(x, y, side_len, color):
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.forward(side_len)
    for i in range(5):
        t.left(60)
        t.forward(side_len)
    t.end_fill()
    t.seth(0)


draw_hexagon(0,0,50, 'orange')
turtle.done()















