# Comes from the book:
# The Recursive Book of Recursion: Ace the Coding Interview with Python and JavaScript
import random
import time
import turtle
turtle.tracer(1000,0)
turtle.setworldcoordinates(0, 0, 700,700)
turtle.hideturtle()

def drawBranch(startPosition, direction, branchLength):
    if branchLength < 5:
        return
    
    # stasrting point
    turtle.penup()
    turtle.goto(startPosition)
    turtle.setheading(direction)

    #draw banch
    turtle.pendown()
    turtle.pensize(max(branchLength / 7.0, 1))
    turtle.forward(branchLength)

    # recond position of branch end
    endPosition = turtle.position()
    leftDirection = direction +  random.randint(10, 30) #LEFT_ANGLE
    leftBranchLength = branchLength - random.randint(8,15) #LEFT_DECREASE
    rightDirection = direction - random.randint(10, 30) #RIGHT_ANGLE
    rightBranchLength = branchLength - random.randint(8, 15)#RIGHT_DECREASE

    #recurse
    drawBranch(endPosition, leftDirection, leftBranchLength)
    drawBranch(endPosition, rightDirection, rightBranchLength)

seed = 0
while True:
    random.seed(seed)
    #LEFT_ANGLE = random.randint(10, 30)
    #LEFT_DECREASE = random.randint(8,15)
    #RIGHT_ANGLE = random.randint(10, 30)
    #RIGHT_DECREASE = random.randint(8, 15)
    START_LENGTH = random.randint(70, 110)

    #wrirwe seed
    turtle.clear()
    turtle.penup()
    turtle.goto(10,10)
    turtle.write('Seed %s' % (seed))

    # Draw tree
    drawBranch((350, 10), 90, START_LENGTH)
    turtle.update()
    time.sleep(2)

    seed += 1
