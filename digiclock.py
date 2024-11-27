import time
import datetime as dt
import turtle


# Create a turtle to display time
t = turtle.Turtle()

# Create a turtle to create rectangle box
t1 = turtle.Turtle()

# Create screen
s = turtle.Screen()

# Set background color of the screen to glossy crimson red
s.bgcolor("crimson")

# Obtain current hour, minute, and second from the system
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour

# Configure the rectangle box
t1.pensize(3)
t1.color('black')
t1.penup()

# Set the position of turtle to draw the rectangle
t1.goto(-10, 7)  # Adjust position for a centered box
t1.pendown()

# Create rectangular box
for i in range(2):
    t1.forward(240)  # Adjust box width
    t1.left(90)
    t1.forward(100)  # Adjust box height
    t1.left(90)

# Hide the turtle
t1.hideturtle()

# Configure the display turtle
t.hideturtle()
t.color("black")
t.penup()
t.goto(0, 10)  # Position the text within the box (inside the box)

# Main loop to update the clock
while True:
    t.clear()
    # Display the time inside the box
    t.write(str(hr).zfill(2)
            + ":" + str(min).zfill(2) + ":"
            + str(sec).zfill(2),
            font=("Arial Narrow", 35, "bold"))
    time.sleep(1)
    sec += 1

    if sec == 60:
        sec = 0
        min += 1

    if min == 60:
        min = 0
        hr += 1

    if hr == 13:
        hr = 1
