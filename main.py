import turtle

t = turtle.Turtle()
t.speed(0)
t.pencolor("black")
t.up()
t.goto(-250, 250)


def get_num_hexagons():
    f = False
    while not f:
        try:
            N = int(input("Пожалуйста, введите количество шестиугольников, располагаемых в ряд:"))
            if 4 <= N <= 20:
                f = True
            else:
                print("Оно должно быть от 4 до 20.")
                N = int(input("Пожалуйста, повторите попытку:"))
            return N
        except ValueError:
            print("Это не число о_о")


def get_color_choice():
    colorsRus = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'фиолетовый']
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    print('Допустимые цвета заливки: \n красный\n оранжевый\n желтый\n зеленый\n голубой\n фиолетовый\n')
    colorNameRus = input('Пожалуйста введите цвет: ')
    while colorNameRus.lower() not in colorsRus:
        print('"', colorNameRus, '"', 'не является верным значением.')
        colorNameRus = input('Введите корректный цвет:')
    colorName = colors[colorsRus.index(colorNameRus.lower())]
    return colorName


def draw_hexagon(x, y, side_len, color):
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.forward(side_len)
    for i in range(5):
        t.left(60)
        t.forward(side_len)
    t.end_fill()
    t.up()
    t.seth(0)


def drawAll(N, colorName1, colorName2):
    shortDiagonal = 500 / N
    side_len = shortDiagonal / (3 ** (1 / 2))
    colorsInUse = [colorName1, colorName2]
    colorsCount = 0
    for i in range(N // 2):
        for j in range(((i + 1) * 2)):
            x, y = t.pos()
            draw_hexagon(x, y, side_len, colorsInUse[i % 2])
            t.right(120)
            t.forward(shortDiagonal)
            t.seth(0)
        t.left(60)
        t.forward(shortDiagonal * ((i + 1) * 2))
        t.seth(0)
        t.forward(shortDiagonal)
        colorsCount += 1
    if N % 2 == 1:
        for j in range(((i + 1) * 2) + 1):
            x, y = t.pos()
            draw_hexagon(x, y, side_len, colorsInUse[(i + N % 2) % 2])
            t.right(120)
            t.forward(shortDiagonal)
            t.seth(0)
        t.left(60)
        t.forward(shortDiagonal * N)
        t.seth(0)
        t.forward(shortDiagonal)
        colorsCount += 1
    for i in range((N // 2) - 1):
        for j in range(N):
            x, y = t.pos()
            draw_hexagon(x, y, side_len, colorsInUse[colorsCount % 2])
            t.right(120)
            t.forward(shortDiagonal)
            t.seth(0)
        t.left(60)
        t.forward(shortDiagonal * N)
        t.seth(0)
        t.forward(shortDiagonal)
        colorsCount += 1
    for i in range(N // 2):
        for j in range(N - i * 2):
            x, y = t.pos()
            draw_hexagon(x, y, side_len, colorsInUse[colorsCount % 2])
            t.right(120)
            t.forward(shortDiagonal)
            t.seth(0)
        t.left(60)
        t.forward(shortDiagonal * (N - 2 - (i * 2)))
        t.seth(0)
        t.forward(shortDiagonal)
        colorsCount += 1
    if (N % 2 == 1):
        x, y = t.pos()
        draw_hexagon(x, y, side_len, colorsInUse[colorsCount % 2])


drawAll(get_num_hexagons(),get_color_choice(),get_color_choice())

t.up()
t.home()
t.hideturtle()
turtle.done()
