import turtle

# This is Global setup
turtle.title("Rosetta")
turtle.bgcolor("black")
turtle.setup(600,600)
turtle.shape("turtle")
# end of Global setup

screen = turtle.Screen()

def draw_square(some_turtle):
  some_turtle.forward(200)
  some_turtle.right(90)

def draw_shapes():
  mimpha = turtle.Turtle(shape= "turtle")
  mimpha.color("purple")
  mimpha.pensize(2)
  mimpha.speed(4)

  for _ in range(36):
    draw_square(mimpha)
    mimpha.right(10)

  revali = turtle.Turtle(shape = "turtle")
  revali.goto(150,150)
  revali.color("green")
  revali.pensize(2)
  revali.speed(7)
  

  size = 1

  for _ in range(300):
    revali.forward(size)
    revali.right(93)
    size += 1

screen.onkey(draw_shapes,"r")
screen.listen()

turtle.done()

