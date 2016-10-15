import turtle

def draw_anyshape():
    window = turtle.Screen()
    window.bgcolor("red")
    draw_square()
    # draw_circle()
    # draw_triangle()

    window.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
    count = 0
    while count < 50:
      brad.forward(100)
      brad.right(90)
      brad.right(10)
      count = count + 1



def draw_circle():
    angie = turtle.Turtle()

    angie.circle(100)
    angie.color("yellow")
    angie.shape("turtle")


def draw_triangle():
    triang = turtle.Turtle()

    triang.forward(300)
    triang.left(120)
    triang.forward(300)
    triang.left(120)
    triang.forward(300)
    triang.color("yellow")
    triang.shape("turtle")


draw_anyshape()
