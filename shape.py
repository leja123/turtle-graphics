import turtle

turtle.bgcolor('black')
turtle.pensize(1)
turtle.speed(0)

for x in range(10):
    for colors in ['magenta', 'cyan', 'violet', 'blue']:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)

turtle.clear()     

for x in range(10):
    for colors in ['yellow', 'red', 'orange', 'white']:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)

turtle.clear()     

for x in range(10):
    for colors in ['green', 'lightgreen', 'blue', 'lightblue']:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)


