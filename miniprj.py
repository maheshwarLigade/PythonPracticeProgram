import turtle

window = turtle.Screen()
window.bgcolor("white")
#
artArrow =turtle.Turtle()
artArrow.shape("arrow")
artArrow.color("black")
artArrow.speed(6)
#
# #for alphabet R
# abc.pu()
# abc.setpos(-50,0)
# abc.pd()
# abc.left(90)
# abc.forward(100)
# abc.right(90)
# abc.seth(0)
# abc.circle(50,180)
# abc.left(90)
# abc.forward(100)
# abc.setpos(0,0)
#
# #for alphabet A
# abc.pu()
# abc.setpos(10,0)
# abc.pd()
# abc.seth(0)
# abc.left(75)
# abc.forward(200)
# abc.right(150)
# abc.forward(200)
# x = abc.xcor()
# print(x)
# abc.right(180)
# abc.forward(80)
# abc.seth(180)
# abc.forward(62)
#
# #for alphabet M
# abc.pu()
# abc.setpos(x+10,0)
# abc.pd()
# abc.seth(90)
# abc.forward(200)
# abc.right(165)
# abc.forward(150)
# abc.left(150)
# abc.forward(150)
# abc.seth(270)
# abc.forward(200)
#
#
# # code for flower design
artArrow.shape("classic")
artArrow.color("blue")
artArrow.speed(10)

artArrow.pu()
artArrow.setpos(-200,0)
artArrow.pd()

for i in range(1,37):
    artArrow.left(35)
    artArrow.forward(50)
    artArrow.right(35)
    artArrow.forward(50)
    artArrow.right(145)
    artArrow.forward(50)
    artArrow.right(35)
    artArrow.forward(50)
    artArrow.right(10)
artArrow.seth(270)
artArrow.forward(200)

# def draw_triangle():
triang = turtle.Turtle()

triang.forward(300)
triang.left(120)
triang.forward(300)
triang.left(120)
triang.forward(300)

triang.left(120)
triang.forward(20)
triang.left(120)
triang.forward(20)
triang.right(180)
triang.forward(20)
triang.left(120)


window.exitonclick()

# import turtle
# #Haha TTpro
# def draw_triangle(the_turtle,length,ori,recursion):
#     recursion=recursion+1
#     meow= the_turtle
#
#     for i in range(0,3):
#         if(recursion<4):
#         #if (0):
#             meow.forward(length/2)
#             meow.left(120)
#             draw_triangle(meow,length/2,0,recursion)
#             meow.right(120)
#             meow.forward(length/2)
#         else:
#             meow.forward(length)
#         if (ori==1):
#             meow.left(120)
#         else:
#             meow.right(120)
#
# meow = turtle.Turtle() # init
# meow.speed(5) # speed = 1 to slow turtle down
# meow.color("black","blue") # set color5
# meow.shape("turtle") # set shape to a turtle
# background = turtle.Screen()  # create background
# background.bgcolor("white")     # set background color to red
#
#
# draw_triangle(meow,200,1,0)

#meow.forward(100)
#meow.left(120)
#draw_triangle(meow,100,0,0)
#meow.right(120)

# background.exitonclick()      # click anywhere to close background
