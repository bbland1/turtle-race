from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Choose", prompt="Enter the color of the turtle you think will win the race: ")

turtles_y = [-50, -25, 0, 25, 50, 75]
turtles_color = ["red", "orange", "yellow", "green", "blue", "purple"]
the_turtles = []

for turtle in range(0, 6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(turtles_color[turtle])
  new_turtle.penup()
  new_turtle.goto(x=-230, y=turtles_y[turtle])
  the_turtles.append(new_turtle)

if user_bet:
  is_on = True

while is_on:
  for turtle in the_turtles:
    if turtle.xcor() > 230:
      is_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"{winning_color} is first you win!")
      else:
        print(f"{winning_color} was first you lose...")
    random_distance = randint(0, 10)
    turtle.forward(random_distance)


screen.exitonclick()
