import turtle


from turtle import speed

global lg
lg = 20
if lg > 150:
        lg = 150
global la
la = lg/179
global returnmeasurment
returnmeasurment = lg * la
global returnangle
returnangle = 179 + returnmeasurment
global trepeat
trepeat = 360/(1-returnmeasurment) + 1   
global num
num = 360/returnmeasurment
global intrepeat
intrepeat = int(trepeat)
turtle.speed(10)
def circle():
    turtle.penup()
    turtle.forward(lg - 1)
    turtle.pendown()
    turtle.forward(1)
    turtle.penup()
    turtle.right(180)
    turtle.forward(lg)
    if returnangle > 180:
        returnangle = 179.5
    turtle.left(returnangle)
    print (returnangle)
    print (turtle.speed)
if returnangle > 180:
    returnangle = 179.5

def makeit():
    for i in range(intrepeat):
        circle()
        print(returnmeasurment)
        print(intrepeat)
turtle.penup()
turtle.right(180)
turtle.forward(lg * 2)
turtle.pendown()



makeit()
turtle.penup()
turtle.right(180)
turtle.forward(lg * 4)
turtle.pendown()
makeit()
turtle.right(180)
turtle.forward(lg)
turtle.pendown()
turtle.forward(lg * 2)





turtle.exitonclick()