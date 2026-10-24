import turtle
from random import randint
import time

screen_board = turtle.Screen()
screen_board.bgcolor("light blue")
screen_board.title("Catch the Snake")
screen_board.register_shape("snake2.gif")

snake_instance = turtle.Turtle()
write_instance = turtle.Turtle()
write_instance.hideturtle()

snake_instance.penup()
snake_instance.shapesize(2, 3, 1)
snake_instance.shape("snake2.gif")
timer = 20

while(True):
    write_instance.write(f"Time Left: {timer}", move=False, align='right', font=('Arial', 16, 'bold'))
    snake_instance.hideturtle()
    snake_instance.setx(randint(-370,370))
    snake_instance.sety(randint(-370,370))
    snake_instance.showturtle()
    time.sleep(1)
    timer -= 1
    write_instance.reset()
    write_instance.hideturtle()

screen_board.mainloop()