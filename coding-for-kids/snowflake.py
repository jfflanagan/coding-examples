# Comes from the book:
# The Recursive Book of Recursion: Ace the Coding Interview with Python and JavaScript
import turtle
turtle.tracer(10, 0)
turtle.setworldcoordinates(0,0,700,700)
turtle.hideturtle()
turtle.pensize(2)

def drawKochCurve(startPosition, heading, length):
    if length < 1:
        return
    else:
        recursiveArgs = []
        turtle.penup()
        turtle.goto(startPosition)
        turtle.setheading(heading)
        recursiveArgs.append({'position':turtle.position(),
                              'heading':turtle.heading()})
        
        #erase midel third
        turtle.forward(length / 3)
        turtle.pencolor('white')
        turtle.pendown()
        turtle.forward(length / 3)

        #draw bump
        turtle.backward(length / 3)
        turtle.left(60)
        recursiveArgs.append({'position':turtle.position(),
                              'heading':turtle.heading()})
        turtle.pencolor('black')
        turtle.forward(length / 3)
        turtle.right(120)
        recursiveArgs.append({'position':turtle.position(),
                              'heading':turtle.heading()})
        turtle.forward(length / 3)
        turtle.left(60)
        recursiveArgs.append({'position':turtle.position(),
                              'heading':turtle.heading()})

        for i in range(4):
            drawKochCurve(recursiveArgs[i]['position'],
                          recursiveArgs[i]['heading'],
                          length / 3) 

        return

def drawKOchSnowFlake(startPosition, heading, length):
    turtle.penup()
    turtle.goto(startPosition)
    turtle.setheading(heading)

    for i in range(3):
        curveStartingPosition = turtle.position()
        curveStartingHeading = turtle.heading()
        drawKochCurve(curveStartingPosition, 
                      curveStartingHeading, length)

        turtle.penup()
        turtle.goto(curveStartingPosition)
        turtle.setheading(curveStartingHeading)

        turtle.forward(length)
        turtle.right(120)

drawKOchSnowFlake((100,500), 0, 500)
turtle.exitonclick()   

