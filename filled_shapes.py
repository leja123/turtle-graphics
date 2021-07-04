import turtle

turtle.bgcolor("black")
turtle.title("Filled shapes")
noob = turtle.Turtle()
noob.color('green')
noob.pensize(10)
noob.shape('turtle')

#circle
noob.begin_fill()
noob.circle(100)
noob.end_fill()
noob.clear()

#triangle
noob.begin_fill()
noob.fd(100)
noob.left(120)
noob.fd(100)
noob.left(120)
noob.fd(100)
noob.end_fill()
noob.clear()

#square
noob.begin_fill()
noob.right(60)
noob.forward(200)
noob.right(90)
noob.forward(200)
noob.left(90)
noob.backward(200)
noob.left(90)
noob.forward(200)
noob.right(90)
noob.end_fill()
noob.clear()
