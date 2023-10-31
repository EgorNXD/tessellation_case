import turtle
t = turtle.Turtle()

t.speed(0)
t.up()
t.goto(-250, 250)
N = 9

side_len = 29
colorName1 = "orange"
colorName2 = "green"
colorsInUse = [colorName1, colorName2]
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

def drawAll(N,colorName1,colorName2):
    shortDiagonal = 500/N
    side_len = shortDiagonal / (3**(1/2))
    colorsInUse = [colorName1, colorName2]
    colorsCount = 0
    for i in range(N//2):
        for j in range(((i+1)*2)):
            x, y = t.pos()
            draw_hexagon(x, y, side_len, colorsInUse[i%2])
            t.right(120)
            t.forward(shortDiagonal)
            t.seth(0)
        t.left(60)
        t.forward(shortDiagonal*((i+1)*2))
        t.seth(0)
        t.forward(shortDiagonal)
        colorsCount+=1
    if (N % 2 == 1):
        for j in range(((i+1)*2)+1):
            x, y = t.pos()
            draw_hexagon(x, y, side_len, colorsInUse[(i+N%2)%2])
            t.right(120)
            t.forward(shortDiagonal)
            t.seth(0)
        t.left(60)
        t.forward(shortDiagonal * N)
        t.seth(0)
        t.forward(shortDiagonal)
        colorsCount += 1
    for i in range((N//2)-1):
        for j in range(N):
            x, y = t.pos()
            draw_hexagon(x, y, side_len, colorsInUse[colorsCount%2])
            t.right(120)
            t.forward(shortDiagonal)
            t.seth(0)
        t.left(60)
        t.forward(shortDiagonal*N)
        t.seth(0)
        t.forward(shortDiagonal)
        colorsCount+=1
    for i in range(N//2):
        for j in range(N-i*2):
            x, y = t.pos()
            draw_hexagon(x, y, side_len, colorsInUse[colorsCount%2])
            t.right(120)
            t.forward(shortDiagonal)
            t.seth(0)
        t.left(60)
        t.forward(shortDiagonal*(N-2-(i*2)))
        t.seth(0)
        t.forward(shortDiagonal)
        colorsCount+=1
    if (N % 2 == 1):
        x, y = t.pos()
        draw_hexagon(x, y, side_len, colorsInUse[colorsCount%2])
    
def get_color_choice():
    colorsRus = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'фиолетовый']
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    print('Допустимые цвета заливки: \n красный\n оранжевый\n желтый\n зеленый\n голубой\n фиолетовый\n')
    colorName = input('Пожалуйста введите цвет: ')
    while colorName.lower() not in colorsRus:
        print('"', colorName, '"', 'не является верным значением.')
        colorName = input('Введите корректный цвет:')
    return colors[colorsRus.index(colorName)]


g = get_color_choice()
print(type(g))
#drawAll()
turtle.done()
