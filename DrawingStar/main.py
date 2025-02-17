import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Drawing Star")

turtle_instance = turtle.Turtle()

num_sides = 5
angle = 360 / num_sides * 2
side_length = 300

for i in range(5):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)

turtle.done()