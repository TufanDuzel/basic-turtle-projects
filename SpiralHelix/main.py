import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Spiral Helix")

turtle_instance = turtle.Turtle()
turtle_instance.color("black")
turtle_instance.speed(10)

turtle_colors = ["pink", "purple", "blue", "yellow", "orange", "green"]

for i in range(15):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(15 * i)
    turtle_instance.circle(-15 * i)
    turtle_instance.left(i)

turtle.done()