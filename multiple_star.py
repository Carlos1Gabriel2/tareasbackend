import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(2000)
n = 50
h = 0

for i in range (380):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h = h + 1/n
    t.color(c)
    t.forward(i*5)
    t.left(145)

turtle.done()