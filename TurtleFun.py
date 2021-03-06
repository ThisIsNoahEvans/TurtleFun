###These demos are from the Teach-ICT.com lessons on Turtle.###

#Watch the console to see what the turtle is about to do...#

import turtle
import time
import random
print('Imported')

win=turtle.Screen()
print('Launched program')

print('Drawing line...')
turtle.forward(100)
turtle.reset()
print('Drawing square...')
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
print('Making error to undo....')
turtle.forward(100)
print('Undoing...')
turtle.undo()
print('Clearing screen to draw square backwards...')
turtle.clear()
print('Drawing square backwards...')
turtle.bk(200)
turtle.lt(90)
turtle.bk(300)
turtle.lt(90)
turtle.bk(200)
turtle.lt(90)
turtle.bk(300)
print('Changing turtle shape...')
turtle.shape('turtle')
time.sleep(1)
turtle.shape('triangle')
time.sleep(1)
turtle.shape('square')
time.sleep(1)
turtle.shape('arrow')
time.sleep(1)
print('Changing name of turtle...')
noah = turtle.Turtle()
print('Clearing screen...')
noah.reset()
print('Drawing square...')
noah.fd(100)
noah.lt(90)
noah.fd(100)
noah.lt(90)
noah.fd(100)
noah.lt(90)
noah.fd(100)
print('Clearing screen...')
turtle.reset()
noah.reset()
print('Drawing circle...')
noah.circle(50)
print('Clearing screen...')
noah.reset()
print('coloring background...')
win.bgcolor('darkorchid')
print('Changing line color...')
noah.color('aqua')
print('Drawing line...')
noah.forward(100)
print('Clearing screen...')
noah.reset()
print('Changing line thickness...')
noah.pensize(3)
print('Drawing circle...')
noah.circle(100)
print('Clearing screen...')
noah.reset()
print('Drawing circle pattern...')
noah.pensize(5)
win.bgcolor('lightgray')
noah.color('violet')
noah.circle(30)
print('Drawn circle 1')
noah.pensize(4)
noah.color('lightblue')
noah.circle(50)
print('Drawn circle 2')
noah.pensize(3)
noah.color('hotpink')
noah.circle(70)
print('Drawn circle 3')
noah.pensize(2)
noah.color('green')
noah.circle(90)
print('Drawn circle 4')
noah.pensize(1)
noah.color('chocolate')
noah.circle(110)
print('Drawn circle 5')
print('Drawing squares and circles...')
noah.reset()
noah.pensize(5)
noah.color('hotpink')
noah.fd(50)
noah.lt(90)
noah.color('lime')
noah.fd(50)
noah.lt(90)
noah.color('orangered')
noah.fd(50)
noah.lt(90)
noah.color('darkcyan')
noah.fd(50)
print('Drawn square 1')
noah.color('gold')
noah.circle(50)
print('Drawn circle 2')
noah.color('black')
noah.fd(30)
noah.color('indigo')
noah.circle(60)
print('Drawn circle 3')
noah.rt(45)
noah.color('navy')
noah.fd(50)
noah.lt(90)
noah.color('maroon')
noah.fd(50)
noah.lt(90)
noah.color('coral')
noah.fd(50)
noah.lt(90)
noah.color('olive')
noah.fd(50)
print('Drawn square 4')
print('Drawing symmetrical pattern...')
noah.reset()
noah.lt(90)
noah.penup()
noah.goto(50, 50)
noah.pendown()
win.bgcolor('indigo')
noah.color('hotpink')
noah.circle(30)
noah.penup()
noah.goto(-50, -50)
noah.pendown()
noah.circle(30)
print('Drawn symmetrical pattern...')
print('Drawing a square using variables...')
win.bgcolor('lightgray')
line = 200
turn = 90
noah.reset()
noah.fd(line)
noah.lt(turn)
noah.fd(line)
noah.lt(turn)
noah.fd(line)
noah.lt(turn)
noah.fd(line)
noah.reset()
print('Drawing a rectangle with variables...')
longLine = 200
shortLine = 100
noah.fd(longLine)
noah.rt(turn)
noah.fd(shortLine)
noah.rt(turn)
noah.fd(longLine)
noah.rt(turn)
noah.fd(shortLine)
noah.reset()
print('Drawing a Square using a for loop...')
line = 250
for x in range(4):
    noah.fd(line)
    noah.rt(turn)
print('Drawing a rectangle using a for loop...')
noah.reset()
longLine = 300
shortLine = 150
for x in range(2):
    noah.fd(shortLine)
    noah.lt(turn)
    noah.fd(longLine)
    noah.lt(turn)
print('Drawing a square using a for loop and a sum...')
noah.reset()
for x in range(4):
    noah.fd(250)
    noah.lt(360/4)
print('Drawing an octagon using a for loop and a sum...')
noah.reset()
for x in range(8):
    noah.fd(100)
    noah.lt(360/8)
print('Drawing a 20 sided shape using a for loop and a sum...')
noah.reset()
for x in range(20):
    noah.fd(100)
    noah.lt(360/20)
print('Drawing a shape pattern...')
noah.pensize(1)
noah.color('lightblue')
noah.reset()
for x in range(4):
    noah.fd(50)
    noah.lt(360/4)
print('Drawn shape 1 - square')
noah.pensize(2)
noah.color('indigo')
for x in range(5):
    noah.fd(70)
    noah.lt(360/5)
print('Drawn shape 2 - pentagon')
noah.pensize(3)
noah.color('lightgreen')
for x in range(6):
    noah.fd(90)
    noah.lt(360/6)
print('Drawn shape 3 - hexagon')
noah.pensize(4)
noah.color('hotpink')
for x in range(7):
    noah.fd(110)
    noah.lt(360/7)
print('Drawn shape 4 - heptagon')
print('Drawing a filled in square...')
noah.reset()
noah.color('blue')
noah.fillcolor('blue')
noah.begin_fill()
for x in range(4):
    noah.fd(250)
    noah.lt(360/4)
noah.end_fill()
time.sleep(1)
noah.reset()
print('Defining turtle 2...')
evans = turtle.Turtle()
print('Drawing two squares...')
noah.color('lightblue')
noah.fillcolor('blue')
evans.color('lightgreen')
evans.fillcolor('green')
noah.begin_fill()
evans.begin_fill()
for x in range(4):
    noah.fd(100)
    evans.fd(50)
    noah.rt(turn)
    evans.lt(turn)
noah.end_fill()
evans.end_fill()
time.sleep(1)
noah.reset()
evans.reset()
print('Drawing eight circles at the same time...')
win.bgcolor('seashell')
anotherTurtle = turtle.Turtle()
extraTurtle = turtle.Turtle()
noah.color('lightblue')
noah.fillcolor('blue')
evans.color('lightgreen')
evans.fillcolor('green')
anotherTurtle.color('lightpink')
anotherTurtle.fillcolor('pink')
extraTurtle.color('peachpuff')
extraTurtle.fillcolor('yellow')
noah.begin_fill()
evans.begin_fill()
anotherTurtle.begin_fill()
extraTurtle.begin_fill()
print('Defined turtles and colours')
for x in range(2):
    noah.circle(100)
    evans.circle(75)
    anotherTurtle.circle(50)
    extraTurtle.circle(25)
    noah.pensize(x + 1)
    evans.pensize(x + 2)
    anotherTurtle.pensize(x + 3)
    extraTurtle.pensize(x + 4)
noah.end_fill()
evans.end_fill()
anotherTurtle.end_fill()
extraTurtle.end_fill()
time.sleep(1)
noah.reset()
evans.reset()
anotherTurtle.reset()
extraTurtle.reset()
print('Drawn eight circles')
print('Drawing square patterns...')
win.bgcolor('lightgray')
noah.color('blue')
for x in range(4):
    noah.fd(50)
    noah.lt(90)
noah.lt(20)
for x in range(4):
    noah.fd(50)
    noah.lt(90)
noah.lt(20)
for x in range(4):
    noah.fd(50)
    noah.lt(90)
noah.lt(20)
for x in range(4):
    noah.fd(50)
    noah.lt(90)
noah.lt(20)
for x in range(4):
    noah.fd(50)
    noah.lt(90)
noah.lt(20)
print('Drawing hexagon patterns...')
win.bgcolor('darkgray')
noah.color('crimson')
for x in range(6):
    noah.fd(50)
    noah.lt(360/6)
noah.lt(20)
for x in range(6):
    noah.fd(50)
    noah.lt(360/6)
noah.lt(20)
for x in range(6):
    noah.fd(50)
    noah.lt(360/6)
noah.lt(20)
for x in range(6):
    noah.fd(50)
    noah.lt(360/6)
noah.lt(20)
for x in range(6):
    noah.fd(50)
    noah.lt(360/6)
noah.lt(20)
noah.reset()
print('Drawing heptatgon patterns...')
for x in range(7):
    noah.fd(50)
    noah.lt(360/7)
noah.lt(45)
for x in range(7):
    noah.fd(50)
    noah.lt(360/7)
noah.lt(45)
for x in range(7):
    noah.fd(50)
    noah.lt(360/7)
noah.lt(45)
for x in range(7):
    noah.fd(50)
    noah.lt(360/7)
noah.lt(45)
for x in range(7):
    noah.fd(50)
    noah.lt(360/7)
noah.lt(45)
noah.reset()
print('Drawing shapes using functions...')
def drawSquare():
    for x in range(4):
        noah.fd(50)
        noah.lt(90)
drawSquare()
print('Drawing a pattern using a function...')
noah.reset()
drawSquare()
noah.lt(10)
drawSquare()
noah.lt(10)
drawSquare()
noah.lt(10)
drawSquare()
noah.lt(10)
drawSquare()
noah.lt(10)
drawSquare()
noah.lt(10)
drawSquare()
noah.lt(10)
drawSquare()
noah.lt(10)
drawSquare()
noah.lt(10)
drawSquare()
noah.lt(10)
drawSquare()
noah.lt(10)
print('Drawing a patttern with multiple functions...')
noah.reset()
def turn10():
    noah.lt(10)
drawSquare()
turn10()
drawSquare()
turn10()
drawSquare()
turn10()
drawSquare()
turn10()
drawSquare()
turn10()
drawSquare()
turn10()
drawSquare()
turn10()
drawSquare()
turn10()
drawSquare()
turn10()
drawSquare()
turn10()
print('Drawing shapes using for loops and functions...')
noah.reset()
for x in range(36):
    drawSquare()
    turn10()
noah.reset()
print('Drawing a pentagon using for loops and functions...')
def drawPentagon():
    for x in range(5):
        noah.fd(50)
        noah.lt(360/5)
drawPentagon()
noah.reset()
print('Drawing a pentagon pattern whilst changing to a random colour on every multple of 4 (every fourth shape)...')
def drawPentagonPattern():
    for x in range(36):
        if x%4==0:
            penColours = ['red', 'deeppink', 'orange', 'gold', 'magenta', 'lime', 'blue', 'brown', 'beige', 'gray']
            randomPenColour = random.choice(penColours)
            noah.pencolor(randomPenColour)
            for x in range(5):
                noah.fd(50)
                noah.lt(360/5)
        else:
            for x in range(5):
                noah.fd(50)
                noah.lt(360/5)
        noah.lt(10)
drawPentagonPattern()
print('Drawing coloured circle patttern where every circle is a randomly chosen colour...')
noah.reset()
def drawCirclePattern():
    for x in range(36):
        penColours = ['red', 'deeppink', 'orange', 'gold', 'magenta', 'lime', 'blue', 'brown', 'beige', 'gray']
        randomPenColour = random.choice(penColours)
        noah.pencolor(randomPenColour)
        noah.circle(50)
        noah.lt(10)
drawCirclePattern()
print('Drawing a dashed line...')
noah.reset()
noah.pencolor('red')
noah.fd(10)
noah.pu()
noah.fd(5)
noah.pd()
noah.fd(10)
noah.pu()
noah.fd(5)
noah.pd()
noah.fd(10)
noah.pu()
noah.fd(5)
noah.pd()
noah.fd(10)
noah.pu()
noah.fd(5)
noah.pd()
noah.fd(10)
noah.pu()
noah.fd(5)
noah.pd()
noah.fd(10)
time.sleep(1)

print('Drawing a dashed line using a for loop...')
noah.reset()
for x in range(10):
    noah.pd()
    noah.fd(10)
    noah.pu()
    noah.fd(5)
noah.reset()
print('Moving the turtle to four corners and drawing a square...')
noah.pu()
noah.goto(300, 300)
noah.pd()
drawSquare()
noah.pu()
noah.goto(-300, 300)
noah.pd()
drawSquare()
noah.pu()
noah.goto(300, -300)
noah.pd()
drawSquare()
noah.pu()
noah.goto(-300, -300)
noah.pd()
drawSquare()
print('Writing "Noah" on the scren...')
noah.pu()
noah.goto(-100,100)
noah.pd()
noah.write('Noah', font=('Tahoma', 24, 'bold'))
time.sleep(5)
print('Program finished!')
