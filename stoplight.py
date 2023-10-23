import turtle
wn = turtle.Screen()
wn.title("Prototype for ENGR 408")
wn.bgcolor("black")

#Draw box around the stoplight
pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

#Red light
redLight = turtle.Turtle()
redLight.shape("circle")
redLight.color("grey")
redLight.penup()
redLight.goto(0, 40)

#Yellow light
yellowLight = turtle.Turtle()
yellowLight.shape("circle")
yellowLight.color("grey")
yellowLight.penup()
yellowLight.goto(0, 0)

#Green light
greenLight = turtle.Turtle()
greenLight.shape("circle")
greenLight.color("grey")
greenLight.penup()
greenLight.goto(0, -40)


def activateRed():
    redLight.color("red")
    yellowLight.color("grey")
    greenLight.color("grey")

def activateYellow():
    redLight.color("grey")
    yellowLight.color("yellow")
    greenLight.color("grey")

def activateGreen():
    redLight.color("grey")
    yellowLight.color("grey")
    greenLight.color("green")

activateRed()
activateGreen()
activateYellow()

wn.mainloop()