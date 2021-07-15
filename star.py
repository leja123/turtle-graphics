import turtle

turtle1 = turtle.Turtle()
turtle1.color('violet')
turtle1.pensize(10)
turtle1.shape('turtle')

turtle1.begin_fill()
for x in range(5):
    turtle1.right(144)
    turtle1.forward(300)
turtle1.end_fill()



