import turtle

turtle.screensize(600, 400, "blue")

linuxidc = turtle.Turtle()

linuxidc.speed(10)

linuxidc.pencolor("red")
for i in range(200):
    linuxidc.forward(150)
    linuxidc.right(30)
    linuxidc.forward(20)
    linuxidc.left(60)
    linuxidc.forward(50)
    linuxidc.right(30)

    linuxidc.penup()
    linuxidc.setposition(0, 0)
    linuxidc.pendown()

    linuxidc.right(2)

turtle.done()