import turtle
from random import randint

score = 0
timer = 20
can_click = True
snake_instance = turtle.Turtle()
write_instance = turtle.Turtle()
score_instance = turtle.Turtle()
write_instance.hideturtle()


score_instance.hideturtle()
score_instance.penup()
score_instance.goto(0, 350)
write_instance.penup()
write_instance.goto(-200, 350)

screen_board = turtle.Screen()
screen_board.bgcolor("light blue")
screen_board.title("Catch the Snake")
screen_board.register_shape("snake2.gif")

snake_instance.penup()
snake_instance.shapesize(2, 3, 1)
snake_instance.shape("snake2.gif")

def turtleOnClick(x,y):
    global can_click
    if can_click:
        scoreUpdate()
        can_click = False

def scoreUpdate():
    global score
    score+=1
    score_instance.clear()
    score_instance.write(f"Total Score: {score}", move=False, align='left', font=('Arial', 16, 'bold'))

def snakeShowUp():
    global can_click
    if timer<= 0:
        snake_instance.hideturtle()
        return
    snake_instance.hideturtle()
    snake_instance.setx(randint(-370, 370))
    snake_instance.sety(randint(-370, 370))
    snake_instance.showturtle()
    can_click = True
    if timer > 0:
        screen_board.ontimer(snakeShowUp,800)

def countdown():
  global timer
  global can_click
  if timer > 0:
    write_instance.clear()
    write_instance.write(
        f"Time Left: {timer}",
        move=False,
        align="right",
        font=("Arial", 16, "bold"),
    )
    timer -= 1
    screen_board.ontimer(countdown, 1000)
  else:
    write_instance.clear()
    write_instance.write(
        "Game Over!",
        move=False,
        align="center",
        font=("Arial", 20, "bold"),
    )
    snake_instance.hideturtle()
    can_click = False



snake_instance.onclick(turtleOnClick)
snakeShowUp()
countdown()

screen_board.mainloop()