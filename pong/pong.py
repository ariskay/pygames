import turtle
import winsound
from paddle import Paddle
from functools import partial

wn = turtle.Screen()
wn.title("Pong by Ariskay")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

paddle_a = Paddle(-350, 0)
paddle_b = Paddle(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))


def paddle_up(paddle):
    y = paddle.ycor()
    y += 20
    paddle.sety(y)


def paddle_down(paddle):
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)


def paddle_hit():
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


wn.listen()
wn.onkeypress(partial(paddle_up, paddle_a), "w")
wn.onkeypress(partial(paddle_down, paddle_a), "s")
wn.onkeypress(partial(paddle_up, paddle_b), "Up")
wn.onkeypress(partial(paddle_down, paddle_b), "Down")

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        paddle_hit()

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        paddle_hit()

    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        paddle_hit()

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        paddle_hit()
