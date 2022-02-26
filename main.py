# trying to play around with the code
# drawing my school logo using python :)
# by Yara ElSakka a.k.a roor or a.k.a TIDDELS :)
# 260222

import turtle as tu             # importing the library or package

Y       = 70                    # how many times the branches will be repeated
r       = 250                   # radius of my circle

tiddels = tu.Turtle()           # Turtle object
window  = tu.Screen()           # Screen Object

window.bgcolor("white")         # Screen Bg color
window.title("my school logo: The International School of Choueifat Ajman")
tiddels.showturtle()            # showing the turtle drawing is fun!

# in position (0,0), writing 1886:
tiddels.color("green")
style = ("arial", 30, "bold")
tiddels.write("1886", font=style, align="center")

# to move to another area of the drawing, we need to use:
# pen-up method
# goto method
# pen-down method

tiddels.penup()
tiddels.goto(0,-25)
tiddels.pendown()

# in position (0,-25), below "1886", writing "The International School of Choueifat":
tiddels.color("green")
style = ("arial", 15, "bold")
tiddels.write("The International School of Choueifat", font=style, align="center")

# to move to another area of the drawing, we need to use penup, goto, pendown methods:
tiddels.penup()
tiddels.goto(0,-60)
tiddels.pendown()

# in position (0,-60), below "The International School of Choueifat", writing "done by Yara":
tiddels.color("deep pink")
style = ("arial", 15, "bold")
tiddels.write("by Yara ElSakka, 25.02.2022 :)", font=style, align="center")

# to move to another area of the drawing, we need to use penup, goto, pendown methods:
tiddels.penup()
tiddels.goto(0,50)
tiddels.pendown()

# drawing the first part of the Tree at (0,50) position:
tiddels.left(90)            # moving the turtle 90 degrees towards left
tiddels.speed(20)           # setting the speed of the turtle

# drawing the branches using the function draw:
def draw(l):                # recursive function taking length 'l' as argument
    if (l < 10):
        return
    else:
        tiddels.pensize(8)          # Setting Pensize
        tiddels.pencolor("green")   # Setting Pencolor as yellow
        tiddels.forward(l)          # moving turtle forward by 'l'
        tiddels.left(30)            # moving the turtle 30 degrees towards left
        draw(3 * l / 4)             # drawing a fractal on the left of the turtle object 'tiddels' with 3/4th of its length
        tiddels.right(60)           # moving the turtle 60 degrees towards right
        draw(3 * l / 4)             # drawing a fractal on the right of the turtle object 'tiddels' with 3/4th of its length
        tiddels.left(30)            # moving the turtle 30 degrees towards left
        tiddels.pensize(2)
        tiddels.backward(l)         # returning the turtle back to its original psition

draw(Y) # drawing the Ys 20 times!

# to move to another area of the drawing, we need to use penup, goto, pendown methods:
tiddels.penup()
tiddels.goto(r,70)
tiddels.pendown()

# drawing a circle around everything at position (r,50), where r = 250
tiddels.circle(r)

# to close the windows once we are done.
window.exitonclick()

# end of code 26.22.22