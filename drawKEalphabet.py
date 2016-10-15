import turtle

def draw_alphabet():
  window = turtle.Screen()
  window.bgcolor("red")
  artArrow =turtle.Turtle()
  artArrow.shape("arrow")
  artArrow.color("black")
  artArrow.speed(6)

 # for alphabet K
  artArrow.pu()
  artArrow.setpos(-50,0)
  artArrow.pd()
  artArrow.left(90)
  artArrow.forward(120)
  artArrow.backward(60)
  artArrow.right(130)
  artArrow.forward(80)
  artArrow.backward(80)
  artArrow.seth(0)
  artArrow.left(45)
  artArrow.forward(80)

  #for E
  artArrow.pu()
  artArrow.setpos(100,0)
  artArrow.pd()
  artArrow.seth(0)
  artArrow.left(90)
  artArrow.forward(120)
  artArrow.right(90)
  artArrow.forward(60)
  artArrow.backward(60)
  artArrow.left(90)
  artArrow.backward(120)
  artArrow.right(90)
  artArrow.forward(60)
  window.exitonclick()


draw_alphabet()
