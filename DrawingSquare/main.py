import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Drawing Square")

turtle_instance = turtle.Turtle()

for i in range(4):
    turtle_instance.forward(200)
    turtle_instance.left(90)

turtle.done()