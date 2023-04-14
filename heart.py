import turtle

t = turtle.Turtle()
turtle.title("for my ali")

screen=turtle.Screen()
screen.bgcolor("black")

# Drawing heart
t.color("red")
t.fillcolor("red")
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)

t.end_fill()

# Writing text
t.up()
t.setpos(-80,150)
t.down()
t.color("white")
t.write("I LOVE YOU", font=("Verdana", 20, "bold"))
t.up()
t.setpos(-95,125)
t.down()
t.write("ngiti ka please hfsdhfsdh", font=("Verdana", 12))

t.ht()

turtle.mainloop()