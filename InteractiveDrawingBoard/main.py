import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Drawing Board")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_turtle_right():
    turtle_instance.right(10)

def rotate_turtle_left():
    turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun = turtle_forward, key = "Up")
drawing_board.onkey(fun = rotate_turtle_right, key = "Right")
drawing_board.onkey(fun = rotate_turtle_left, key = "Left")
drawing_board.onkey(fun = turtle_return_home, key = "space")
drawing_board.onkey(fun = clear_screen, key = "c")

turtle.mainloop()