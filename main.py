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
global posintrepeat
posintrepeat = abs(intrepeat)
turtle.speed(100)
returnmeaurement = 0.5
def circle():
    turtle.penup()
    turtle.forward(lg - 1)
    turtle.pendown()
    turtle.forward(1)
    turtle.penup()
    turtle.right(180)
    turtle.forward(lg)
    returnangle = 179.5
    turtle.left(returnangle)
    print (returnangle)
    print (turtle.speed)

returnangle = 179.5
def makeit():
    for i in range(posintrepeat):
        circle()
        print(returnmeasurment)
print(abs(intrepeat))
makeit()





turtle.exitonclick()