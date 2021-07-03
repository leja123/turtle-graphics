import turtle

turtle1 = turtle.Turtle()
turtle1.color('violet')
turtle1.pensize(10)
turtle1.shape('turtle')

turtle1.circle(100)

turtle2 = turtle.Turtle()
turtle2.color('blue')
turtle2.pensize(10)
turtle2.shape('turtle')

turtle2.forward(200)
turtle2.right(90)
turtle2.forward(200)
turtle2.left(90)
turtle2.backward(200)
turtle2.left(90)
turtle2.forward(200)
turtle2.right(90)

turtle3 = turtle.Turtle()
turtle3.color('green')
turtle3.pensize(10)
turtle3.shape('turtle')

for x in range(4):
    turtle3.backward(100)
    turtle3.left(90)
 



