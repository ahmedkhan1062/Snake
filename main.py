import random
import score, time
from turtle import Turtle, Screen

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake")
sc.tracer(0)


with open("historay.txt") as file:
     hs = file.read()

points = score.Score(int(hs))

score = Turtle()
score.speed(0)
score.hideturtle()
score.penup()
score.goto(0, 270)
score.width(100)
score.speed(0)
score.color("white")
score.write("Score: 0     Highscore: 0", align="center", font=("Comic Sans",
                                    20, "normal"))

food = Turtle()
food.penup()
food.shape("circle")
food.color("yellow")
food.shapesize(0.5)
food.goto(20 * random.randint(-14, 14), 20 * random.randint(-14, 14))
food.speed(0)


snake = Turtle()
snake.speed(0)
snake.shape("square")
snake.color("red")
snake.penup()

snake1 = Turtle()
snake1.speed(0)
snake1.penup()
snake1.shape("square")
snake1.color("lightgreen")
snake1.setx(-20)


snake2 = Turtle()
snake2.speed(0)
snake2.penup()
snake2.shape("square")
snake2.color("lightgreen")
snake2.setx(-40)

lose = Turtle()
lose.speed(0)
lose.hideturtle()
lose.penup()
lose.width(100)
lose.speed(0)
lose.color("white")

blocks = [snake1, snake2]

def goUp():

    snake.setheading(90)

def goRight():

    snake.setheading(0)

def goLeft():

    snake.setheading(180)

def goDown():

    snake.setheading(270)

def restart():
     
     with open("historay.txt", mode = "w") as file:
         file.write(points.getHighScore())
     points.reset()
     global blocks
     for block in blocks[2:]:
          block.hideturtle()
          block.clear()
     blocks = [snake1, snake2]
     snake.goto(0,0)

def moveBody(headPosition):

    for i in blocks:
        newHead = i.pos()
        i.goto(headPosition)
        headPosition = newHead
        if (round(int(snake.pos()[0]) / 10) * 10 == int(i.pos()[0])) and (
                round(int(snake.pos()[1]) / 10) * 10 == int(i.pos()[1])):
                    restart()
                    

    if (round(int(snake.pos()[0]) / 10) * 10 <=-300) or (
            round(int(snake.pos()[0]) / 10) * 10 >= 300)or (
            round(int(snake.pos()[1]) / 10) * 10 <= -300)or (
            round(int(snake.pos()[1]) / 10) * 10 >= 300):
                restart()

    if (round(int(snake.pos()[0]) / 10) * 10 == int(food.pos()[0])) and (
            round(int(snake.pos()[1]) / 10) * 10 == int(food.pos()[1])):
        eat(headPosition)

def eat(last):

    nblock = Turtle()
    nblock.speed(0)
    nblock.penup()
    nblock.color("lightgreen")
    nblock.shape("square")
    nblock.goto(last)

    blocks.append(nblock)

    points.scoreUp()

    score.clear()
    score.write("Score: "+points.getScore()+"     Highscore: "+points.getHighScore(), align="center", font=("Comic Sans",
                                                  20, "normal"))

    food.goto(20 * random.randint(-14, 14), 20 * random.randint(-14, 14))

def playGame():
    while points.getStatus():
        sc.update()
        sc.listen()
        sc.onkey(key= "w", fun=goUp)
        sc.onkey(key= "d", fun=goRight)
        sc.onkey(key= "a", fun=goLeft)
        sc.onkey(key= "s", fun=goDown)
        head = snake.pos()
        snake.forward(20)

        moveBody(head)
        score.clear()
        score.write("Score: "+points.getScore()+"     Highscore: "+points.getHighScore(), align="center", font=("Comic Sans",
                                                  20, "normal"))
        time.sleep(0.1)

playGame()

sc.exitonclick()

