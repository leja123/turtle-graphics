import turtle

turtle.bgcolor('black')
turtle.title('House')
t = turtle.Turtle()
t.pensize(5)
t.shape('circle')

t.penup
t.left(270)
t.forward(300)
t.right(90)
t.forward(100)
t.left(180)

for x in range(4):
    t.color('yellow')
    t.forward(250)
    t.left(90)

t.penup
t.left(90)
t.forward(250)

for x in range(2):
    t.color('red')
    t.right(30)
    t.forward(250)
    t.right(90)
