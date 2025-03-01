#Martha Moreno Gonzalez
#02/28/2025
#Problem 5: replicate image 
 
import turtle 
def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

size = 50
space = 50
initial_pos = (0, 0)

alex.penup() 
alex.goto(initial_pos)  
alex.pendown()  
for _ in range (10):
    alex.penup()
    alex.goto(initial_pos[0] - (size / 2), initial_pos[1] - (size / 2)) 
    alex.pendown()
    drawSquare(alex, size)
    
    size += 20

wn.exitonclick() 