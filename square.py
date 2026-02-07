import turtle

turtle.Screen().bgcolor("Yellow")
turtle.Screen().setup(500,600)
square=turtle.Turtle()

num_sides=4
side_len=88
angle=360.0/num_sides

for i in range(4):
     square.forward(side_len)  # Move forward
     square.right(90)    
