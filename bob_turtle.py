import turtle

def drawMyTurtle(tur, sz):
  for i in range(4):
    tur.forward(sz)
    tur.left(90)

#setup window and color
wn = turtle.Screen()
wn.bgcolor('lightgreen')

#create turtle named bob
bob = turtle.Turtle()

#call function
drawMyTurtle(bob,200)


bob.penup()
bob.goto(100,100)
bob.pendown()

drawMyTurtle(bob,75)




wn.exitonclick()

