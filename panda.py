import turtle
pen = turtle.Turtle()
def ring(col, rad):
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
pen.speed(4)

pen.up()
pen.setpos(-35, 95)
pen.down
ring('black', 15)

pen.up()
pen.setpos(35, 95)
pen.down()
ring('black', 15)

pen.up()
pen.setpos(0, 35)
pen.down()
ring('white', 40)

pen.up()
pen.setpos(-18, 75)
pen.down()
ring('black', 8)

pen.up()
pen.setpos(18, 75)
pen.down()
ring('black', 8)

pen.up()
pen.setpos(-18, 77)
pen.down()
ring('white', 4)

pen.up()
pen.setpos(18, 77)
pen.down()
ring('white', 4)

pen.up()
pen.setpos(0, 55)
pen.down()
ring('black', 5)

pen.up()
pen.setpos(0, 55)
pen.down()
pen.right(90)
pen.circle(5, 180)
pen.up()
pen.setpos(0, 55)
pen.down()
pen.left(360)
pen.circle(5, -180)

pen.up()
pen.setpos(-80, -45)
pen.down()
ring('white', 80)

pen.up()
pen.setpos(-40, -40)
pen.down()
ring('black', 40)

pen.up()
pen.setpos(-120, -100)
pen.down()
ring('black', 30)

pen.up()
pen.setpos(-95, 20)
pen.down()
ring('black', 20)

pen.up()
pen.setpos(55, 20)
pen.down()
ring('black', 20)

pen.up()
pen.setpos(55, -100)
pen.down()
ring('black', 30)

pen.hideturtle()