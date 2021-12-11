#import libraries
import turtle
import random
#global variables
counter1=0
counter2=0
counter3=0
#other
turtle.colormode(255)
turtle.ht()
#main program
num=random.randint(5,15)
#background
#neeeeeeoooooowwwwww speeeeeeed
turtle.speed(1000000000000000000000000000000000000000000000000000000000000000000000000000000000)
#background
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
turtle.pencolor(r,g,b)
r1=random.randint(0,255)
g1=random.randint(0,255)
b1=random.randint(0,255)
turtle.fillcolor(r1,g1,b1)
turtle.penup()
turtle.goto(-500,500)
turtle.pendown()
turtle.begin_fill()
turtle.forward(1000)
turtle.right(90)
turtle.forward(1000)
turtle.right(90)
turtle.forward(1000)
turtle.right(90)
turtle.forward(1000)
turtle.right(90)
turtle.end_fill()
for counter3 in range(0,200):
    turtle.pensize(random.randint(3,10))
    turtle.setx(random.randint(-500,500))
    turtle.sety(random.randint(-500,500))
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    turtle.pencolor(r,g,b)
#shape maker
for counter1 in range(0,num):
    turtle.pensize(random.randint(1,5))
    #size decider
    length=random.randint(60,200)
    #angle decider
    angle=random.randint(45,89)
    #side amount decider
    amount=random.randint(50,100)
    #color decider
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    turtle.pencolor(r,g,b)
    r1=random.randint(0,255)
    g1=random.randint(0,255)
    b1=random.randint(0,255)
    turtle.fillcolor(r1,g1,b1)
    #position decider
    turtle.penup()
    turtle.setx(random.randint(-200,200))
    turtle.sety(random.randint(-200,200))
    turtle.pendown()
    #shape drawer
    turtle.begin_fill()
    for counter2 in range(0,amount):
        turtle.fd(length)
        turtle.right(angle)
    turtle.end_fill()
#signature
turtle.penup()
turtle.goto(-450,-450)
turtle.pencolor(0,0,0)
turtle.pendown
turtle.write("made by rng and an idiot with too much time on their hands")
input()
