
import turtle

# Create the drawing screen
screen = turtle.Screen()
screen.title("Turtle Pattern Generator")
screen.setup(width=800, height=700)
screen.bgcolor("black")

# Create the drawing pen
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

# Custom colors
colors = ["cyan", "magenta", "yellow", "lime"]

# Recursive function to draw Koch curve
def koch_curve(length, depth):
    if depth == 0:
        pen.forward(length)
    else:
        koch_curve(length / 3, depth - 1)
        pen.left(60)

        koch_curve(length / 3, depth - 1)
        pen.right(120)

        koch_curve(length / 3, depth - 1)
        pen.left(60)

        koch_curve(length / 3, depth - 1)


# Draw the Koch snowflake
depth = int(screen.textinput("Fractal Depth", "Enter depth (0 to 4): "))
depth = max(0, min(depth, 4))

pen.penup()
pen.goto(-200, 120)
pen.pendown()

pen.color(colors[depth % len(colors)])

for _ in range(3):
    koch_curve(400, depth)
    pen.right(120)

# Keep the window open
screen.mainloop()
