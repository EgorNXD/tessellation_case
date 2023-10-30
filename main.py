import turtle

t = turtle.Turtle()
t.speed(1)
t.pencolor("black")

def get_num_hexagons():
    f = False
    while not f:
        try:
            N = int(input("Пожалуйста, введите количество шестиугольников, распологаемых в ряд:"))
            if (str(N).isdigit() and (4 <= N <= 20)):
                f = True
            else:
                print("Оно должно быть от 4 до 20.")
                N = int(input("Пожалуйста, повторите попытку:"))
            return N
        except ValueError:
            print("Это не число о_о")





t.up()
t.home()
t.hideturtle()
turtle.done()