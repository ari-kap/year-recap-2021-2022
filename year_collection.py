P_COL = "blue"

WIN_W = 1500
WIN_H = 1000
CLICKED = False
LEVEL = 1


def draw_something():
    import turtle
    import os

    # setup

    bgcol = (240, 241, 243)
    linecol = (0, 75, 75)
    fillcol = (230, 235, 235)
    circcol = (255, 225, 225)
    edgecol = (255, 180, 206)
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(bgcol)
    t = turtle.Turtle()

    t.speed(100)
    t.color(linecol)
    t.pensize(5)

    t.up()

    wn.addshape("draw/bg_gif.gif")
    t.shape(os.path.expanduser("draw/bg_gif.gif"))
    t.goto(-50, 0)
    t.stamp()

    wn.addshape(os.path.expanduser("draw/NEUTRA.gif"))
    t.shape(os.path.expanduser("draw/NEUTRA.gif"))
    t.goto(-250, 150)
    t.stamp()
    t.goto(0, -100)

    t.shape("classic")

    # head circle
    t.down()
    t.fillcolor(fillcol)
    t.begin_fill()
    for i in range(180):
        t.forward(3.2)
        t.left(2)
    t.end_fill()
    for i in range(50):
        t.forward(3.2)
        t.left(2)

    # 2nd part of blade(e)
    t.right(80)
    t.begin_fill()

    t.forward(35)
    for i in range(20):
        t.forward(4)
        t.right(3)
    for i in range(25):
        t.forward(5)
        t.right(1.4)

    t.left(130)
    for i in range(60):
        t.forward(8)
        t.left(0.8)

    # inner blade
    t.left(150)
    for i in range(50):
        t.forward(6)
        t.right(0.5)
    t.right(80)
    for i in range(5):
        t.right(2)
        t.forward(30 - (5 * (i + 1)))
    t.forward(200)
    t.left(175)
    t.forward(200)
    for i in range(5):
        t.right(2)
        t.forward((i + 1) * 5)
    t.right(100)
    for i in range(8):
        t.forward(14)
        t.right(1.5)

    t.end_fill()
    t.left(110)
    for i in range(30):
        t.forward(3.2)
        t.right(2)

    # handle
    t.up()
    t.right(100)
    t.forward(185)
    t.down()
    t.begin_fill()
    t.forward(500)
    t.left(90)
    t.forward(5)
    t.pensize(2)
    t.right(90)
    for i in range(30):
        t.forward(1)
        t.right(2)
    t.left(180)
    for i in range(30):
        t.forward(1)
        t.left(2)

    t.pensize(5)

    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(500)
    t.end_fill()

    # ball thing
    t.up()
    t.left(178)
    t.forward(525)
    t.fillcolor(circcol)
    t.color(edgecol)
    t.shape("circle")
    t.stamp()
    t.forward(-528)
    t.shape("classic")
    t.color(linecol)
    t.fillcolor(fillcol)
    t.down()

    t.left(90)
    for i in range(55):
        t.forward(3.2)
        t.left(2)
    t.right(80)
    # final under
    t.forward(5)
    t.down()
    t.begin_fill()
    for i in range(8):
        t.forward(14)
        t.right(1.5)
    t.right(80)
    for i in range(5):
        t.right(2)
        t.forward(30 - (5 * (i + 1)))
    t.forward(200)
    t.left(175)
    t.forward(200)
    for i in range(5):
        t.right(2)
        t.forward((i + 1) * 5)
    t.right(100)
    for i in range(50):
        t.forward(6)
        t.right(0.5)

    t.left(150)

    # first line
    for i in range(60):
        t.forward(8)
        t.left(0.8)

    t.left(130)
    # curve into head
    for i in range(25):
        t.forward(5)
        t.right(1.2)
    for i in range(20):
        t.forward(4)
        t.right(3)
    t.forward(70)

    t.end_fill()

    t.left(105)
    for i in range(15):
        t.forward(3.2)
        t.right(2)

    t.up()

    wn.addshape(os.path.expanduser("draw/pls_work.gif"))
    t.shape(os.path.expanduser("draw/pls_work.gif"))
    t.goto(-50, 5)
    t.stamp()
    t.goto(400, -500)

    t.shape("classic")

    t.setheading(90)

    t.down()

    for i in [1000, 900, 1000, 900]:
        t.forward(i)
        t.left(90)

    wn.exitonclick()


def turtle_race():
    import turtle
    import random
    import os

    # setup
    wn = turtle.Screen()
    wn.bgcolor("ghostwhite")

    text = turtle.Turtle()
    text.hideturtle()

    wn.addshape(os.path.expanduser("turtle/racing_w2.gif"))
    images = turtle.Turtle()
    images.shape(os.path.expanduser("turtle/racing_w2.gif"))
    images.speed(100)
    images.goto(0, 50)

    images.stamp()
    images.shape("classic")
    images.up()
    images.color("salmon")
    images.hideturtle()

    clicked = False

    wn.onclick(images.goto)

    while images.xcor() == 0:
        images.forward(10)
        images.forward(-10)

    images.clear()

    a = turtle.Turtle()
    b = turtle.Turtle()
    c = turtle.Turtle()
    d = turtle.Turtle()
    e = turtle.Turtle()
    f = turtle.Turtle()
    g = turtle.Turtle()
    h = turtle.Turtle()

    myman = turtle.Turtle()
    # placement

    text.up()
    myman.up()
    dummy = 400
    myman.speed(10)
    myman.shape("square")
    myman.goto(-400, 440)
    myman.right(90)
    for u in range(2):
        for i in (90, 270, 90):
            for p in range(20):
                myman.stamp()
                myman.forward(40)
            myman.left(i)
            myman.forward(20)
            myman.left(i)
            myman.forward(20)
        myman.goto(400, 440)
        myman.left(180)

    for i in [a, b, c, d, e, f, g, h]:
        i.speed(10)
        i.up()
        i.shape("turtle")
        i.goto(-500, dummy)
        i.down()
        dummy = dummy - 100
        i.pensize(5)
        i.shapesize(5)
        i.speed(3)

    a.color("salmon")
    b.color("navajowhite")
    c.color("yellow")
    d.color("palegreen")
    e.color("paleturquoise")
    f.color("slateblue")
    g.color("plum")

    # countdown
    text.write("3", False, "center", ("times", 75, "normal"))
    text.speed(1)
    text.forward(50)
    text.forward(-50)
    text.clear()
    text.write("2", False, "center", ("times", 100, "normal"))
    text.forward(75)
    text.forward(-75)
    text.clear()
    text.write("1", False, "center", ("times", 125, "normal"))
    text.forward(100)
    text.forward(-100)
    text.clear()
    text.write("GO!", False, "center", ("times", 125, "normal"))
    text.forward(50)
    text.forward(-50)
    text.clear()

    # the race :o
    winstate = False

    # idk if necessary, makes global
    movingt = a

    while True:
        movingt = random.choice([a, b, c, d, e, f, g, h])
        movingt.forward(random.randrange(10, 40))
        if movingt.xcor() > 500:
            break

    winnername = "global"
    wincol = "global"

    if movingt == a:
        winnername = "red won!"
        wincol = "salmon"
    elif movingt == b:
        winnername = "orange won!"
        wincol = "navajowhite"
    elif movingt == c:
        winnername = "yellow won!"
        wincol = "yellow"
    elif movingt == d:
        winnername = "green won!"
        wincol = "palegreen"
    elif movingt == e:
        winnername = "turquoise won!"
        wincol = "paleturquoise"
    elif movingt == f:
        winnername = "blue won!"
        wincol = "slateblue"
    elif movingt == g:
        winnername = "pink won!"
        wincol = "plum"
    elif movingt == h:
        winnername = "black won!"
        wincol = "black"
    fcol = wincol

    text.color(wincol)
    text.write(winnername, False, "center", ("times", 75, "normal"))
    print(winnername)
    fplace = winnername

    movingt.speed(100)
    movingt.up()
    movingt.stamp()
    movingt.color("ghostwhite")
    movingt.forward(110)

    while True:
        movingt = random.choice([a, b, c, d, e, f, g, h])
        movingt.forward(random.randrange(10, 40))
        if 600 > movingt.xcor() > 500:
            break

    if movingt == a:
        winnername = "red is second"
        wincol = "salmon"
    elif movingt == b:
        winnername = "orange is second"
        wincol = "navajowhite"
    elif movingt == c:
        winnername = "yellow is second"
        wincol = "yellow"
    elif movingt == d:
        winnername = "green is second"
        wincol = "palegreen"
    elif movingt == e:
        winnername = "turquoise is second"
        wincol = "paleturquoise"
    elif movingt == f:
        winnername = "blue is second"
        wincol = "slateblue"
    elif movingt == g:
        winnername = "pink is second"
        wincol = "plum"
    elif movingt == h:
        winnername = "black is second"
        wincol = "black"
    scol = wincol

    print(winnername)
    splace = winnername
    movingt.speed(100)
    movingt.up()
    movingt.stamp()
    movingt.color("ghostwhite")
    movingt.forward(110)

    while True:
        movingt = random.choice([a, b, c, d, e, f, g, h])
        movingt.forward(random.randrange(10, 40))
        if 600 > movingt.xcor() > 500:
            break

    if movingt == a:
        winnername = "red is third"
        wincol = "salmon"
    elif movingt == b:
        winnername = "orange is third"
        wincol = "navajowhite"
    elif movingt == c:
        winnername = "yellow is third"
        wincol = "yellow"
    elif movingt == d:
        winnername = "green is third"
        wincol = "palegreen"
    elif movingt == e:
        winnername = "turquoise is third"
        wincol = "paleturquoise"
    elif movingt == f:
        winnername = "blue is third"
        wincol = "slateblue"
    elif movingt == g:
        winnername = "pink is third"
        wincol = "plum"
    elif movingt == h:
        winnername = "black is third"
        wincol = "black"

    print(winnername)

    text.speed(1)
    text.forward(200)

    erase = turtle.Turtle()
    erase.color("ghostwhite")
    erase.shape("square")
    erase.shapesize(75)

    text.speed(50)
    text.showturtle()
    text.shape("turtle")
    text.shapesize(5)
    text.goto(-150, 175)
    text.color(fcol)
    text.stamp()
    text.goto(0, 150)
    text.write(fplace, False, "left", ("times", 50, "normal"))
    text.goto(-150, 25)
    text.color(scol)
    text.stamp()
    text.goto(0, 0)
    text.write(splace, False, "left", ("times", 50, "normal"))
    text.goto(-150, -125)
    text.color(wincol)
    text.stamp()
    text.goto(0, -150)
    text.write(winnername, False, "left", ("times", 50, "normal"))
    text.hideturtle()

    wn.exitonclick()


def bit_draw():
    import turtle

    win_l = 1000
    win_h = 1000
    box_dim = 50

    wn = turtle.Screen()
    wn.tracer(100)
    wn.setworldcoordinates(0, 0, win_h, win_l)
    pen = turtle.Turtle()

    def clear_tracer():
        pen.up()
        for i in range(box_dim):
            pen.fd(1)
        for i in range(box_dim):
            pen.back(1)

    def hor_lines(x):
        while x <= win_l - box_dim * 2:
            pen.up()
            pen.goto(x, 0)
            pen.down()
            pen.goto(x, win_h)
            x += box_dim
        pen.pensize(4)
        pen.up()
        pen.goto(x, 0)
        pen.down()
        pen.goto(x, win_h)
        pen.pensize(1)

    def ver_lines(y):
        while y <= win_h:
            pen.up()
            pen.goto(0, y)
            pen.down()
            pen.goto(win_l, y)
            y += box_dim

    def color_box(x, y):
        pen.up()
        pen.goto((int(x / box_dim)) * box_dim, (int(y / box_dim)) * box_dim)
        pen.down()
        if P_COL == "white":
            pen.color("lightgray", P_COL)
        else:
            pen.color(P_COL, P_COL)
        pen.begin_fill()
        for i in range(4):
            pen.fd(box_dim)
            pen.left(90)
        pen.end_fill()
        pen.up()

    def where_click(x, y):
        if x < win_l - box_dim:
            color_box(x, y)
            return "#B4C3FA"
        else:
            global P_COL
            if y > win_h - box_dim:
                P_COL = "#B4C3FA"
            elif y > win_h - box_dim * 2:
                P_COL = "#95C5DE"
            elif y > win_h - box_dim * 3:
                P_COL = "#B0F5EE"
            elif y > win_h - box_dim * 4:
                P_COL = "#95DEB4"
            elif y > win_h - box_dim * 5:
                P_COL = "#AFFFAB"
            elif y > win_h - box_dim * 6:
                P_COL = "#D6FAAC"
            elif y > win_h - box_dim * 7:
                P_COL = "#DEDB8E"
            elif y > win_h - box_dim * 8:
                P_COL = "#F5E6A9"
            elif y > win_h - box_dim * 9:
                P_COL = "#DEC18E"
            elif y > win_h - box_dim * 10:
                P_COL = "#FFC9A3"
            elif y > win_h - box_dim * 11:
                P_COL = "#FAACBC"
            elif y > win_h - box_dim * 12:
                P_COL = "#DD8EDE"
            elif y > win_h - box_dim * 13:
                P_COL = "#D1A8F5"
            elif y > win_h - box_dim * 14:
                P_COL = "#958EDE"
            elif y > win_h - box_dim * 15:
                P_COL = "white"

    pen.speed(100)
    pen.color("lightgray")

    ver_lines(0)
    hor_lines(0)
    global P_COL
    for i in ["#B4C3FA", "#95C5DE", "#B0F5EE", "#95DEB4", "#AFFFAB", "#D6FAAC", "#DEDB8E",
              "#F5E6A9", "#DEC18E", "#FFC9A3", "#FAACBC", "#DD8EDE", "#D1A8F5", "#958EDE", "white"]:
        P_COL = i
        pen.right(90)
        pen.forward(box_dim)
        pen.left(90)
        color_box(pen.xcor() + box_dim / 2, pen.ycor() + box_dim / 2)
    pen.forward(box_dim / 2)
    pen.write("eraser", True, "center", ("Arial", int(box_dim / 3), "normal"))
    pen.hideturtle()
    clear_tracer()
    while True:
        wn.onclick(where_click)
        pen.fd(2)
        pen.bk(2)


def adventure():
    import time
    import sys
    import turtle

    wn = turtle.Screen()
    draw = turtle.Turtle()
    uni_c = turtle.Turtle()

    def type(text, speed):
        for c in text:
            sys.stdout.write(c)
            time.sleep(speed)

    def where_click(x, y):
        if -50 < x < 50 and -50 < y < 50:
            uni_c.forward(1)

    def start_g():
        draw.turtlesize(50)
        draw.color("LightBlue")
        draw.stamp()
        t = turtle.Turtle()
        t.shape("square")
        t.turtlesize(5)
        t.color("black", "white")
        t.stamp()
        t.color("LightBlue")
        t.hideturtle()
        t.up()
        draw.forward(100)
        wn.onclick(where_click)
        uni_c.hideturtle()
        uni_c.up()
        write1 = 0
        while uni_c.xcor() < 250:
            xcor = int(uni_c.xcor())
            t.goto(0, 300)
            t.color("LightBlue")
            t.stamp()
            t.color("black")
            t.write(xcor, False, "center", ("Arial", 45, "normal"))
            t.goto(0, 200)
            if write1 == 0:
                t.write("THE GOAL IS TO PRESS THE BUTTON 250 TIMES!", False, "center", ("Arial", 45, "normal"))
                write1 = 1
            elif write1 == 1 and xcor > 9:
                t.turtlesize(10)
                t.color("LightBlue")
                t.goto(-500, 200)
                for i in range(40):
                    t.fd(25)
                    t.stamp()
                t.color("black")
                t.goto(0, 200)
                t.write("KEEP GOING!!!", False, "center", ("Arial", 45, "normal"))
                t.turtlesize(5)
                write1 = 2
            elif write1 == 2 and xcor > 49:
                t.turtlesize(10)
                t.color("LightBlue")
                t.goto(-250, 200)
                for i in range(20):
                    t.fd(25)
                    t.stamp()
                t.color("black")
                t.goto(0, 200)
                t.write("WE ARE GETTING THERE!", False, "center", ("Arial", 45, "normal"))
                t.turtlesize(5)
                write1 = 3
            elif write1 == 3 and xcor > 124:
                t.turtlesize(10)
                t.color("LightBlue")
                t.goto(-400, 200)
                for i in range(32):
                    t.fd(25)
                    t.stamp()
                t.color("black")
                t.goto(0, 200)
                t.write("HALFWAY POINT!", False, "center", ("Arial", 45, "normal"))
                t.turtlesize(5)
                write1 = 4
            elif write1 == 4 and xcor > 199:
                t.turtlesize(10)
                t.color("LightBlue")
                t.goto(-300, 200)
                for i in range(24):
                    t.fd(25)
                    t.stamp()
                t.color("black")
                t.goto(0, 200)
                t.write("NEARLY THERE!", False, "center", ("Arial", 45, "normal"))
                t.turtlesize(5)
                write1 = 5
            draw.fd(1)
            draw.bk(1)
        t.turtlesize(50)
        t.color("LightBlue")
        t.goto(0, 0)
        t.stamp()
        t.color("black")
        t.write("CONGRATULATIONS, YOU'VE WON!", False, "center", ("Arial", 45, "normal"))
        time.sleep(2)
        wn.bye()
        print()
        print()
        type("Wow, that actually was pretty fun", 0.1)
        print()
        type("Thank you for trying your best and playing the game :D", 0.1)
        print()
        print()
        print('\33[34m'"true end")

    def which_box(x, y):
        if -450 < x < -200 and -250 < y < -150:
            start_g()
        elif 200 < x < 450 and -250 < y < -150:
            wn.bye()
            print()
            print()
            print()
            type('\x1b[0;30;41m'"WHAT HAVE YOU DONE"'\33[0m', 0.1)
            print()
            time.sleep(2)
            type('\x1b[0;30;41m'"YOU'VE RUINED EVERYTHING"'\33[0m', 0.1)
            print()
            time.sleep(1)
            type('\x1b[0;30;41m'"I HAD NO PLAN FOR THIS AT ALL"'\33[0m', 0.1)
            print()
            time.sleep(0.5)
            type('\x1b[0;30;41m'"EVERYTHING IS BREAKING OH NO"'\33[0m', 0.1)
            print()
            print()
            print('\33[34m'"broken end")

    def games():
        print()
        type("Fine, we'll do it your way.", 0.2)
        wn.bgcolor("LightBlue")

        # draws game
        wn.tracer(20)
        draw.up()
        draw.shape("square")
        draw.goto(0, 300)
        draw.write("THE MOST FUNNEST", False, "center", ("Arial", 45, "normal"))
        draw.goto(0, 200)
        draw.write("GAME EVER", False, "center", ("Arial", 45, "normal"))
        draw.goto(-400, -200)
        draw.shapesize(5)
        draw.stamp()
        draw.forward(75)
        draw.stamp()
        draw.forward(75)
        draw.stamp()
        draw.forward(500)
        draw.stamp()
        draw.forward(75)
        draw.stamp()
        draw.forward(75)
        draw.stamp()
        draw.goto(325, -225)
        draw.color("white")
        draw.write("EXIT", False, "center", ("Arial", 38, "normal"))
        draw.goto(-325, -225)
        draw.write("START", False, "center", ("Arial", 38, "normal"))
        draw.hideturtle()
        draw.goto(0, 0)
        wn.onclick(which_box)
        while draw.xcor() < 10:
            draw.fd(1)
            draw.bk(1)

    def stop_it():
        type("Oh like you could do better ha!", 0.1)
        print()
        time.sleep(0.5)
        type("This story took a while to write, you know?", 0.1)
        print()
        time.sleep(0.5)
        type("You could have just appreciated it for what it is", 0.1)
        print()
        time.sleep(1)
        type("But noooooo you just "'\33[33m'"HAD"'\33[0m'" to criticise it", 0.1)
        print()
        time.sleep(0.5)
        type("You probably just want to play games instead huh?", 0.1)
        print()
        val = input('\33[4m'"Would you rather play a game than read? (y/n)"'\33[0m')
        print()
        if val == "n":
            type("Then let me continue", 0.1)
            print()
        elif val == "y":
            games()
            exit()

    def start_real():
        print()
        type("Well I'm sorry but I don't have one", 0.05)
        time.sleep(1)
        print()
        type("Let me double check", 0.05)
        time.sleep(1)
        print()
        print('\33[31m' + "*rustle sound*"'\33[0m')
        # rustle sound
        time.sleep(3)
        type("Ah ok, found one!", 0.05)
        print()
        print()
        time.sleep(1)
        type('\33[35m' + "Long ago, the four nations lived together in harmony. " +
             "Then, everything changed when the Fire-"'\33[0m', 0.05)
        print()
        type("Wait not this one", 0.2)
        time.sleep(1)
        print()
        print('\33[31m' "*more papers rustling*"'\33[0m')
        time.sleep(3)
        type("Finally! An original story", 0.1)
        time.sleep(1)
        print()
        print()
        type('\33[35m'"Cold days like these were far to come by for Quinn. He recently moved into the neighborhood",
             0.03)
        print()
        type("and the struggles of life pursued him. He felt unaccomplished. And so on one walk home from", 0.03)
        print()
        type("work, he gazed at the beauty of the cherry blossoms on each side of him. Flowering crowns", 0.03)
        print()
        type("flaunted by the trees, only further complimented by the peach sunset.", 0.03)
        print()
        print()
        inp1 = input('\33[4m'"Do you like the story so far? (y/n)" '\33[0m')
        if inp1 == "y":
            type("I'll continue", 0.1)
        elif inp1 == "n":
            stop_it()
        else:
            type("I'm taking that as a yes", 0.1)
        time.sleep(1)
        print()
        print()
        type('\33[35m'"But then he came across a small cardboard parcel on the ground. He picked it up", 0.03)
        print()
        type("simply assuming someone lost it. Walking a few blocks up, his curiosity grew. What would a", 0.03)
        print()
        type("small package be doing here? He tried to shake it but the questions began to wear on him. There were",
             0.03)
        print()
        type("no addresses, no names, nothing. As if the package were meant for him. He finally cracked and set it",
             0.03)
        print()
        type("on the ground.", 0.1)
        print()
        print()
        inp1 = input('\33[4m'"Do you like the story so far? (y/n)" '\33[0m')
        if inp1 == "y":
            type("I'll continue", 0.1)
        elif inp1 == "n":
            stop_it()
            exit()
        else:
            type("I'm taking that as a yes", 0.1)
        time.sleep(1)
        print()
        print()
        type('\33[35m'"He fingered out a pocket knife. Flipping it open, he started scratching at the surface of", 0.03)
        print()
        type("the package. Once tape teared, it was nearly open. Then the sides followed suit. Then he sloped the",
             0.03)
        print()
        type("flaps open. Finally, what was inside was the cause of the allure the whole time. Peering in he found",
             0.03)
        print()
        time.sleep(3)
        type("nothing. Just some bubble wrap. There was nothing in the package. The day was completely uneventful",
             0.03)
        print()
        type("his life had no change from that event and was unimportant. That's it. The end.", 0.03)
        print()
        print()
        inp1 = input('\33[4m'"Did you like the story?(y/n)" '\33[0m')
        if inp1 == "n":
            stop_it()
            exit()
        elif inp1 != "y":
            type("I'm taking that as a yes", 0.1)
        print()
        time.sleep(2)
        type("Thank you so much for liking the story! You're such a good listener :)", 0.1)
        time.sleep(0.5)
        print()
        print()
        print('\33[34m'"basic end")
        exit()

    def cmon1(f1, acc1):
        f1m = f1 != "n" and f1 != "y"
        if acc1 == 0 and f1m:
            type('''Please input "y" or "n"''', 0.05)
            print()
        elif acc1 == 1 and f1m:
            type('''PLEASE input either "y" or "n"''', 0.05)
            print()
        elif acc1 == 2 and f1m:
            type('''I promise this is not a trick just say "y" or "n"''', 0.05)
            print()
        elif acc1 == 3 and f1m:
            type("There's no need to contest this," + '\33[33m' + " PLEASE " + '\33[0m' + '''SAY "y" OR "n"''', 0.05)
            print()
        if f1 == "y":
            start_real()
        elif f1 == "n":
            print()
            type("Oh ok", 0.05)
            print()
            time.sleep(1)
            type("I guess I could get used to this", 0.05)
            print()
            time.sleep(2)
            print()
            print('\33[34m'"dumb end")
            exit()

    uni_c.hideturtle()
    draw.hideturtle()
    print("The Shortest Story: By Aristotle Kaporis")
    type("hello", 0.5)
    print()
    print()
    print("Process finished with exit code 0")
    time.sleep(6)
    print()
    type("No... that's not right", 0.05)
    print()
    time.sleep(1)
    type("There has to be" + '\33[33m' + " SOMETHING " + '\33[0m' + "in this program right?", 0.05)
    print()
    time.sleep(0.5)
    type("How else would this earn credit?", 0.05)
    print()
    time.sleep(1.5)
    for i in range(3):
        print(".")
        time.sleep(1.5)
    for acc1 in range(5):
        cmon1(input('\33[4m' + "Do you want a full story? (input y or n)" + '\33[0m'), acc1)
    print()
    type("Look, I don't want to deal with someone like this", 0.05)
    print()
    type("Just have an ending", 0.05)
    print()
    print()
    print('\33[34m'"refusal end")


def guessing():
    import random

    def generate(min_n, max_n):
        return random.randrange(min_n, max_n + 1)

    def make_num(dif):
        if dif == "medium":
            return generate(0, 100)
        elif dif == "hard":
            return generate(0, 1000)
        return generate(0, 10)

    def easy_robot(round_num, win1, win2, round_over, first, f_save):
        num1 = make_num("easy")
        num2 = make_num("easy")
        while win1 <= 2 and win2 <= 2:
            if first:
                guess = int(input('\33[4m'"What is your guess P1?"'\33[0m'"\n"))
                if guess > num1:
                    print("The number is lower")
                elif guess < num1:
                    print("The number is higher")
                elif guess == num1:
                    round_num += 1
                    print('\x1b[0;30;47m'"Player wins round", round_num, '\33[0m')
                    print('\x1b[0;30;47m'"Robot's number was", num2, '\33[0m'"\n")
                    win1 += 1
                    print(win1, ":", win2)
                    print()
                    round_over = True
                print()

            if not round_over:
                first = True
                guess = random.randrange(0, 11)
                print("Robot guessed", guess)
                if guess > num2:
                    print("The number is lower")
                elif guess < num2:
                    print("The number is higher")
                elif guess == num2:
                    round_num += 1
                    print('\x1b[0;30;47m'"Robot wins round", round_num, '\33[0m')
                    print('\x1b[0;30;47m'"Player's number was", num1, '\33[0m'"\n")
                    win2 += 1
                    print(win1, ":", win2)
                    print()
                    round_over = True
                print()
            if win2 == 3:
                print('\n''\33[34m'"ROBOT WINS!"'\33[0m')
            elif win1 == 3:
                print('\n''\33[34m'"PLAYER WINS!"'\33[0m')
            if round_over:
                num1 = make_num("easy")
                num2 = make_num("easy")
                if f_save:
                    first = False
                    f_save = False
                else:
                    first = True
                    f_save = True
                round_over = False

    def medium_robot(round_num, win1, win2, round_over, first, f_save):
        num1 = make_num("medium")
        num2 = make_num("medium")
        highest_n = 101
        lowest_n = 0
        while win1 <= 2 and win2 <= 2:
            if first:
                guess = int(input('\33[4m'"What is your guess P1?"'\33[0m'"\n"))
                if guess > num1:
                    print("The number is lower")
                elif guess < num1:
                    print("The number is higher")
                elif guess == num1:
                    round_num += 1
                    print('\x1b[0;30;47m'"Player wins round", round_num, '\33[0m')
                    print('\x1b[0;30;47m'"Robot's number was", num2, '\33[0m'"\n")
                    win1 += 1
                    print(win1, ":", win2)
                    print()
                    round_over = True
                print()

            if not round_over:
                first = True
                guess = random.randrange(lowest_n + 1, highest_n)
                print("Robot guessed", guess)
                if guess > num2:
                    print("The number is lower")
                    highest_n = guess
                elif guess < num2:
                    print("The number is higher")
                    lowest_n = guess
                elif guess == num2:
                    round_num += 1
                    print('\x1b[0;30;47m'"Robot wins round", round_num, '\33[0m')
                    print('\x1b[0;30;47m'"Player's number was", num1, '\33[0m'"\n")
                    win2 += 1
                    print(win1, ":", win2)
                    print()
                    round_over = True
                print()
            if win2 == 3:
                print('\n''\33[34m'"ROBOT WINS!"'\33[0m')
            elif win1 == 3:
                print('\n''\33[34m'"PLAYER WINS!"'\33[0m')
            if round_over:
                num1 = make_num("medium")
                num2 = make_num("medium")
                highest_n = 101
                lowest_n = 0
                if f_save:
                    first = False
                    f_save = False
                else:
                    first = True
                    f_save = True
                round_over = False

    def hard_robot(round_num, win1, win2, round_over, first, f_save):
        num1 = make_num("hard")
        num2 = make_num("hard")
        highest_n = 1001
        lowest_n = 0
        while win1 <= 2 and win2 <= 2:
            if first:
                guess = int(input('\33[4m'"What is your guess P1?"'\33[0m'"\n"))
                if guess > num1:
                    print("The number is lower")
                elif guess < num1:
                    print("The number is higher")
                elif guess == num1:
                    round_num += 1
                    print('\x1b[0;30;47m'"Player wins round", round_num, '\33[0m')
                    print('\x1b[0;30;47m'"Robot's number was", num2, '\33[0m'"\n")
                    win1 += 1
                    print(win1, ":", win2)
                    print()
                    round_over = True
                print()

            if not round_over:
                first = True
                guess = int(lowest_n + (highest_n - lowest_n) / 2)
                print("Robot guessed", guess)
                if guess > num2:
                    print("The number is lower")
                    highest_n = guess
                elif guess < num2:
                    print("The number is higher")
                    lowest_n = guess
                elif guess == num2:
                    round_num += 1
                    print('\x1b[0;30;47m'"Robot wins round", round_num, '\33[0m')
                    print('\x1b[0;30;47m'"Player's number was", num1, '\33[0m'"\n")
                    win2 += 1
                    print(win1, ":", win2)
                    print()
                    round_over = True
                print()
            if win2 == 3:
                print('\n''\33[34m'"ROBOT WINS!"'\33[0m')
            elif win1 == 3:
                print('\n''\33[34m'"PLAYER WINS!"'\33[0m')
            if round_over:
                num1 = make_num("hard")
                num2 = make_num("hard")
                highest_n = 1001
                lowest_n = 0
                if f_save:
                    first = False
                    f_save = False
                else:
                    first = True
                    f_save = True
                round_over = False

    def vs_robot():
        dif = input('\33[4m'"How difficult would you like it? (easy/medium/hard)"'\33[0m'"\n")
        round_num = 0
        win1 = 0
        win2 = 0
        round_over = False
        first = random.randrange(0, 2)
        if first == 1:
            first = True
            print("Player is going first!")
        else:
            first = False
            print("Robot is going first!")
        f_save = first
        # game start
        if dif == "easy":
            easy_robot(round_num, win1, win2, round_over, first, f_save)
        elif dif == "medium":
            medium_robot(round_num, win1, win2, round_over, first, f_save)
        elif dif == "hard":
            hard_robot(round_num, win1, win2, round_over, first, f_save)

    def vs_human():
        dif = input('\33[4m'"Which difficulty would you like? (easy/medium/hard)"'\33[0m'"\n")
        num1 = make_num(dif)
        num2 = make_num(dif)
        round_num = 0
        win1 = 0
        win2 = 0
        round_over = False
        first = random.randrange(0, 2)
        if first == 1:
            first = True
            print("P1 is going first!")
        else:
            first = False
            print("P2 is going first!")
        f_save = first
        # game start
        while win1 <= 2 and win2 <= 2:
            if first:
                guess = int(input('\33[4m'"What is your guess P1?"'\33[0m'"\n"))
                if guess > num1:
                    print("The number is lower")
                elif guess < num1:
                    print("The number is higher")
                elif guess == num1:
                    round_num += 1
                    print('\x1b[0;30;47m'"P1 wins round", round_num, '\33[0m')
                    print('\x1b[0;30;47m'"P2's number was", num2, '\33[0m'"\n")
                    win1 += 1
                    print(win1, ":", win2)
                    print()
                    round_over = True
                print()

            if not round_over:
                first = True
                guess = int(input('\33[4m'"What is your guess P2?"'\33[0m'"\n"))
                if guess > num2:
                    print("The number is lower")
                elif guess < num2:
                    print("The number is higher")
                elif guess == num2:
                    round_num += 1
                    print('\x1b[0;30;47m'"P2 wins round", round_num, '\33[0m')
                    print('\x1b[0;30;47m'"P1's number was", num1, '\33[0m'"\n")
                    win2 += 1
                    print(win1, ":", win2)
                    print()
                    round_over = True

                print()
            if win2 == 3:
                print('\n''\33[34m'"P2 WINS!"'\33[0m')
            elif win1 == 3:
                print('\n''\33[34m'"P1 WINS!"'\33[0m')
            if round_over:
                num1 = make_num(dif)
                num2 = make_num(dif)
                if f_save:
                    first = False
                    f_save = False
                else:
                    first = True
                    f_save = True
                round_over = False

    # code executed every time
    print("Welcome to the Guessing Game!")
    play = True
    while play:
        gamemode = input("\n"'\33[4m'"Player vs player or player vs robot? (p/r)"'\33[0m'"\n")
        if gamemode == "p":
            vs_human()
        else:
            vs_robot()
        if input("Would you like to play again?(y/n)""\n") != "y":
            play = False


def pong():
    import pygame, sys, math, random

    black = (0, 0, 0)
    white = (255, 255, 255)
    win_w = 970
    win_h = 520
    fps = 60

    class Paddle:

        def __init__(self, width, height, speed, xpos, ypos):
            self.w = width
            self.h = height
            self.speed = speed
            self.image = pygame.Surface((width, height))
            self.rect = pygame.Rect(width * 2, win_h / 2 - height / 2, width, height)
            self.xpos = xpos
            self.ypos = ypos
            self.score = 0

    class Ball:

        def __init__(self, size, speed, xpos, ypos):
            self.size = size
            self.speed = speed
            self.image = pygame.Surface((size, size))
            self.rect = pygame.Rect(win_w / 2, win_h / 2 - size / 2, size, size)
            self.xpos = xpos
            self.ypos = ypos
            self.true_loc = int(win_w / 2 - self.size / 2), int(win_h / 2 - self.size / 2)

        def repos(self):
            self.rect.center = self.true_loc = (win_w / 2 - self.size / 2), int(win_h / 2 - self.size / 2)
            self.speed = 1, 1

    def sfx(sound):
        pygame.mixer.Sound("pong/sounds/" + sound + ".ogg").play()

    pygame.init()
    # paddle stuff
    p_up1 = False
    p_down1 = False

    p_up2 = False
    p_down2 = False

    pygame.display.set_caption("Pong")
    screen = pygame.display.set_mode((win_w, win_h))

    left_paddle = Paddle(40, 150, 2, win_w / 20, win_h / 2 - 75)
    right_paddle = Paddle(40, 150, 2, win_w - (win_w / 20 + 40), win_h / 2 - 75)

    num_font = pygame.font.Font("pong/fonts/CaviarDreams.ttf", 50)
    win_font = pygame.font.Font("pong/fonts/aldo.ttf", 100)
    left_score = num_font.render(str(left_paddle.score), True, black)
    left_score_rect = left_score.get_rect()
    left_score_rect = left_score_rect.move(win_w / 3 - left_score_rect.width / 2, win_h / 6)
    right_score = num_font.render(str(right_paddle.score), True, black)
    right_score_rect = right_score.get_rect()
    right_score_rect = right_score_rect.move(win_w * 2 / 3 - right_score_rect.width / 2, win_h / 6)

    leave = num_font.render("leave", True, black)
    leave_rect = leave.get_rect()
    leave_rect = leave_rect.move(win_w * 2 / 3, win_h / (3 / 2))
    replay = num_font.render("replay", True, black)
    replay_rect = replay.get_rect()
    replay_rect = replay_rect.move(win_w / 3 - replay_rect.width, win_h / (3 / 2))

    left_win = win_font.render("LEFT WON!", True, black)
    left_win_rect = left_win.get_rect()
    left_win_rect = left_win_rect.move(win_w / 2 - left_win_rect.width / 2, win_h / 2 - left_win_rect.height / 2)
    right_win = win_font.render("RIGHT WON!", True, black)
    right_win_rect = right_win.get_rect()
    right_win_rect = right_win_rect.move(win_w / 2 - right_win_rect.width / 2,
                                         win_h / 2 - right_win_rect.height / 2)

    left_paddle.image.fill(black)
    right_paddle.image.fill(black)
    # ball stuff
    ball = Ball(20, (1, 1), win_w, win_h)
    ball.image.fill(black)
    ball_still = True
    time_start = 0
    ball.true_loc = int(win_w / 2 - ball.size), int(win_h / 2 - ball.size)

    bg_val = random.randrange(3)
    intro_bg = pygame.image.load("pong/images/title_3.png").convert()
    if bg_val == 1:
        intro_bg = pygame.image.load("pong/images/title_1.png").convert()
    elif bg_val == 2:
        intro_bg = pygame.image.load("pong/images/title_2.png").convert()

    intro_bg = pygame.transform.scale(intro_bg, (win_w, win_h))
    intro_rect = intro_bg.get_rect()

    recent_p = 0
    add = num_font.render("+1", True, white)
    add_rect = add.get_rect()
    add_rect = add_rect.move(win_w / 3 - add_rect.width / 2, win_h / 6 + left_score_rect.height)

    clock = pygame.time.Clock()
    play = intro = True

    # start screen
    sfx("amb")
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_RETURN] != 0:
                intro = False
        # screen.fill(white)
        # if pygame.time.get_ticks() % 1000 < 500: DO SOMETHING WITH THE BLINKING SCREEN.

        screen.blit(intro_bg, intro_rect)

        clock.tick(fps)
        pygame.display.flip()

    # game start
    true_time_st = pygame.time.get_ticks()
    while play:
        # keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    p_up1 = True
                if event.key == pygame.K_s:
                    p_down1 = True
                if event.key == pygame.K_UP:
                    p_up2 = True
                if event.key == pygame.K_DOWN:
                    p_down2 = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    p_up1 = False
                if event.key == pygame.K_s:
                    p_down1 = False
                if event.key == pygame.K_UP:
                    p_up2 = False
                if event.key == pygame.K_DOWN:
                    p_down2 = False

        if ball.rect.left > win_w:
            left_paddle.score += 1
            left_score = num_font.render(str(left_paddle.score), True, black)
            ball.repos()
            ball_still = True
            time_start = pygame.time.get_ticks() - true_time_st
            recent_p = win_w / 3 - add_rect.width / 2
        if ball.rect.right < 0:
            right_paddle.score += 1
            right_score = num_font.render(str(right_paddle.score), True, black)
            ball.repos()
            ball_still = True
            time_start = pygame.time.get_ticks() - true_time_st
            recent_p = win_w / (3 / 2) - add_rect.width / 2

        # movement
        if p_up1 and left_paddle.ypos > 0:
            left_paddle.ypos -= left_paddle.speed
        if p_down1 and left_paddle.ypos < win_h - left_paddle.h:
            left_paddle.ypos += left_paddle.speed
        if p_up2 and right_paddle.ypos > 0:
            right_paddle.ypos -= right_paddle.speed
        if p_down2 and right_paddle.ypos < win_h - right_paddle.h:
            right_paddle.ypos += right_paddle.speed

        if ball.rect.bottom >= win_h or ball.rect.top <= 0:
            ball.speed = (ball.speed[0], -ball.speed[1])
        if right_paddle.xpos + right_paddle.w >= ball.rect.right >= \
                right_paddle.xpos and math.fabs(right_paddle.ypos + right_paddle.h / 2 - ball.rect.center[1]) \
                <= right_paddle.h / 2 + ball.size / 2:
            ball.speed = (-math.fabs(ball.speed[0]), ball.speed[1])
            sfx("m" + str(random.randrange(8) + 1))
        elif left_paddle.xpos + left_paddle.w >= ball.rect.left >= \
                left_paddle.xpos and math.fabs(left_paddle.ypos + left_paddle.h / 2 - ball.rect.center[1]) \
                <= left_paddle.h / 2 + ball.size / 2:
            ball.speed = (math.fabs(ball.speed[0]), ball.speed[1])
            sfx("m" + str(random.randrange(8) + 1))
        v1 = (pygame.time.get_ticks() - true_time_st) - time_start

        if pygame.time.get_ticks() % 1000 == 0:
            ball.speed = ball.speed[0] * 1.1, ball.speed[1] * 1.1

        if not ball_still:
            ball.true_loc = ball.true_loc[0] + ball.speed[0], ball.true_loc[1] + ball.speed[1]
            ball.rect.center = (ball.true_loc[0] + ball.size, ball.true_loc[1] + ball.size)
        elif v1 >= 1000:
            ball_still = False
        elif v1 <= 765 and time_start > 800:
            idk = v1 // 3
            add = num_font.render("+1", True, (idk, idk, idk))
            add_rect = add.get_rect()
            add_rect = add_rect.move(recent_p, win_h / 6 + left_score_rect.height)

        # draws sprites at start
        screen.fill(white)
        screen.blit(left_paddle.image, (left_paddle.xpos, left_paddle.ypos))
        screen.blit(right_paddle.image, (right_paddle.xpos, right_paddle.ypos))
        screen.blit(left_score, left_score_rect)
        screen.blit(right_score, right_score_rect)
        screen.blit(add, add_rect)
        screen.blit(ball.image, ball.rect)
        pygame.display.flip()

        if left_paddle.score > 2 or right_paddle.score > 2:
            screen.fill(white)
            finished = True
            screen.blit(leave, leave_rect)
            screen.blit(replay, replay_rect)
            if left_paddle.score > right_paddle.score:
                screen.blit(left_win, left_win_rect)
            else:
                screen.blit(right_win, right_win_rect)
            while finished:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if win_w / 3 - replay_rect.width < event.pos[0] < win_w / 3 and\
                                (win_h / 3) * 2 < event.pos[1] < win_h - win_h / 6:
                            finished = False
                            left_paddle.score = 0
                            right_paddle.score = 0
                            ball_still = True
                            true_time_st = pygame.time.get_ticks()
                            time_start = 0
                            left_score = num_font.render(str(left_paddle.score), True, black)
                            left_score_rect = left_score.get_rect()
                            left_score_rect = left_score_rect.move(win_w / 3 - left_score_rect.width / 2, win_h / 6)
                            right_score = num_font.render(str(right_paddle.score), True, black)
                            right_score_rect = right_score.get_rect()
                            right_score_rect = right_score_rect.move(win_w * 2 / 3 - right_score_rect.width / 2,
                                                                     win_h / 6)
                            ball.repos()
                            add = num_font.render("+1", True, white)
                        elif (win_w / 3) * 2 + leave_rect.width > event.pos[0] > (win_w / 3) * 2 and (
                                win_h / 3) * 2 < event.pos[1] < win_h - win_h / 6:
                            sys.exit()
                pygame.display.flip()


def density():
    import sys, pygame, os, random

    # Force static position of screen
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Constants
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (104, 111, 255)
    l_blue = (56, 168, 225)
    pink = (255, 71, 250)
    green = (71, 255, 71)
    ship_size = 10
    top_buffer = 50
    pill_height = 25
    pill_width = 7

    size = width, height = 920, 570

    # Runs imported module
    pygame.init()

    class Ship(pygame.sprite.Sprite):
        def __init__(self, x, y, side):
            pygame.sprite.Sprite.__init__(self)
            self.speed = 7
            self.image = pygame.Surface((ship_size, ship_size)).convert()
            self.rect = pygame.Rect(x, y, ship_size, ship_size)
            self.type = side
            self.size = ship_size
            self.points = 0

        def update(self, p_g):
            key = pygame.key.get_pressed()
            if self.type == "left":
                if key[pygame.K_w]: self.rect.y -= self.speed
                if key[pygame.K_s]: self.rect.y += self.speed
                if key[pygame.K_a]: self.rect.x -= self.speed
                if key[pygame.K_d]: self.rect.x += self.speed

                if self.rect.x <= 0:
                    self.rect.x = 0
                elif self.rect.x >= width / 2 - self.size:
                    self.rect.x = width / 2 - self.size
            if self.type == "right":
                if key[pygame.K_UP]: self.rect.y -= self.speed
                if key[pygame.K_DOWN]: self.rect.y += self.speed
                if key[pygame.K_LEFT]: self.rect.x -= self.speed
                if key[pygame.K_RIGHT]: self.rect.x += self.speed

                if self.rect.x <= width / 2:
                    self.rect.x = width / 2
                elif self.rect.x + self.size >= width:
                    self.rect.x = width - self.size

            if self.rect.y <= top_buffer:
                self.rect.y = top_buffer
            elif self.rect.y >= height - self.size:
                self.rect.y = height - self.size

            collisions = pygame.sprite.spritecollide(self, p_g, True)
            for p in collisions:
                self.size += p.density / 4
                self.points += p.density
                self.rect = pygame.Rect(self.rect.x, self.rect.y, self.size, self.size)
                self.image = pygame.Surface((self.size, self.size)).convert()

    class Pill(pygame.sprite.Sprite):
        def __init__(self, x, density):
            pygame.sprite.Sprite.__init__(self)
            self.speed = 3
            self.density = density
            self.image = pygame.Surface((pill_width, pill_height)).convert()
            self.rect = self.image.get_rect().move(x, top_buffer)

        def update(self):
            if self.density == 1:
                self.image.fill(blue)
            elif self.density == 2:
                self.image.fill(l_blue)
            elif self.density == 3:
                self.image.fill(pink)
            elif self.density == 5:
                self.image.fill(green)

            self.rect.y += self.speed
            if self.rect.y > height:
                self.kill()

    # init local vars
    fps = 30

    num_font = pygame.font.Font("density/rounded.ttf", 50)

    pygame.display.set_caption('Density')
    screen = pygame.display.set_mode(size, pygame.SRCALPHA)
    clock = pygame.time.Clock()
    play = True
    loop_counter = 0

    vertical = pygame.Surface((1, height - top_buffer)).convert()
    horizontal = pygame.Surface((width, 1)).convert()

    # game obj here
    p1 = Ship(width / 4 - ship_size / 2, height - (4 * ship_size), "left")
    p2 = Ship(width * 0.75 - ship_size / 2, height - (4 * ship_size), "right")

    # groups
    ship_group = pygame.sprite.Group()
    ship_group.add(p1, p2)
    pill_group = pygame.sprite.Group()

    # Gameplay
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        if loop_counter % 6 == 0:
            pill_l = Pill(random.randrange(0, width / 2 - pill_width), int(random.choice("1111111111222223335")))
            pill_r = Pill(random.randrange(width / 2 + pill_width, width - pill_width),
                          int(random.choice("1111111111222223335")))
            pill_group.add(pill_l, pill_r)

        # update groups
        ship_group.update(pill_group)
        pill_group.update()
        p1p = num_font.render(str(p1.points), True, black)
        p2p = num_font.render(str(p2.points), True, black)

        p1p_rect = p1p.get_rect()
        p1p_rect = p1p_rect.move(width / 4 - p1p_rect.width / 2, 0)
        p2p_rect = p2p.get_rect()
        p2p_rect = p2p_rect.move(width * 0.75 - p2p_rect.width / 2, 0)

        # Print background
        screen.fill(white)
        ship_group.draw(screen)
        pill_group.draw(screen)
        screen.blit(p1.image, p1.rect)
        screen.blit(p1p, p1p_rect)
        screen.blit(p2.image, p2.rect)
        screen.blit(p2p, p2p_rect)
        screen.blit(vertical, (width / 2, top_buffer))
        screen.blit(horizontal, (0, top_buffer))

        if p1.points >= 100 or p2.points >= 100:
            play = False

        # Limits frames
        loop_counter += 1
        clock.tick(fps)
        # Writes to main surface
        pygame.display.flip()

    font = pygame.font.Font("density/earthorbiter.ttf", 100)
    if p2.points > p1.points:
        text = font.render("PLAYER 2 WINS", True, black)
    elif p1.points < p2.points:
        text = font.render("PLAYER 1 WINS", True, black)
    else:
        text = font.render("TIE!", True, black)
    text_rect = text.get_rect()

    screen.blit(text, text_rect.move(width / 2 - text_rect.width / 2, height / 6))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


def raiden():
    import pygame, sys, random

    # global vars
    win_w = 512
    win_h = 640
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    silver = (115, 115, 135)
    sc_scroll = 2

    def scroll(obj, speed):
        obj.y += speed

    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((32, 32))
            self.image.convert()
            self.image.fill(black)
            self.rect = pygame.Rect(x, y, 32, 32)

    class Image:
        def __init__(self, image, x, y):
            self.image = pygame.image.load("raiden/images/" + image + ".png")
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y

        def scroll(self, speed):
            self.rect.y += speed

    def play_s(sound):
        pygame.mixer.Sound("raiden/sounds/" + sound + ".mp3").play()

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, ship_x, ship_y, b_type):
            pygame.sprite.Sprite.__init__(self)
            self.speed = 4
            self.x = ship_x + 2
            self.y = ship_y
            self.image = Image("bullet", self.x, self.y)
            self.b_type = b_type
            self.image = pygame.transform.scale(self.image.image, (6, 18))

            if self.b_type == 2:
                self.image = pygame.transform.rotate(self.image, 11.31)
            elif self.b_type == 3:
                self.image = pygame.transform.rotate(self.image, -11.31)
            elif self.b_type == 4:
                self.x -= 6
            elif self.b_type == 5:
                self.x += 6

            self.image.convert()
            self.rect = pygame.Rect(self.x, self.y, 5, 15)

        def update(self, enemies, bul_g, camera, upgrades, ship):
            if self.b_type == 1 or self.b_type == 4 or self.b_type == 5:
                self.rect.y -= 10
            if self.b_type == 2:
                self.rect.y -= 10
                self.rect.x -= 2
            if self.b_type == 3:
                self.rect.y -= 10
                self.rect.x += 2
            for i in enemies:
                if i.type == "crystal":
                    if self.rect.colliderect(camera.apply(i)):
                        i.hit(enemies, upgrades, camera, ship)
                        bul_g.remove(self)
                elif self.rect.colliderect(i):
                    i.hit(enemies, upgrades, camera, ship)
                    bul_g.remove(self)
            if self.rect.y <= -self.image.get_height():
                bul_g.remove(self)

    class Heart(pygame.sprite.Sprite):
        def __init__(self, distance):
            pygame.sprite.Sprite.__init__(self)
            self.x = distance * 90 + win_w * distance / 50
            self.image = pygame.transform.scale(Image("heart", 0, 0).image, (90, 80))
            self.image.convert()
            self.rect = pygame.Rect(self.x, 0, 90, 80)

    class Upgrade(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.x = x - 25
            self.y = y - 25
            self.type = random.randrange(1, 3)
            self.image = pygame.transform.scale(Image("upgrades/upgrade_" + str(self.type) + "_1", 0, 0).image,
                                                (50, 50))
            self.image.convert()
            self.rect = pygame.Rect(self.x, self.y, 50, 50)
            self.frame = 1

        def update(self, ship, upg_g, flash):
            if self.type == 1:
                self.image = pygame.transform.scale(Image("upgrades/upgrade_1_" +
                                                          str(int(self.frame % 100 / 10) + 1), 0, 0).image, (50, 50))
            elif self.frame % 40 <= 20:
                self.image = pygame.transform.scale(Image("upgrades/upgrade_2_" +
                                                          str(int(self.frame % 40 / 4) + 1), 0, 0).image, (50, 50))
            else:
                self.image = pygame.transform.scale(Image("upgrades/upgrade_2_" +
                                                          str(int(10 - self.frame % 40 / 4) + 1), 0, 0).image, (50, 50))
            self.image.convert()
            self.frame += 1
            if ship.rect.colliderect(self.rect):
                if self.type == 1 and ship.upgrade < 4:
                    ship.upgrade += 1
                elif self.type == 2:
                    ship.speed_cap += 1
                    ship.speed += 1
                ship.score += 50000
                play_s("upgrade")
                flash.action(white)
                upg_g.remove(self)

    class Enemy(pygame.sprite.Sprite):
        def __init__(self, size, e_type):
            pygame.sprite.Sprite.__init__(self)
            self.size = size * 36
            self.image = pygame.transform.scale(Image(e_type + str(1), 0, 0).image, (self.size, self.size))
            self.image.convert()
            if e_type == "crystal":
                self.rotation = random.randrange(-1, 2) * 20
                self.image = pygame.transform.rotate(self.image, self.rotation)
                self.rect = pygame.Rect(random.randrange(int(32 ** 2 / 1.5) - self.size), -self.size, self.size,
                                        self.size)
            else:
                self.rect = pygame.Rect(random.randrange(win_w - self.size), -self.size / 9 * 5, self.size,
                                        self.size / 9 * 5)
            self.type = e_type
            self.health = 5
            self.damage = 0
            self.state = 1
            self.ref = False

        def update(self, time):
            # crystal refresh
            if self.type == "crystal":
                scroll(self.rect, sc_scroll)
                if self.ref:
                    self.image = pygame.transform.scale(
                        Image("crystal" + str(self.state), 0, 0).image, (self.size, self.size))
                    self.image.convert()
                    self.image = pygame.transform.rotate(self.image, self.rotation)
            # bat refresh
            if self.damage == 0:
                self.ref = True
            if self.type == "bat":
                scroll(self.rect, sc_scroll)
                calc = time % 100
                if calc == 25:
                    self.state = 1
                    self.ref = True
                elif calc == 50 or calc == 0:
                    self.state = 2
                    self.ref = True
                elif calc == 75:
                    self.state = 3
                    self.ref = True
                if self.damage > 0 and self.ref:
                    self.image = pygame.transform.scale(
                        Image("hit_bat" + str(self.state), 0, 0).image, (self.size, self.size / 9 * 5))
                elif self.ref:
                    self.image = pygame.transform.scale(
                        Image("bat" + str(self.state), 0, 0).image, (self.size, self.size / 9 * 5))
                if self.ref:
                    self.image.convert()
                    self.ref = False
            self.damage -= 1

        def hit(self, enemies, upgrades, camera, ship):
            ship.score += random.randrange(350, 440)
            self.health -= 1
            self.ref = True
            self.damage = 10
            if self.type == "crystal":
                self.state += 1
            if self.health == 0:
                enemies.remove(self)
                play_s("self_hit")
                ship.score += random.randrange(2000, 3000)
                if random.randrange(15) == 5:
                    if self.type == "crystal":
                        upgrades.add(
                            Upgrade(camera.apply(self).x + self.size / 2, camera.apply(self).y + self.size / 2))
                    else:
                        upgrades.add(Upgrade(self.rect.x + self.size / 2, self.rect.y + self.size / 18 * 5))

    class Counter(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.bg_image = pygame.transform.scale(Image("score_bar", 0, 0).image, (200, 40))
            self.bg_rect = pygame.Rect(0, win_h - 40, 0, 0)
            self.bg_image.convert()
            self.text_img = pygame.font.Font("raiden/ConnectionII.ttf", 35).render("0", False, white)
            self.text_rect = self.text_img.get_rect()
            self.text_rect = self.text_rect.move(0, win_h - self.text_rect.h)

        def update(self, ship):
            self.text_img = pygame.font.Font("raiden/ConnectionII.ttf", 35).render(str(ship.score), False, white)
            self.text_rect = self.text_img.get_rect()
            self.text_rect = self.text_rect.move(0, win_h - self.text_rect.h)

    class Ship(pygame.sprite.Sprite):
        def __init__(self, size, speed, container, image):
            pygame.sprite.Sprite.__init__(self)
            self.container = container
            self.image = image
            self.size = size
            self.speed = speed
            self.speed_cap = 4
            self.image.convert()
            self.cooldown = 0
            self.rect = pygame.Rect(win_w / 2 - size / 2, win_h / 1.25 - size / 2, 36, 48)
            self.upgrade = 1
            self.health = pygame.sprite.Group()
            self.health_c = 3
            self.i_frames = 0
            self.score = 0
            self.score_counter = Counter()
            self.dead = False
            self.dead_frame = 0

            for i in range(self.health_c):
                self.health.add(Heart(i))

        def update(self, bul_g, enemies, camera, flash, gametime):
            self.cooldown -= 1
            self.i_frames -= 1
            key = pygame.key.get_pressed()
            if key[pygame.K_w] or key[pygame.K_UP]: self.rect.y -= int(self.speed)
            if key[pygame.K_s] or key[pygame.K_DOWN]: self.rect.y += int(self.speed)
            if key[pygame.K_a] or key[pygame.K_LEFT]: self.rect.x -= int(self.speed)
            if key[pygame.K_d] or key[pygame.K_RIGHT]: self.rect.x += int(self.speed)
            if key[pygame.K_SPACE] and self.cooldown <= 0:
                play_s("shoot")
                if self.upgrade == 1 or self.upgrade == 3:
                    bul_g.add(Bullet(self.rect.x + self.rect.w / 2 - 5, self.rect.y, 1))
                if self.upgrade == 2 or self.upgrade == 4:
                    bul_g.add(Bullet(self.rect.x + self.rect.w / 2 - 5, self.rect.y, 4))
                    bul_g.add(Bullet(self.rect.x + self.rect.w / 2 - 5, self.rect.y, 5))
                if self.upgrade == 3 or self.upgrade == 4:
                    bul_g.add(Bullet(self.rect.x + self.rect.w / 2 - 5, self.rect.y, 2))
                    bul_g.add(Bullet(self.rect.x + self.rect.w / 2 - 5, self.rect.y, 3))

                self.cooldown = 10

            for i in enemies:
                if ((self.rect.colliderect(i.rect) and i.type == "bat") or (self.rect.colliderect(camera.apply(i)) and
                                                                            i.type == "raiden/crystal")) and self.i_frames < 0:
                    self.speed = 1
                    self.health_c -= 1
                    self.i_frames = 100
                    lol = 0
                    flash.action(red)
                    play_s("self_hit")
                    for acc in self.health:
                        lol = acc
                    self.health.remove(lol)
                    if self.health_c == 0:
                        self.i_frames = gametime
                        self.dead = True
                        play_s("ded")
            self.rect.clamp_ip(self.container)

            '''if self.rect.x <= 0:
                self.rect.x = 0
            elif self.rect.x >= win_w - self.size:
                self.rect.x = win_w - self.size
            if self.rect.y <= 0:
                self.rect.y = 0
            elif self.rect.y >= win_h - self.size:
                self.rect.y = win_h - self.size'''

        def dead_update(self, gametime):
            self.image = pygame.transform.rotate(pygame.transform.scale(
                Image("ex_" + str(int(gametime / 3) % 4 + 1), 0, 0).image,
                (self.size * 5, self.size * 5)), random.randrange(4) * 90)

    class Camera:
        def __init__(self):
            self.x = 0
            self.y = 0

        def apply(self, obj):
            return pygame.Rect(obj.rect.x + self.x,
                               obj.rect.y,
                               obj.rect.width, obj.rect.height)

        def update(self, ship):
            self.x = -ship.rect.x + win_w / 4 + ship.size
            if self.x >= 0:
                self.x = 0
            elif self.x <= -200:
                self.x = -200

    class Flash:
        def __init__(self):
            self.rect = pygame.Rect(0, 0, win_w, win_h)
            self.image = pygame.Surface((win_w, win_h))
            self.brightness = 1
            self.color = white

        def update(self):
            self.brightness -= 1
            if self.brightness >= 0:
                self.image.fill((self.color[0], self.color[1], self.color[2]))
                self.image.set_alpha(self.brightness)

        def action(self, color):
            self.color = color
            self.brightness = 50


    # initialize
    pygame.init()
    fps = 60
    clock = pygame.time.Clock()
    play = False
    pygame.display.set_caption("crystalcaves")
    screen = pygame.display.set_mode((win_w, win_h), pygame.SRCALPHA)
    camera = Camera()

    # more initializing that could be changed
    container = pygame.Rect(0, 0, win_w, win_h)
    ship = Image("ship3", 0, 0)
    ship.image = pygame.transform.scale(ship.image, (36, 48))
    pl = Ship(16, 1, container, ship.image)

    # MAP LAYOUT UNUSED
    '''x = -win_w/4 - pl.size
    y = -win_h/4 - pl.size
    # platform_group = pygame.sprite.Group()

    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]

    # create objects

    for row in level:
        for col in row:
            if col == "P":
                platform_group.add(Platform(x, y))
            x += 32
        y += 32
        x = -win_w/4 - pl.size'''

    # background creation
    bg = Image("bg_light", 0, 0)
    transform_dim = 32 ** 2 / 1.4 / bg.image.get_width()
    bg.image = pygame.transform.scale(bg.image, (32 ** 2 / 1.4, bg.rect.h * transform_dim))
    bg.rect.topleft = 0, -bg.image.get_height() + win_h * 2

    title = Image("bg_cave", 0, 0)
    help_sc = Image("how2play", 0, 0)

    the_font = pygame.font.Font("raiden/ConnectionII.ttf", 25)
    text = the_font.render("press any key to begin", False, black)
    text_rect = text.get_rect()
    text_rect = text_rect.move(win_w / 2 - text_rect.width / 2, win_h / 1.5)

    info = the_font.render("or click for info", False, black)
    info_rect = info.get_rect()
    info_rect = info_rect.move(win_w / 2 - info_rect.width / 2, win_h / 1.5 + 50)

    l = the_font.render("you lost", False, white)
    l_rect = l.get_rect()
    l_rect = l_rect.move(win_w / 2 - l_rect.width / 2, win_h / 3)
    dummy = 0
    dummy_rect = 0

    overlay = Flash()

    bul_g = pygame.sprite.Group()
    enemy_g = pygame.sprite.Group()
    upgrade_g = pygame.sprite.Group()

    gametime = 0

    # title loop
    loop_count = 0
    display_help = False

    while not play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                else:
                    play = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                display_help = True
        if display_help:
            screen.blit(help_sc.image, help_sc.rect)
        else:
            screen.blit(title.image, title.rect)
            if loop_count % 100 < 50:
                screen.blit(text, text_rect)
                screen.blit(info, info_rect)
        loop_count += 1
        pygame.display.flip()

    play_s("main_theme")

    # game loop
    while play:
        # read input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: sys.exit()
                # if event.key == pygame.K_1: pl.upgrade = 1
                # if event.key == pygame.K_2: pl.upgrade = 2
                # if event.key == pygame.K_3: pl.upgrade = 3
        # update
        if not pl.dead:
            if pl.speed < pl.speed_cap:
                pl.speed += 0.01

            if int(random.randrange(75)) == 25:
                enemy_g.add(Enemy(int(random.randrange(3) + 3), "crystal"))
            if int(random.randrange(75)) == 25:
                enemy_g.add(Enemy(2, "bat"))

            enemy_g.update(gametime)
            bul_g.update(enemy_g, bul_g, camera, upgrade_g, pl)
            upgrade_g.update(pl, upgrade_g, overlay)

            pl.update(bul_g, enemy_g, camera, overlay, gametime)
            pl.score_counter.update(pl)
            camera.update(pl)
            overlay.update()
            # scrolls and drawing

            for i in upgrade_g:
                scroll(i.rect, sc_scroll)

            scroll(bg.rect, sc_scroll)
            screen.fill(white)
            screen.blit(bg.image, camera.apply(bg))
            # for p in platform_group:
            #     screen.blit(p.image, camera.apply(p))

            bul_g.draw(screen)
            upgrade_g.draw(screen)

            for i in enemy_g:
                if i.type == "crystal":
                    screen.blit(i.image, camera.apply(i))
                else:
                    screen.blit(i.image, i.rect)
            screen.blit(pl.image, pl.rect)
            screen.blit(pl.score_counter.bg_image, pl.score_counter.bg_rect)
            screen.blit(pl.score_counter.text_img, pl.score_counter.text_rect)
            pl.health.draw(screen)

            screen.blit(overlay.image, overlay.rect)
        else:
            if dummy == 0:
                dummy = the_font.render("Score: " + str(pl.score), False, white)
                dummy_rect = dummy.get_rect()
                dummy_rect = dummy_rect.move(win_w / 2 - dummy_rect.width / 2, win_h / 3 + win_h / 6)
            pl.dead_update(gametime)
            screen.blit(bg.image, camera.apply(bg))
            screen.blit(pl.image, pl.rect)
            screen.blit(l, l_rect)
            screen.blit(dummy, dummy_rect)
            if gametime - pl.i_frames >= 200:
                sys.exit()

        gametime += 1

        clock.tick(fps)

        pygame.display.flip()

        if gametime >= 2900:
            play = False
            gametime = 0

    the_font = pygame.font.Font("raiden/ConnectionII.ttf", 75)
    counted = 0
    pygame.mixer.pause()
    play_s("winner")

    while not play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: sys.exit()
        pl.rect.y -= 5
        screen.blit(bg.image, camera.apply(bg))
        screen.blit(pl.image, pl.rect)

        clock.tick(fps)
        gametime += 1
        pygame.display.flip()

        if gametime >= 150:
            play = True
    for _ in pl.health:
        pl.score += 100000
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: sys.exit()
        score_img = the_font.render("Score: " + str(counted), False, white)
        score_rect = score_img.get_rect()
        score_rect = score_rect.move(win_w / 2 - score_rect.width / 2, win_h / 1.5)

        if counted < pl.score:
            counted += random.randrange(100, 2500)
            if counted > pl.score:
                counted = pl.score

        if gametime >= 150:
            play_s("ping")

        screen.blit(bg.image, camera.apply(bg))
        screen.blit(score_img, score_rect)

        clock.tick(fps)
        gametime += 1
        pygame.display.flip()

        if counted == pl.score and gametime >= 150:
            gametime = 0
            play_s("finished")
        if counted == pl.score and gametime >= 100:
            play = False


def music():
    import pygame, sys, random, time

    win_w = 1080
    win_h = 720

    white = (255, 255, 255)

    '''
    NOTES:

        bpms:
            redwood 90 to 140 ???
            success 99ish
            party 138
            test me 142
    '''

    def play_s(sound):
        pygame.mixer.Sound("music/other_sounds/" + sound + ".mp3").play()

    def play_song(sound):
        pygame.mixer.Sound("music/songs/" + sound + ".mp3").play()

    # where settings are stored

    class Settings:
        def __init__(self):
            self.level = 1
            self.font = ""

    class NoteTiming(pygame.sprite.Sprite):
        def __init__(self, letter):
            pygame.sprite.Sprite.__init__(self)
            self.time_left = 64
            self.l = letter
            self.image = Image("letters/" + str(letter), 0, 0).image
            self.rect = pygame.Rect(win_w, int(win_h / 2) - int(self.image.get_height() / 2), 75, 75)
            self.rect.x = win_w
            self.rect.y = int(win_h / 2) - int(self.rect.height / 2) - win_w / 8

        def update(self):
            self.rect.x -= 16
            self.time_left -= 1

    class Image:
        def __init__(self, image, x, y):
            self.image = pygame.image.load("music/" + image + ".png")
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y

    class Counter(pygame.sprite.Sprite):
        def __init__(self, y):
            pygame.sprite.Sprite.__init__(self)
            self.text_img = pygame.font.Font("music/Aeros.ttf", 100).render("0", True, white)
            self.text_rect = self.text_img.get_rect()
            self.text_rect = self.text_rect.move(win_w / 16, y)
            self.counter = 0
            self.hype = 0
            self.y = y

        def update(self):
            self.text_img = pygame.font.Font("music/Aeros.ttf", 100 + self.hype).render(str(self.counter), True, white)
            self.text_rect = self.text_img.get_rect()
            self.text_rect = self.text_rect.move(win_w / 16, self.y)

    # the variable that holds map layout

    class Map:
        def __init__(self, charting):
            self.layout = ""
            self.charting = charting
            if self.charting == "test_me":
                self.layout = "" \
                              "0000000a000000000000000000000000" \
                              "0000000000000000000000000" \
                              "l00000000000l000000000000" \
                              "00000000000000000000000000" \
                              "a000000000000000000000000" \
                              "l000000000000000000000000" \
                              "a000000000000000000000000" \
                              "l000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "0000000000000000000000000" \
                              "l00000000000l000000000000" \
                              "0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "l000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "l000000000000000000000000" \
                              "a000000000000000000000000" \
                              "0000000000000000000000000" \
                              "l00000000000l000000000000" \
                              "00000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "l0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "l000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "0000000000000000000000000" \
                              "l00000000000l000000000000" \
                              "0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "00000000000000000000000000" \
                              "0000000000000000000000000" \
                              "0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "l000000000000000000000000" \
                              "l00000000000l0000000000000" \
                              "0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "l000000000000000000000000" \
                              "a000000000000000000000000" \
                              "l0000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "l0000000000000000000000000" \
                              "l00000000000l000000000000" \
                              "0000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "l000000000000000000000000" \
                              "a000000000000000000000000" \
                              "l000000000000000000000000" \
                              "a000000000000000000000000" \
                              "00000000000000000000000000" \
                              "l00000000000l000000000000" \
                              "0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "l000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "l000000000000000000000000" \
                              "a000000000000000000000000" \
                              "0000000000000000000000000" \
                              "l00000000000l000000000000" \
                              "00000000000000000000000000" \
                              "a00000000000000000000000000" \
                              "00000000000000000000000000" \
                              "0000000000000000000000000" \
                              "0000000000000000000000000" \
                              "00000000000000000000000000" \
                              "l00000000000l000000000000" \
                              "l000000000000000000000000" \
                              "k000000000000000000000000" \
                              "k00000000000000000j0000000" \
                              "k00000000000l000000000000" \
                              "l000000000000000000000000" \
                              "0000000000000000000000000" \
                              "0000000000000000000000000" \
                              "d00000000000000000000000000" \
                              "d000000000000000000000000" \
                              "s0000000000000000000000000" \
                              "s00000000000000000a000000" \
                              "s00000000000d0000000000000" \
                              "d000000000000000000000000" \
                              "0000000000000000000000000" \
                              "00000000000000000000000000" \
                              "l00000000000l00000000000000" \
                              "l000000000000000000000000" \
                              "k0000000000000000000000000" \
                              "k00000000000000000j000000" \
                              "k00000000000l000000000000" \
                              "l0000000000000000000000000" \
                              "0000000000000000000000000" \
                              "0000000000000000000000000" \
                              "d0000000000000000000000000" \
                              "d000000000000000000000000" \
                              "s000000000000000000000000" \
                              "s00000000000000000a000000" \
                              "s00000000000d000000000000" \
                              "d0000000000000000000000000" \
                              "0000000000000000000000000" \
                              "000000000000l000000000000" \
                              "l00000000000l0000000000000" \
                              "k000000000000000000000000" \
                              "j0000000000000000000000000" \
                              "j00000000000000000d00000000" \
                              "s00000000000a000000000000" \
                              "a000000000000000000000000" \
                              "0000000000000000000000000" \
                              "000000000000a000000000000" \
                              "a00000000000a000000000000" \
                              "s000000000000000000000000" \
                              "d000000000000000000000000" \
                              "d00000000000000000j0000000" \
                              "k00000000000l00000000000000" \
                              "l000000000000000000000000" \
                              "0000000000000000000000000" \
                              "0000000000000000000000000" \
                              "l000000000000000000000000" \
                              "l000000000000000000000000" \
                              "k000000000000000000000000" \
                              "k00000000000000000j0000000" \
                              "k00000000000l000000000000" \
                              "l000000000000000000000000" \
                              "0000000000000000000000000" \
                              "0000000000000000000000000" \
                              "d00000000000000000000000000" \
                              "d000000000000000000000000" \
                              "s000000000000000000000000" \
                              "s00000000000000000a000000" \
                              "s00000000000d0000000000000" \
                              "d000000000000000000000000" \
                              "0000000000000000000000000" \
                              "000000000000l000000000000" \
                              "0000000000000000000000000" \
                              "k0000000000000000000000000" \
                              "j0000000000000000000000000" \
                              "j000000000000000000000000" \
                              "000000000000000000k000000" \
                              "l000000000000000000000000" \
                              " 000000000000000000000000" \
                              " 00000000000a000000000000" \
                              "0000000000000000000000000" \
                              "s0000000000000000000000000" \
                              "s0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "000000000000s000000000000" \
                              "d00000000000s000000000000" \
                              "a000000000000000000000000" \
                              " 00000000000l000000000000" \
                              "0000000000000000000000000" \
                              "k0000000000000000000000000" \
                              "j00000000000000000000000000" \
                              "j000000000000000000000000" \
                              "000000000000000000k000000" \
                              "l000000000000000000000000" \
                              " 000000000000000000000000" \
                              " 00000000000a000000000000" \
                              "0000000000000000000000000" \
                              "s0000000000000000000000000" \
                              "s0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "000000000000s000000000000" \
                              "d00000000000s000000000000" \
                              "a000000000000000000000000" \
                              " 0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "s000000000000000000000000" \
                              "d000000000000000000000000" \
                              "f000000000000000000000000" \
                              "g0000000000000000000000000" \
                              "h000000000000000000000000" \
                              " 0000000000000000000000000" \
                              " 000000000000000000000000" \
                              "l000000000000000000000000" \
                              "k0000000000000000000000000" \
                              "j000000000000000000000000" \
                              "h000000000000000000000000" \
                              "g000000000000000000000000" \
                              "f000000000000000000000000" \
                              " 0000000000000000000000000" \
                              " 000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a00000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a00000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a000000000000000000000000" \
                              "a00000000000000000000000000" \
                              "a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

            elif self.charting == "s5":
                self.layout = "0000000" \
                              " 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "0000000000000000000000000000000000000000000000000000000000z000000000000000000000z000000000000000000000p" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "0000000000000000000000000000000000000000000000000000 00000000000000000000000000000000000000000000000000" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "r0000000000e00000000000" \
                              "00000000000r00000000000" \
                              "e0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "p0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "r0000000000e00000000000" \
                              "00000000000r00000000000" \
                              "e0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "m0000000000n00000000000" \
                              "b0000000000000000000000" \
                              "l0000000000000000000000" \
                              "r0000000000e00000000000" \
                              "00000000000r00000000000" \
                              "e0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "p0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "r0000000000e00000000000" \
                              "00000000000r00000000000" \
                              "e0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "m0000000000n00000000000" \
                              "b0000000000000000000000" \
                              "l0000000000000000000000" \
                              "r0000000000e00000000000" \
                              "00000000000r00000000000" \
                              "e0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "p0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "r0000000000e00000000000" \
                              "00000000000r00000000000" \
                              "e0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "m0000000000n00000000000" \
                              "b0000000000000000000000" \
                              "l0000000000000000000000" \
                              "r0000000000e00000000000" \
                              "00000000000r00000000000" \
                              "e0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "p0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "r0000000000e00000000000" \
                              "00000000000r00000000000" \
                              "e0000000000000000000000" \
                              "a0000000000000000000000" \
                              "l0000000000000000000000" \
                              "m0000000000n00000000000" \
                              " 0000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "a0000000000000000000000" \
                              "00000000000000000000000" \
                              "s0000000000500000000000" \
                              "00000000000000000000000" \
                              "s0000000000500000000000" \
                              "00000000000000000000000" \
                              "s0000000000500000000000" \
                              "00000000000000000000000" \
                              "s0000000000500000000000" \
                              "00000000000000000000000" \
                              "s0000000000500000000000" \
                              "000000000000000000000000" \
                              "s0000000000500000000000" \
                              "00000000000000000000000" \
                              "s0000000000500000000000" \
                              "00000000000000000000000" \
                              "s0000000000500000000000000" \
                              " 0000000000000000000000" \
                              "q0000q00000000000000000" \
                              " 0000000000q00000000000" \
                              "p0000000000000000000000" \
                              "00000000000q000000000000" \
                              "p0000000000000000000000" \
                              " 0000000000p00000000000" \
                              " 0000000000000000000000" \
                              "00000000000q00000000000" \
                              "q0000000000000000000000" \
                              " 0000000000q00000000000" \
                              "p0000000000000000000000" \
                              "00000000000q00000000000" \
                              "p0000000000000000000000" \
                              " 0000000000q000000000000" \
                              " 0000000000000000000000" \
                              "00000000000000000000000" \
                              " 0000000000000000000000" \
                              "a0000000000000000000000" \
                              "00000000000000000000000" \
                              "00000000000l00000000000" \
                              "a0000000000000000000000" \
                              "00000000000l00000000000" \
                              "a0000000000000000000000" \
                              "000000000000000000000000" \
                              "00000000000000000000000" \
                              " 0000000000000000000000" \
                              "a0000000000000000000000" \
                              "00000000000l00000000000" \
                              "a00000000000000000000000" \
                              "00000000000 00000000000" \
                              "a0000000000 00000000000" \
                              "10000000000200000000000" \
                              "30000000000400000000000" \
                              " 00000000000000000000000" \
                              "q0000000000000000000000" \
                              "00000000000p00000000000" \
                              "q0000000000000000000000" \
                              "p0000000000 00000000000" \
                              "p00000000000000000000000" \
                              "00000000000q00000000000" \
                              "q0000000000000000000000" \
                              "q0000000000 00000000000" \
                              "p0000000000000000000000" \
                              "00000000000q000000000000" \
                              "q0000000000000000000000" \
                              " 0000000000p00000000000" \
                              " 0000000000000000000000" \
                              "10000000000000000000000" \
                              "a00000000000000000000000" \
                              "00000000000l00000000000" \
                              "l0000000000000000000000" \
                              "00000000000l00000000000" \
                              "l0000000000000000000000" \
                              "00000000000l000000000000" \
                              "l0000000000000000000000" \
                              "00000000000l00000000000" \
                              "l0000000000000000000000" \
                              "00000000000l00000000000" \
                              "l00000000000000000000000" \
                              "00000000000l00000000000" \
                              "l0000000000000000000000" \
                              "00000000000l00000000000" \
                              "l0000000000000000000000" \
                              "00000000000000000000000" \
                              "00000000000000000000000" \
                              "00000000000000000000000" \
                              "00000000000000000000000" \
                              "00000000000000000000000" \
                              "00000000000000000000000"

            elif self.charting == "redwood":
                self.layout = "00000030000000002000001000" \
                              "000000300000000020000010000" \
                              "00000030000000002000001000" \
                              "000000300000000020000010000" \
                              "00000030000000002000001000" \
                              "000000300000000020000010000" \
                              "00000030000000002000001000" \
                              "000000300000000020000010000" \
                              "00000030000000002000001000" \
                              "000000300000000020000010000" \
                              "00000030000000002000001000" \
                              "000000300000000020000010000" \
                              "00000030000000002000001000" \
                              "000000300000000020000010000" \
                              "00000030000000002000001000" \
                              "00000030000000002000001000" \
                              "00000030000000002000001000" \
                              "00000030000000002000001000" \
                              "00000030000000002000001000"

            elif self.charting == "party":
                self.layout = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                              "p00000000000000000o0000000" \
                              "000000000000o0000000000000" \
                              "000000000000o0000000000000" \
                              "i00000000000o0000000000000" \
                              "p00000000000000000o0000000" \
                              "000000000000o0000000000000" \
                              "000000000000o0000000000000" \
                              "i00000000000o0000000000000" \
                              "p00000000000000000o0000000" \
                              "000000000000o0000000000000" \
                              "000000000000o0000000000000" \
                              "i00000000000o0000000000000" \
                              "p0000000000000000000000000" \
                              "00000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "00000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "00000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "00000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "q0000000000000000000000000" \
                              "o0000000000000000000000000" \
                              "w0000000000000000000000000" \
                              "p00000000000a0000000000000" \
                              "p00000000000a0000000000000" \
                              "p00000000000a0000000000000" \
                              "p00000000000a0000000000000" \
                              "p00000000000a0000000000000" \
                              "p00000000000a0000000000000" \
                              "p00000000000a0000000000000" \
                              "p00000000000a0000000000000" \
                              "p00000000000a0000000000000" \
                              "o00000000000a0000000000000" \
                              "i00000000000a0000000000000" \
                              "u00000000000a0000000000000" \
                              "y00000000000a0000000000000" \
                              "t00000000000a0000000000000" \
                              "r00000000000a0000000000000" \
                              "e00000000000a0000000000000" \
                              "l00000000000q0000000000000" \
                              "l00000000000q0000000000000" \
                              "l00000000000q0000000000000" \
                              "l00000000000q0000000000000" \
                              "l00000000000q0000000000000" \
                              "l00000000000q0000000000000" \
                              "l00000000000q0000000000000" \
                              "l00000000000q0000000000000" \
                              "l00000000000q0000000000000" \
                              "l00000000000w0000000000000" \
                              "l00000000000e0000000000000" \
                              "l00000000000r0000000000000" \
                              "l00000000000t0000000000000" \
                              "l00000000000y0000000000000" \
                              "l00000000000u0000000000000" \
                              "l00000000000i000000000000" \
                              "l00000000000a0000000000000" \
                              "l00000a0000000000000000000" \
                              "l00000000000l0000000000000" \
                              "a00000000000a0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q000000000000" \
                              "l00000000000a0000000000000" \
                              "l00000a0000000000000000000" \
                              "l00000000000l0000000000000" \
                              "a00000000000a0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q000000000000" \
                              "l00000000000a0000000000000" \
                              "l00000a0000000000000000000" \
                              "l00000000000l0000000000000" \
                              "a00000000000a0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "l00000000000a0000000000000" \
                              "l00000a0000000000000000000" \
                              "l00000000000l0000000000000" \
                              "a00000000000a0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "s00000000000s0000000000000" \
                              "d00000d0000000000000000000" \
                              "000000j00000j000000j00000" \
                              "k00000000000k0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "s00000000000s0000000000000" \
                              "d00000d0000000000000000000" \
                              "000000j00000j000000j000000" \
                              "k00000000000k0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "s00000000000s0000000000000" \
                              "d00000d0000000000000000000" \
                              "000000j00000j000000j000000" \
                              "k00000000000k0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "s00000000000s0000000000000" \
                              "d00000d0000000000000000000" \
                              "000000j00000j000000j00000" \
                              "k00000000000k0000000000000" \
                              "p00000000000q000000p000000" \
                              "000000000000q0000000000000" \
                              "p0000000000000000000000000" \
                              "q0000000000000000000000000" \
                              "q0000000000000000000000000" \
                              "w0000000000000000000000000" \
                              "e00000000000r0000000000000" \
                              "t00000000000y0000000000000" \
                              "u000000000000000000i000000" \
                              "000000o0000000000000000000" \
                              "00000000000000000000000000" \
                              "00000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "s0000000000000000000000000" \
                              "d00000000000f0000000000000" \
                              "g00000000000h0000000000000" \
                              "j000000000000000000k000000" \
                              "000000l0000000000000000000" \
                              "00000000000000000000000000" \
                              "0000000000000000000000000" \
                              "q0000000000000000000000000" \
                              "w0000000000000000000000000" \
                              "e00000000000r0000000000000" \
                              "t00000000000y0000000000000" \
                              "u000000000000000000i000000" \
                              "000000o0000000000000000000" \
                              "00000000000000000000000000" \
                              "00000000000000000000000000" \
                              "a0000000000000000000000000" \
                              "s0000000000000000000000000" \
                              "d00000000000f0000000000000" \
                              "g00000000000h0000000000000" \
                              "j000000000000000000k000000" \
                              "000000l0000000000000000000" \
                              "00000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "p00000000000g0000000000000" \
                              "p00000000000g0000000000000" \
                              "o00000000000g0000000000000" \
                              "o00000000000g00000000000000" \
                              "i00000000000g0000000000000" \
                              "i00000000000g0000000000000" \
                              "i00000000000g0000000000000" \
                              "i00000000000g0000000000000" \
                              "i0000000000000000000p00000" \
                              "000000000000o0000000000000" \
                              "i00000000000o0000000000000" \
                              "p0000000000000000000000000" \
                              "00000000000000000000000000" \
                              "00000000000000000000000000" \
                              "000000000000000000000000000" \
                              "q0000000000000000000000000" \
                              "q00000000000g0000000000000" \
                              "q00000000000g0000000000000" \
                              "w00000000000g0000000000000" \
                              "w00000000000g0000000000000" \
                              "e00000000000g0000000000000" \
                              "e00000000000g0000000000000" \
                              "e00000000000g0000000000000" \
                              "e00000000000g0000000000000" \
                              "e0000000000000000000e000000" \
                              "000000000000w0000000000000" \
                              "q00000000000w0000000000000" \
                              "e0000000000000000000000000" \
                              "w0000000000000000000000000" \
                              "w0000000000000000000000000" \
                              "w0000000000000000000000000" \
                              "w0000000000000000000000000" \
                              "s00000000000s0000000000000" \
                              "d00000d000000000000j000000" \
                              "000000j00000j000000j000000" \
                              "k0000000000000000000000000" \
                              "s00000000000s0000000000000" \
                              "d00000d000000000000j0000000" \
                              "000000j00000j000000j000000" \
                              "k0000000000000000000000000" \
                              "s00000000000s0000000000000" \
                              "d0000000000000000000000000" \
                              "000000j00000j000000j000000" \
                              "k0000000000000000000000000" \
                              "o0000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "p00000000000o0000000000000" \
                              "i00000000000o00000000000000" \
                              "p0000000000000000000000000" \
                              "00000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "00000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "00000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "00000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "p0000000000000000000000000" \
                              "p00000000000000000000000000" \
                              "l00000000000a0000000000000" \
                              "l00000a0000000000000000000" \
                              "l00000000000l0000000000000" \
                              "a00000000000a0000000000000" \
                              "a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

    class Fill(pygame.sprite.Sprite):
        def __init__(self, l):
            pygame.sprite.Sprite.__init__(self)
            self.x = self.y = 0
            self.size = 36
            if l == "1":
                self.x = 312
                self.y = 383
            if l == "2":
                self.x = 359
                self.y = 383
            if l == "3":
                self.x = 406
                self.y = 383
            if l == "4":
                self.x = 454
                self.y = 383
            if l == "5":
                self.x = 500
                self.y = 383
            if l == "6":
                self.x = 547
                self.y = 383
            if l == "7":
                self.x = 594
                self.y = 383
            if l == "8":
                self.x = 641
                self.y = 383
            if l == "9":
                self.x = 688
                self.y = 383
            if l == "q":
                self.x = 336
                self.y = 429
            if l == "w":
                self.x = 383
                self.y = 429
            if l == "e":
                self.x = 430
                self.y = 429
            if l == "r":
                self.x = 478
                self.y = 429
            if l == "t":
                self.x = 524
                self.y = 429
            if l == "y":
                self.x = 571
                self.y = 429
            if l == "u":
                self.x = 618
                self.y = 429
            if l == "i":
                self.x = 665
                self.y = 429
            if l == "o":
                self.x = 712
                self.y = 429
            if l == "p":
                self.x = 759
                self.y = 429
            if l == "a":
                self.x = 348
                self.y = 474
            if l == "s":
                self.x = 395
                self.y = 474
            if l == "d":
                self.x = 442
                self.y = 474
            if l == "f":
                self.x = 489
                self.y = 474
            if l == "g":
                self.x = 536
                self.y = 474
            if l == "h":
                self.x = 583
                self.y = 474
            if l == "j":
                self.x = 630
                self.y = 474
            if l == "k":
                self.x = 677
                self.y = 474
            if l == "l":
                self.x = 724
                self.y = 474
            if l == "z":
                self.x = 371
                self.y = 521
            if l == "x":
                self.x = 418
                self.y = 521
            if l == "c":
                self.x = 465
                self.y = 521
            if l == "v":
                self.x = 512
                self.y = 521
            if l == "b":
                self.x = 559
                self.y = 521
            if l == "n":
                self.x = 606
                self.y = 521
            if l == "m":
                self.x = 653
                self.y = 521
            if l == " ":
                self.x = 464
                self.y = 569
                self.size = 225
            self.image = pygame.Surface((self.size, 36))
            self.rect = pygame.Rect(self.x, self.y, self.size, 36)
            self.transparency = 2
            self.uptime = 0
            self.image.fill((255, 255, 255))

        def update(self, fill_group):
            self.uptime += 1
            if self.transparency <= 255 and self.uptime < 70:
                self.transparency = self.transparency ** 1.034
                self.image.set_alpha(self.transparency)
            else:
                self.transparency = self.transparency ** 0.5
                if self.transparency <= 14:
                    fill_group.remove(self)

    # main ofc


    # initialize
    pygame.init()
    # fps = 58.82353415
    fps = 60
    # fps = 59
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((win_w, win_h), pygame.SRCALPHA)
    gametime = 0

    note_timings = pygame.sprite.Group()
    fill_group = pygame.sprite.Group()

    play = False

    brightness = 0
    screen_flash = pygame.Surface((win_w, win_h))
    screen_flash.set_alpha(0)
    screen_flash.fill((255, 255, 255))

    settings = Settings()

    acc = 0
    title = Counter(int(win_h / (5 / 4)))

    # background creation
    bg = Image("menu", 0, 0)
    # keyboard = Image("board", 0, 0)

    play_song("menu")

    while not play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 980 > pos[0] > 900 and 100 < pos[1] < 292:
                    acc += 1
                elif 665 < pos[0] < 745 and 100 < pos[1] < 292:
                    acc -= 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    play = True
                    pygame.mixer.stop()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    acc -= 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    acc += 1

        if gametime == 1700:
            play_song("menu")
            gametime = 0

        if acc % 5 == 0:
            title.counter = "test_me"
        elif acc % 5 == 1:
            title.counter = "success"
        elif acc % 5 == 2:
            title.counter = "s5"
        elif acc % 5 == 3:
            title.counter = "redwood"
        elif acc % 5 == 4:
            title.counter = "party"

        title.update()

        screen.blit(bg.image, bg.rect)
        screen.blit(title.text_img, title.text_rect)

        gametime += 1
        clock.tick(fps)
        pygame.display.flip()

    # background creation
    bg = Image("compressed_bg", 0, 0)

    song_choice = Map(title.counter)

    combo = Counter(0)
    gametime = 0

    for i in song_choice.layout:
        keypressed = ""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    keypressed = "q"
                elif event.key == pygame.K_w:
                    keypressed = "w"
                elif event.key == pygame.K_e:
                    keypressed = "e"
                elif event.key == pygame.K_r:
                    keypressed = "r"
                elif event.key == pygame.K_t:
                    keypressed = "t"
                elif event.key == pygame.K_y:
                    keypressed = "y"
                elif event.key == pygame.K_u:
                    keypressed = "u"
                elif event.key == pygame.K_i:
                    keypressed = "i"
                elif event.key == pygame.K_o:
                    keypressed = "o"
                elif event.key == pygame.K_p:
                    keypressed = "p"
                elif event.key == pygame.K_a:
                    keypressed = "a"
                elif event.key == pygame.K_s:
                    keypressed = "s"
                elif event.key == pygame.K_d:
                    keypressed = "d"
                elif event.key == pygame.K_f:
                    keypressed = "f"
                elif event.key == pygame.K_g:
                    keypressed = "g"
                elif event.key == pygame.K_h:
                    keypressed = "h"
                elif event.key == pygame.K_j:
                    keypressed = "j"
                elif event.key == pygame.K_k:
                    keypressed = "k"
                elif event.key == pygame.K_l:
                    keypressed = "l"
                elif event.key == pygame.K_z:
                    keypressed = "z"
                elif event.key == pygame.K_x:
                    keypressed = "x"
                elif event.key == pygame.K_c:
                    keypressed = "c"
                elif event.key == pygame.K_v:
                    keypressed = "v"
                elif event.key == pygame.K_b:
                    keypressed = "b"
                elif event.key == pygame.K_n:
                    keypressed = "n"
                elif event.key == pygame.K_m:
                    keypressed = "m"
                elif event.key == pygame.K_SPACE:
                    keypressed = "space"
                elif event.key == pygame.K_1:
                    keypressed = "1"
                elif event.key == pygame.K_2:
                    keypressed = "2"
                elif event.key == pygame.K_3:
                    keypressed = "3"
                elif event.key == pygame.K_4:
                    keypressed = "4"
                elif event.key == pygame.K_5:
                    keypressed = "5"
                elif event.key == pygame.K_6:
                    keypressed = "6"
                elif event.key == pygame.K_7:
                    keypressed = "7"
                elif event.key == pygame.K_8:
                    keypressed = "8"
                elif event.key == pygame.K_9:
                    keypressed = "9"

        # note updates
        if gametime == 70:
            play_song(song_choice.charting)

        if i != "0":
            if i != " ":
                note_timings.add(NoteTiming(i))
            else:
                note_timings.add(NoteTiming("space"))
            fill_group.add(Fill(i))

        screen.fill((0, 0, 0))
        fill_group.update(fill_group)
        for j in fill_group:
            screen.blit(j.image, j.rect)
        screen.blit(bg.image, (0, 27))

        for j in note_timings:
            if keypressed == j.l and j.time_left <= 10:
                note_timings.remove(j)
                fill_group.remove()
                brightness = 30
                combo.counter += 1
                if combo.counter < 25:
                    combo.hype = 6
                elif combo.counter < 50:
                    combo.hype = 12
                elif combo.counter < 50:
                    combo.hype = 18
                else:
                    combo.hype = 30
                break

            elif j.time_left < -10:
                note_timings.remove(j)
                fill_group.remove()
                combo.counter = 0

            elif keypressed != "":
                combo.counter = 0

            j.update()

        combo.update()

        # blitting and finishing
        note_timings.draw(screen)

        screen.blit(combo.text_img, combo.text_rect)
        # screen.blit(keyboard.image, keyboard.rect)
        # screen_flash.set_alpha(brightness)
        # screen.blit(screen_flash, (0, 0))

        if brightness > 0:
            brightness -= 3
        if combo.hype > 0:
            combo.hype -= 3
        gametime += 1
        clock.tick(fps)
        pygame.display.flip()


def simplism():
    import pygame
    import sys
    import math
    import time

    class Lines:
        def __init__(self, rect):
            self.top_line = ((rect.x, rect.y), (rect.x + rect.width, rect.y))
            self.bottom_line = ((rect.x, rect.y + rect.height), (rect.x + rect.width, rect.y + rect.height))
            self.left_line = ((rect.x, rect.y), (rect.x, rect.y + rect.height))
            self.right_line = ((rect.x + rect.width, rect.y), (rect.x + rect.width, rect.y + rect.height))

    class Camera:
        def __init__(self):
            self.x_offset = 0
            self.y_offset = 0
            self.max_x = 0
            self.max_y = 0

        def new_level(self, level_size):
            self.x_offset = 0
            self.y_offset = -level_size[1]

        def update(self, ball):
            if ball.x < 400 and self.x_offset > -100:
                self.x_offset -= (400 - ball.x)
                ball.x = 400
            elif ball.x > WIN_W - 400 and self.x_offset < self.max_x:
                self.x_offset -= WIN_W - 400 - ball.x
                ball.x = WIN_W - 400
            if ball.y < 400 and self.y_offset > 0:
                self.y_offset -= (400 - ball.y)
                ball.y = 400
            elif ball.y > WIN_H - 400 and self.y_offset < self.max_y:
                self.y_offset -= WIN_H - 400 - ball.y
                ball.y = WIN_H - 400

            if self.y_offset > self.max_y:
                self.y_offset = self.max_y
            if self.x_offset > self.max_x:
                self.x_offset = self.max_x
            if self.x_offset < -400:
                self.x_offset = -400
            if self.y_offset < 0:
                self.y_offset = 0

    class HitBox(pygame.sprite.Sprite):
        def __init__(self, width, height, location, kind):
            pygame.sprite.Sprite.__init__(self)
            self.width = width
            self.height = height
            self.x = location[0]
            self.y = location[1]
            self.image = pygame.Surface((width, height))
            self.rect = pygame.Rect(self.x, self.y, width, height)
            self.lines = Lines(self.rect)
            self.hit_rect = self.rect
            self.kind = kind

            if kind == "hurt":
                self.image.fill((255, 100, 100))
            elif kind == "click":
                self.image.fill((200, 255, 200))

        def update(self, camera):
            self.hit_rect = pygame.Rect(self.x - camera.x_offset, self.y - camera.y_offset, self.width, self.height)
            self.lines = Lines(self.hit_rect)

    class Level:
        def __init__(self, layout, sizes, title):
            self.layout = layout
            self.sizes = sizes
            self.name = title[1].render(title[0], True, (0, 0, 0))
            '''
            velo_text = debug_font.render(str(int(scrunkly)) + ":" + str(int(scrunkly*100)-int(scrunkly)*100),
                                          True, (255, 255, 255))'''

        def spawn(self, camera):
            camera.max_x = self.sizes[0]
            camera.max_y = self.sizes[1]

    class Hints:
        def __init__(self, font):
            self.things = []
            self.font = font
            self.texts = self.font.render("what help would you need here?", True, (255, 255, 255))
            self.text_loc = (WIN_W - self.texts.get_width(), 0)

        def new_level(self):
            if LEVEL == 2:
                self.things = []
                self.texts = self.font.render("i guess you like easter eggs", True, (255, 255, 255))
                self.text_loc = (WIN_W - self.texts.get_width(), 0)
            if LEVEL == 3:
                self.things = []
                self.texts = self.font.render("well congrats on finding me!", True, (255, 255, 255))
                self.text_loc = (WIN_W - self.texts.get_width(), 0)
            if LEVEL == 4:
                self.things = []
                self.texts = self.font.render("sorry but this is where these end", True, (255, 255, 255))
                self.text_loc = (WIN_W - self.texts.get_width(), 0)
            if LEVEL == 5:
                self.things = [(200, 750)]
                self.texts = self.font.render("shorter clicks are faster", True, (0, 0, 0))
                self.text_loc = (0, WIN_H - self.texts.get_height())
            if LEVEL == 6:
                self.things = [(2025, 1100), (1575, 100)]
                self.texts = self.font.render("and longer clicks are slower", True, (0, 0, 0))
                self.text_loc = (0, 100)
            if LEVEL == 7:
                self.things = [(2650, 100)]
                self.texts = self.font.render("drag your click when you're at the top", True, (220, 150, 150))
                self.text_loc = (0, WIN_H - self.texts.get_height())
            if LEVEL == 8:
                self.things = [(850, 450)]
                self.texts = self.font.render("hold your click for just a moment", True, (0, 0, 0))
            if LEVEL == 9:
                self.things = [(750, 850), (1750, 850), (1250, 100), (2250, 100)]
                self.texts = self.font.render("catch the ball before it falls in the red", True, (0, 0, 0))
            if LEVEL == 10:
                self.things = [(-150, 0), (350, 0), (850, 0), (1350, 0), (1850, 0)]
                self.texts = self.font.render("be as fast as possible between gaps", True, (0, 0, 0))
            if LEVEL == 11:
                self.things = [(1500, 250)]
                self.texts = self.font.render("click here for a moment", True, (0, 0, 0))
            if LEVEL == 12:
                self.things = [(1000, 800)]
                self.texts = self.font.render("click twice", True, (0, 0, 0))
            if LEVEL == 13:
                self.things = [(-150, 50)]
                self.texts = self.font.render("lame way of doing this", True, (0, 0, 0))
            if LEVEL == 14:
                self.things = [(1500, 50)]
                self.texts = self.font.render("click when right under here", True, (0, 0, 0))
            if LEVEL == 15:
                self.things = [(850, 50), (1850, 650), (1550, 1350)]
                self.texts = self.font.render("drop at these places", True, (0, 0, 0))
                self.text_loc = (WIN_W - self.texts.get_width(), 0)
            if LEVEL == 16:
                self.things = [(1575, 0), (1575, 300), (1575, 800)]
                self.texts = self.font.render("click shortly from top to bottom", True, (0, 0, 0))
                self.text_loc = (0, WIN_H - self.texts.get_height())
            if LEVEL == 17:
                self.things = [(1075, 0), (1075, 300), (1075, 800)]
                self.texts = self.font.render("click shortly from bottom to top", True, (0, 0, 0))
            if LEVEL == 18:
                self.things = []
                self.texts = self.font.render("try and click high when you are low", True, (0, 0, 0))
            if LEVEL == 19:
                self.things = []
                self.texts = self.font.render("follow the line", True, (255, 255, 255))
                self.text_loc = (WIN_W - self.texts.get_width(), 0)
            if LEVEL == 20:
                self.things = [(1775, 550)]
                self.texts = self.font.render("click here but not too fast", True, (0, 0, 0))
                self.text_loc = (0, WIN_H - self.texts.get_height())

        def show(self, screen, camera):
            for i in self.things:
                pygame.draw.line(screen, (219, 190, 86), (i[0] - camera.x_offset, i[1] - camera.y_offset),
                                 (i[0] + 50 - camera.x_offset, i[1] - camera.y_offset - 50), 10)
                pygame.draw.line(screen, (219, 190, 86), (i[0] + 50 - camera.x_offset, i[1] - camera.y_offset - 50),
                                 (i[0] + 100 - camera.x_offset, i[1] - camera.y_offset), 10)
                pygame.draw.line(screen, (219, 190, 86), (i[0] - camera.x_offset, i[1] - camera.y_offset),
                                 (i[0] + 50 - camera.x_offset, i[1] - camera.y_offset + 50), 10)
                pygame.draw.line(screen, (219, 190, 86), (i[0] + 50 - camera.x_offset, i[1] - camera.y_offset + 50),
                                 (i[0] + 100 - camera.x_offset, i[1] - camera.y_offset), 10)
            screen.blit(self.texts, self.text_loc)

        globals()["level" + str(LEVEL - 1)] = 0

    class Ball:
        def __init__(self, size, camera):
            self.spawn = (100, camera.max_y)
            camera.y_offset = camera.max_y
            self.x = WIN_W * 0.1
            self.y = WIN_H * 0.75
            self.size = size
            self.weight = 1
            self.clicked = False
            self.slowness = 10 / self.weight
            self.ot_size = math.sqrt((size ** 2) / 2)
            self.finished = True

            self.velocity = (0, 0)

            self.click_dis = 0

        def respawn(self, camera):
            global CLICKED
            self.x = WIN_W * 0.1
            self.y = WIN_H * 0.75
            self.velocity = (0, 0)
            CLICKED = False
            camera.x_offset = 0
            camera.y_offset = camera.max_y

        def update(self, hit_boxes, hurt_boxes, camera, levels, click_loc=()):

            respawn = False
            if click_loc == ():
                click_loc = (self.x, self.y)
                self.clicked = False
            else:
                self.clicked = True

            self.velocity = (self.velocity[0] * 0.99, self.velocity[1] * 0.99)

            if math.fabs(self.velocity[0]) < 0.5:
                self.velocity = (0, self.velocity[1])
            if math.fabs(self.velocity[1]) < 0.5:
                self.velocity = (self.velocity[0], 0)
            self.velocity = (self.velocity[0], (self.velocity[1] + self.weight))

            if self.y + self.size >= WIN_H:
                self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                self.y = WIN_H - self.size + 1
            elif self.y <= self.size:
                self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                self.y = 0 + self.size
            if self.x + self.size >= WIN_W:
                global LEVEL
                respawn = True
                if LEVEL < len(levels):
                    LEVEL += 1
                    levels[LEVEL - 1].spawn(camera)
                    self.spawn = (100, camera.max_y)
                else:
                    self.finished = True

            elif self.x <= self.size:
                self.velocity = (-0.5 * self.velocity[0], self.velocity[1])
                self.x = 0 + self.size

            if self.clicked:
                click_loc = (click_loc[0], click_loc[1] + 200)
                self.velocity = (0, (click_loc[1] - self.y) / self.slowness)

            if self.clicked:
                self.velocity = ((click_loc[0] - self.x) / self.slowness, self.velocity[1])

            # hitbox stuff
            for i in hit_boxes:

                # bottom of circle to top of box
                if i.lines.top_line[0][1] < self.y + self.size + self.velocity[1] and \
                        i.lines.top_line[0][0] < self.x + self.velocity[0] < i.lines.top_line[1][0]:
                    if i.lines.top_line[0][1] >= self.y + self.size:
                        if self.velocity[1] > 4 and click_loc[1] < i.lines.top_line[0][
                            1] - self.size and not self.clicked:
                            self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                        else:
                            self.velocity = (self.velocity[0], 0)
                            self.y = i.lines.top_line[0][1] - self.size
                # left bottom of circle to top of box
                if i.lines.top_line[0][1] < self.y + self.ot_size + self.velocity[1] and \
                        i.lines.top_line[0][0] < self.x + self.velocity[0] - self.ot_size < i.lines.top_line[1][0]:
                    if i.lines.top_line[0][1] >= self.y + self.ot_size:
                        if self.velocity[1] > 4 \
                                and click_loc[1] < i.lines.top_line[0][1] - self.ot_size and not self.clicked:
                            self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                        else:
                            self.velocity = (self.velocity[0], 0)
                            self.y = i.lines.top_line[0][1] - self.ot_size
                # right bottom of circle to top of box
                if i.lines.top_line[0][1] < self.y + self.ot_size + self.velocity[1] and \
                        i.lines.top_line[0][0] < self.x + self.velocity[0] + self.ot_size < i.lines.top_line[1][0]:
                    if i.lines.top_line[0][1] >= self.y + self.ot_size:
                        if self.velocity[1] > 4 \
                                and click_loc[1] < i.lines.top_line[0][1] - self.ot_size and not self.clicked:
                            self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                        else:
                            self.velocity = (self.velocity[0], 0)
                            self.y = i.lines.top_line[0][1] - self.ot_size
                # left of circle to top of box
                if i.lines.top_line[0][1] < self.y + self.velocity[1] and \
                        i.lines.top_line[0][0] < self.x - self.size + self.velocity[0] < i.lines.top_line[1][0]:
                    if i.lines.top_line[0][1] >= self.y:
                        if self.velocity[1] > 4 and click_loc[1] < i.lines.top_line[0][1] and not self.clicked:
                            self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                        else:
                            self.velocity = (self.velocity[0], 0)
                            self.y = i.lines.top_line[0][1]
                # right of circle to top of box
                if i.lines.top_line[0][1] < self.y + self.velocity[1] and \
                        i.lines.top_line[0][0] < self.x + self.size + self.velocity[0] < i.lines.top_line[1][0]:
                    if i.lines.top_line[0][1] >= self.y:
                        if self.velocity[1] > 4 and click_loc[1] < i.lines.top_line[0][1] and not self.clicked:
                            self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                        else:
                            self.velocity = (self.velocity[0], 0)
                            self.y = i.lines.top_line[0][1]

                # top of circle to bottom of box
                if i.lines.bottom_line[0][1] > self.y - self.size + self.velocity[1] and \
                        i.lines.bottom_line[0][0] < self.x + self.velocity[0] < i.lines.bottom_line[1][0]:
                    if i.lines.bottom_line[0][1] <= self.y - self.size:
                        if self.velocity[1] < -4 \
                                and click_loc[1] > i.lines.bottom_line[0][1] + self.size and not self.clicked:
                            self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                        else:
                            self.velocity = (self.velocity[0], 0)
                            self.y = i.lines.bottom_line[0][1] + self.size

                # top left of circle to bottom of box
                if i.lines.bottom_line[0][1] > self.y - self.ot_size + self.velocity[1] and \
                        i.lines.bottom_line[0][0] < self.x + self.velocity[0] - self.ot_size < i.lines.bottom_line[1][
                    0]:
                    if i.lines.bottom_line[0][1] <= self.y - self.ot_size:
                        if self.velocity[1] < -4 \
                                and click_loc[1] > i.lines.bottom_line[0][1] + self.ot_size and not self.clicked:
                            self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                        else:
                            self.velocity = (self.velocity[0], 0)
                            self.y = i.lines.bottom_line[0][1] + self.ot_size

                # top right of circle to bottom of box
                if i.lines.bottom_line[0][1] > self.y - self.ot_size + self.velocity[1] and \
                        i.lines.bottom_line[0][0] < self.x + self.velocity[0] + self.ot_size < i.lines.bottom_line[1][
                    0]:
                    if i.lines.bottom_line[0][1] <= self.y - self.ot_size:
                        if self.velocity[1] < -4 \
                                and click_loc[1] > i.lines.bottom_line[0][1] - self.ot_size and not self.clicked:
                            self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                        else:
                            self.velocity = (self.velocity[0], 0)
                            self.y = i.lines.bottom_line[0][1] + self.ot_size

                # left of circle to bottom of box
                if i.lines.bottom_line[0][1] > self.y + self.velocity[1] and \
                        i.lines.bottom_line[0][0] < self.x - self.size + self.velocity[0] < i.lines.bottom_line[1][0]:
                    if i.lines.bottom_line[0][1] <= self.y:
                        if self.velocity[1] < -4 and click_loc[1] > i.lines.bottom_line[0][1] and not self.clicked:
                            self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                        else:
                            self.velocity = (self.velocity[0], 0)
                            self.y = i.lines.bottom_line[0][1]
                # right of circle to bottom of box
                if i.lines.bottom_line[0][1] > self.y + self.velocity[1] and \
                        i.lines.bottom_line[0][0] < self.x + self.size + self.velocity[0] < i.lines.bottom_line[1][0]:
                    if i.lines.bottom_line[0][1] <= self.y:
                        if self.velocity[1] < -4 and click_loc[1] > i.lines.bottom_line[0][1] and not self.clicked:
                            self.velocity = (self.velocity[0], -0.5 * self.velocity[1])
                        else:
                            self.velocity = (self.velocity[0], 0)
                            self.y = i.lines.bottom_line[0][1]

                # left of circle to right of box
                if i.lines.right_line[0][1] < self.y + self.velocity[1] < i.lines.right_line[1][1] and \
                        i.lines.right_line[0][0] > self.x - self.size + self.velocity[0]:
                    if i.lines.right_line[0][0] <= self.x - self.size:
                        if self.velocity[0] < -4 and not self.clicked:
                            self.velocity = (-0.5 * self.velocity[0], self.velocity[1])
                        else:
                            self.velocity = (0, self.velocity[1])
                            self.x = i.lines.right_line[0][0] + self.size

                # top left of circle to right of box
                if i.lines.right_line[0][1] < self.y + self.velocity[1] - self.ot_size < i.lines.right_line[1][1] and \
                        i.lines.right_line[0][0] > self.x - self.ot_size + self.velocity[0]:
                    if i.lines.right_line[0][0] <= self.x - self.ot_size:
                        if self.velocity[0] < -4 and not self.clicked:
                            self.velocity = (-0.5 * self.velocity[0], self.velocity[1])
                        else:
                            self.velocity = (0, self.velocity[1])
                            self.x = i.lines.right_line[0][0] + self.ot_size

                # bottom left of circle to right of box
                if i.lines.right_line[0][1] < self.y + self.velocity[1] + self.ot_size < i.lines.right_line[1][1] and \
                        i.lines.right_line[0][0] > self.x - self.ot_size + self.velocity[0]:
                    if i.lines.right_line[0][0] <= self.x - self.ot_size:
                        if self.velocity[0] < -4 and not self.clicked:
                            self.velocity = (-0.5 * self.velocity[0], self.velocity[1])
                        else:
                            self.velocity = (0, self.velocity[1])
                            self.x = i.lines.right_line[0][0] + self.ot_size

                # top of circle to right of box
                if i.lines.right_line[0][1] < self.y - self.size + self.velocity[1] < i.lines.right_line[1][1] and \
                        i.lines.right_line[0][0] > self.x + self.velocity[0]:
                    if i.lines.right_line[0][0] <= self.x:
                        if self.velocity[0] < -4 and not self.clicked:
                            self.velocity = (-0.5 * self.velocity[0], self.velocity[1])
                        else:
                            self.velocity = (0, self.velocity[1])
                            self.x = i.lines.right_line[0][0]

                # bottom of circle to right of box
                if i.lines.right_line[0][1] < self.y + self.size + self.velocity[1] < i.lines.right_line[1][1] and \
                        i.lines.right_line[0][0] > self.x + self.velocity[0]:
                    if i.lines.right_line[0][0] <= self.x:
                        if self.velocity[0] < -4 and not self.clicked:
                            self.velocity = (-0.5 * self.velocity[0], self.velocity[1])
                        else:
                            self.velocity = (0, self.velocity[1])
                            self.x = i.lines.right_line[0][0]

                # right of circle to left of box
                if i.lines.left_line[0][1] < self.y + self.velocity[1] < i.lines.left_line[1][1] and \
                        i.lines.left_line[0][0] < self.x + self.size + self.velocity[0]:
                    if i.lines.left_line[0][0] >= self.x + self.size:
                        if self.velocity[0] > 4 and not self.clicked:
                            self.velocity = (-0.5 * self.velocity[0], self.velocity[1])
                        else:
                            self.velocity = (0, self.velocity[1])
                            self.x = i.lines.left_line[0][0] - self.size

                # top right of circle to left of box
                if i.lines.left_line[0][1] < self.y + self.velocity[1] - self.ot_size < i.lines.left_line[1][1] and \
                        i.lines.left_line[0][0] < self.x + self.ot_size + self.velocity[0]:
                    if i.lines.left_line[0][0] >= self.x + self.ot_size:
                        if self.velocity[0] > 4 and not self.clicked:
                            self.velocity = (-0.5 * self.velocity[0], self.velocity[1])
                        else:
                            self.velocity = (0, self.velocity[1])
                            self.x = i.lines.left_line[0][0] - self.ot_size

                # top right of circle to left of box
                if i.lines.left_line[0][1] < self.y + self.velocity[1] + self.ot_size < i.lines.left_line[1][1] and \
                        i.lines.left_line[0][0] < self.x + self.ot_size + self.velocity[0]:
                    if i.lines.left_line[0][0] >= self.x + self.ot_size:
                        if self.velocity[0] > 4 and not self.clicked:
                            self.velocity = (-0.5 * self.velocity[0], self.velocity[1])
                        else:
                            self.velocity = (0, self.velocity[1])
                            self.x = i.lines.left_line[0][0] - self.ot_size

                # top of circle to left of box
                if i.lines.left_line[0][1] < self.y - self.size + self.velocity[1] < i.lines.left_line[1][1] and \
                        i.lines.left_line[0][0] < self.x + self.velocity[0]:
                    if i.lines.left_line[0][0] >= self.x:
                        if self.velocity[0] > 4 and not self.clicked:
                            self.velocity = (-0.5 * self.velocity[0], self.velocity[1])
                        else:
                            self.velocity = (0, self.velocity[1])
                            self.x = i.lines.left_line[0][0]

                # top of circle to left of box
                if i.lines.left_line[0][1] < self.y + self.size + self.velocity[1] < i.lines.left_line[1][1] and \
                        i.lines.left_line[0][0] < self.x + self.velocity[0]:
                    if i.lines.left_line[0][0] >= self.x:
                        if self.velocity[0] > 4 and not self.clicked:
                            self.velocity = (-0.5 * self.velocity[0], self.velocity[1])
                        else:
                            self.velocity = (0, self.velocity[1])
                            self.x = i.lines.left_line[0][0]

                # time to suffer again
            for i in hurt_boxes:
                # bottom of circle to top of box
                if i.lines.top_line[0][1] < self.y + self.size + self.velocity[1] and \
                        i.lines.top_line[0][0] < self.x + self.velocity[0] < i.lines.top_line[1][0]:
                    if i.lines.top_line[0][1] >= self.y + self.size:
                        respawn = True
                # left bottom of circle to top of box
                if i.lines.top_line[0][1] < self.y + self.ot_size + self.velocity[1] and \
                        i.lines.top_line[0][0] < self.x + self.velocity[0] - self.ot_size < i.lines.top_line[1][0]:
                    if i.lines.top_line[0][1] >= self.y + self.ot_size:
                        respawn = True
                # right bottom of circle to top of box
                if i.lines.top_line[0][1] < self.y + self.ot_size + self.velocity[1] and \
                        i.lines.top_line[0][0] < self.x + self.velocity[0] + self.ot_size < i.lines.top_line[1][0]:
                    if i.lines.top_line[0][1] >= self.y + self.ot_size:
                        respawn = True
                # left of circle to top of box
                if i.lines.top_line[0][1] < self.y + self.velocity[1] and \
                        i.lines.top_line[0][0] < self.x - self.size + self.velocity[0] < i.lines.top_line[1][0]:
                    if i.lines.top_line[0][1] >= self.y:
                        respawn = True
                # right of circle to top of box
                if i.lines.top_line[0][1] < self.y + self.velocity[1] and \
                        i.lines.top_line[0][0] < self.x + self.size + self.velocity[0] < i.lines.top_line[1][0]:
                    if i.lines.top_line[0][1] >= self.y:
                        respawn = True

                # top of circle to bottom of box
                if i.lines.bottom_line[0][1] > self.y - self.size + self.velocity[1] and \
                        i.lines.bottom_line[0][0] < self.x + self.velocity[0] < i.lines.bottom_line[1][0]:
                    if i.lines.bottom_line[0][1] <= self.y - self.size:
                        respawn = True

                # top left of circle to bottom of box
                if i.lines.bottom_line[0][1] > self.y - self.ot_size + self.velocity[1] and \
                        i.lines.bottom_line[0][0] < self.x + self.velocity[0] - self.ot_size < i.lines.bottom_line[1][
                    0]:
                    if i.lines.bottom_line[0][1] <= self.y - self.ot_size:
                        respawn = True

                # top right of circle to bottom of box
                if i.lines.bottom_line[0][1] > self.y - self.ot_size + self.velocity[1] and \
                        i.lines.bottom_line[0][0] < self.x + self.velocity[0] + self.ot_size < i.lines.bottom_line[1][
                    0]:
                    if i.lines.bottom_line[0][1] <= self.y - self.ot_size:
                        respawn = True

                # left of circle to bottom of box
                if i.lines.bottom_line[0][1] > self.y + self.velocity[1] and \
                        i.lines.bottom_line[0][0] < self.x - self.size + self.velocity[0] < i.lines.bottom_line[1][0]:
                    if i.lines.bottom_line[0][1] <= self.y:
                        respawn = True
                # right of circle to bottom of box
                if i.lines.bottom_line[0][1] > self.y + self.velocity[1] and \
                        i.lines.bottom_line[0][0] < self.x + self.size + self.velocity[0] < i.lines.bottom_line[1][0]:
                    if i.lines.bottom_line[0][1] <= self.y:
                        respawn = True

                # left of circle to right of box
                if i.lines.right_line[0][1] < self.y + self.velocity[1] < i.lines.right_line[1][1] and \
                        i.lines.right_line[0][0] > self.x - self.size + self.velocity[0]:
                    if i.lines.right_line[0][0] <= self.x - self.size:
                        respawn = True

                # top left of circle to right of box
                if i.lines.right_line[0][1] < self.y + self.velocity[1] - self.ot_size < i.lines.right_line[1][1] and \
                        i.lines.right_line[0][0] > self.x - self.ot_size + self.velocity[0]:
                    if i.lines.right_line[0][0] <= self.x - self.ot_size:
                        respawn = True

                # bottom left of circle to right of box
                if i.lines.right_line[0][1] < self.y + self.velocity[1] + self.ot_size < i.lines.right_line[1][1] and \
                        i.lines.right_line[0][0] > self.x - self.ot_size + self.velocity[0]:
                    if i.lines.right_line[0][0] <= self.x - self.ot_size:
                        respawn = True

                # top of circle to right of box
                if i.lines.right_line[0][1] < self.y - self.size + self.velocity[1] < i.lines.right_line[1][1] and \
                        i.lines.right_line[0][0] > self.x + self.velocity[0]:
                    if i.lines.right_line[0][0] <= self.x:
                        respawn = True

                # bottom of circle to right of box
                if i.lines.right_line[0][1] < self.y + self.size + self.velocity[1] < i.lines.right_line[1][1] and \
                        i.lines.right_line[0][0] > self.x + self.velocity[0]:
                    if i.lines.right_line[0][0] <= self.x:
                        respawn = True

                # right of circle to left of box
                if i.lines.left_line[0][1] < self.y + self.velocity[1] < i.lines.left_line[1][1] and \
                        i.lines.left_line[0][0] < self.x + self.size + self.velocity[0]:
                    if i.lines.left_line[0][0] >= self.x + self.size:
                        respawn = True

                # top right of circle to left of box
                if i.lines.left_line[0][1] < self.y + self.velocity[1] - self.ot_size < i.lines.left_line[1][1] and \
                        i.lines.left_line[0][0] < self.x + self.ot_size + self.velocity[0]:
                    if i.lines.left_line[0][0] >= self.x + self.ot_size:
                        respawn = True

                # top right of circle to left of box
                if i.lines.left_line[0][1] < self.y + self.velocity[1] + self.ot_size < i.lines.left_line[1][1] and \
                        i.lines.left_line[0][0] < self.x + self.ot_size + self.velocity[0]:
                    if i.lines.left_line[0][0] >= self.x + self.ot_size:
                        respawn = True

                # top of circle to left of box
                if i.lines.left_line[0][1] < self.y - self.size + self.velocity[1] < i.lines.left_line[1][1] and \
                        i.lines.left_line[0][0] < self.x + self.velocity[0]:
                    if i.lines.left_line[0][0] >= self.x:
                        respawn = True

                # top of circle to left of box
                if i.lines.left_line[0][1] < self.y + self.size + self.velocity[1] < i.lines.left_line[1][1] and \
                        i.lines.left_line[0][0] < self.x + self.velocity[0]:
                    if i.lines.left_line[0][0] >= self.x:
                        respawn = True

            if respawn:
                self.respawn(camera)

            prev_loc = (self.x, self.y)
            self.x += self.velocity[0]
            self.y += self.velocity[1]

            if prev_loc[0] >= WIN_W:
                self.velocity = (0, self.velocity[1])
            if prev_loc[1] >= WIN_H:
                self.velocity = (self.velocity[0], 0)

    global WIN_W, WIN_H

    pygame.init()
    fps = 60
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    info = pygame.display.Info()
    WIN_W = info.current_w
    WIN_H = info.current_h
    all_times = []
    scrunkly = 0

    hints = Hints(pygame.font.Font("simplism/Nu.ttf", 100))
    hints_on = False

    debug_font = pygame.font.Font("simplism/Nu.ttf", 50)

    camera = Camera()
    level1 = Level((HitBox(3000, 1300, (-400, -200), "hit"),
                    HitBox(2000, 2000, (1500, 1500), "hit"),
                    HitBox(4000, 4000, (-400, -200), "click")), (-400, 700), ("Welcome", debug_font))
    level2 = Level((HitBox(3000, 1300, (-400, -200), "hit"),
                    HitBox(2000, 2000, (1500, 1500), "hurt"),
                    HitBox(4000, 4000, (-400, -200), "click")), (-400, 700), ("Red hurts", debug_font))
    level3 = Level((HitBox(3000, 1300, (-400, -200), "hurt"),
                    HitBox(2000, 2000, (1500, 1500), "hurt"),
                    HitBox(4000, 4000, (-400, -200), "click")), (-400, 700), ("Red hurts... A LOT", debug_font))
    level4 = Level((HitBox(3000, 400, (-400, 800), "hit"),
                    HitBox(2000, 2000, (1500, 1500), "hurt"),
                    HitBox(4000, 1000, (-400, -200), "click")), (-400, 700), ("Clicks work on green", debug_font))
    level5 = Level((HitBox(3000, 200, (-400, -200), "hit"),
                    HitBox(2000, 3000, (1500, 500), "hit"),
                    HitBox(500, 200, (0, 750), "click"),
                    HitBox(3000, 200, (-400, 0), "click")), (-400, 700),
                   ("Press h for a level's hints", debug_font))
    level6 = Level((HitBox(100, 1000, (1000, 500), "hit"),
                    HitBox(100, 1000, (2060, 0), "hurt"),
                    HitBox(100, 500, (2060, 1000), "click"),
                    HitBox(400, 100, (1100, 500), "hurt"),
                    HitBox(310, 100, (1750, 500), "hurt"),
                    HitBox(250, 250, (1500, 0), "click")), (-400, 0), ("Getting under it", debug_font))
    level7 = Level((HitBox(800, 100, (1500, 1850), "hit"),
                    HitBox(100, 1900, (1500, -50), "hit"),
                    HitBox(100, 1900, (2200, -50), "hit"),
                    HitBox(100, 2000, (500, 500), "hit"),
                    HitBox(100, 1450, (2500, 500), "hurt"),
                    HitBox(100, 2000, (2800, -50), "hurt"),
                    HitBox(100, 200, (2500, 1950), "hit"),
                    HitBox(4000, 200, (-150, -50), "click"),
                    HitBox(4000, 200, (-150, 1950), "click"),
                    HitBox(1000, 200, (-400, 700), "click"),
                    HitBox(500, 200, (2300, 700), "click")), (300, 700),
                   ("Press R     for quick restart", debug_font))
    level8 = Level((HitBox(1000, 50, (400, 1400), "hurt"),
                    HitBox(50, 900, (1400, 800), "hurt"),
                    HitBox(50, 500, (1400, 0), "hurt"),
                    HitBox(200, 200, (700, 300), "click")), (-400, 0), ("Not too fast, not too slow", debug_font))
    level9 = Level((HitBox(100, 1000, (1500, 500), "hurt"),
                    HitBox(100, 1000, (500, 500), "hurt"),
                    HitBox(100, 800, (1000, 0), "hurt"),
                    HitBox(100, 800, (2000, 0), "hurt"),
                    HitBox(100, 300, (2500, 500), "hurt"),
                    HitBox(100, 700, (2500, 800), "hit"),
                    HitBox(4000, 200, (-400, 800), "click"),
                    HitBox(3000, 100, (600, 1400), "hurt"),
                    HitBox(4000, 200, (-400, 0), "click")), (300, 0), ("Over and out", debug_font))
    level10 = Level((HitBox(3000, 50, (-400, 50), "hurt"),
                     HitBox(1200, 3000, (300, 500), "hurt"),
                     HitBox(100, 1700, (2100, -500), "hurt"),
                     HitBox(200, 200, (-200, 0), "click"),
                     HitBox(200, 200, (300, 0), "click"),
                     HitBox(200, 200, (800, 0), "click"),
                     HitBox(200, 200, (1300, 0), "click"),
                     HitBox(200, 200, (1800, 0), "click"),
                     HitBox(3000, 300, (-400, 1200), "click")), (-400, 0), ("  PARKOUR !!!", debug_font))
    level11 = Level((HitBox(3000, 100, (600, 1350), "hurt"),
                     HitBox(100, 100, (1500, 700), "hurt"),
                     HitBox(100, 100, (300, 800), "hit"),
                     HitBox(100, 100, (600, 700), "click"),
                     HitBox(100, 100, (0, 200), "hurt"),
                     HitBox(100, 100, (1000, 1000), "hit"),
                     HitBox(100, 100, (2200, 300), "click"),
                     HitBox(100, 100, (100, 500), "click"),
                     HitBox(100, 100, (2000, 900), "hurt"),
                     HitBox(100, 100, (2100, 100), "hit"),
                     HitBox(100, 100, (1500, 200), "click"),
                     HitBox(100, 100, (1000, 400), "hurt"),
                     HitBox(100, 100, (1700, 600), "hit")), (-150, 0), ("Déjà vu", debug_font))
    level12 = Level((HitBox(100, 850, (2000, 600), "hurt"),
                     HitBox(1000, 100, (1000, 1350), "hurt"),
                     HitBox(1950, 100, (50, 600), "hurt"),
                     HitBox(100, 200, (50, 400), "hit"),
                     HitBox(100, 200, (50, 700), "hit"),
                     HitBox(100, 300, (50, 900), "hurt"),
                     HitBox(100, 1000, (1000, 600), "click"),
                     HitBox(200, 200, (-150, 400), "click"),
                     HitBox(2000, 100, (850, 0), "click")), (-150, 0), ("Backtrack", debug_font))
    level13 = Level((HitBox(3000, 100, (300, 800), "hit"),
                     HitBox(250, 50, (-150, 0), "click")), (-150, 0),
                    ("Well what are you waiting for?", debug_font))
    level14 = Level((HitBox(1425, 50, (1025, 1400), "hurt"),
                     HitBox(1600, 50, (-150, 400), "hurt"),
                     HitBox(800, 50, (1650, 400), "hurt"),
                     HitBox(1500, 100, (1125, 0), "click"),
                     HitBox(100, 2000, (1025, 450), "click"),
                     HitBox(50, 1000, (2375, 450), "hit")), (-150, 0), ("WALL BALL", debug_font))
    level15 = Level((HitBox(400, 50, (400, 400), "hurt"),
                     HitBox(1425, 50, (1000, 400), "hurt"),
                     HitBox(200, 50, (800, 900), "hit"),
                     HitBox(2100, 100, (300, 0), "click"),
                     HitBox(1400, 50, (400, 1400), "hurt"),
                     HitBox(400, 50, (2000, 1400), "hurt"),
                     HitBox(2100, 100, (300, 600), "click"),
                     HitBox(200, 50, (1800, 1900), "hit"),
                     HitBox(2100, 100, (300, 1300), "click"),
                     HitBox(1100, 50, (400, 2100), "hurt"),
                     HitBox(700, 50, (1700, 2100), "hurt"),
                     HitBox(200, 50, (1500, 2600), "hit"),
                     HitBox(100, 3000, (300, 400), "hit"),
                     HitBox(100, 3000, (200, 0), "click"),
                     HitBox(50, 2450, (2375, 0), "hurt"),
                     HitBox(1700, 50, (400, 2900), "hurt"),
                     HitBox(275, 50, (2100, 2900), "hit"),
                     HitBox(50, 500, (2375, 2450), "click")), (-150, 1500), ("     Dropper", debug_font))
    level16 = Level((HitBox(825, 50, (1550, 900), "hurt"),
                     HitBox(750, 50, (950, 1400), "hurt"),
                     HitBox(750, 50, (950, 400), "hurt"),
                     HitBox(50, 1050, (900, 400), "hit"),
                     HitBox(200, 2000, (1525, 0), "click"),
                     HitBox(50, 950, (2375, 0), "hurt")), (-150, 0), ("At least it isn't upw   ards", debug_font))
    level17 = Level((HitBox(1350, 50, (-150, 900), "hurt"),
                     HitBox(1425, 50, (1025, 1400), "hurt"),
                     HitBox(1400, 50, (1050, 400), "hurt"),
                     HitBox(1500, 100, (1225, 0), "click"),
                     HitBox(200, 2000, (1025, 0), "click"),
                     HitBox(50, 1000, (2375, 450), "hurt")), (-150, 0), ("I'm sorry", debug_font))
    level18 = Level((HitBox(2150, 200, (-150, 3400), "click"),
                     HitBox(2150, 200, (-150, 2900), "click"),
                     HitBox(2150, 200, (-150, 2400), "click"),
                     HitBox(2150, 200, (-150, 1900), "click"),
                     HitBox(2150, 200, (-150, 1400), "click"),
                     HitBox(2150, 200, (-150, 900), "click"),
                     HitBox(2150, 200, (-150, 400), "click"),
                     HitBox(3000, 200, (-150, 0), "click"),
                     HitBox(100, 4250, (2000, 400), "hit"),
                     HitBox(500, 100, (2000, 400), "hit")), (-150, 3000), ("The climb", debug_font))
    level19 = Level((HitBox(1000, 25, (-150, 1000), "click"),
                     HitBox(25, 800, (825, 200), "click"),
                     HitBox(800, 25, (850, 200), "click"),
                     HitBox(25, 600, (1650, 200), "click"),
                     HitBox(800, 25, (1650, 800), "click"),
                     HitBox(900, 1000, (-150, 0), "hurt"),
                     HitBox(900, 800, (1750, 0), "hurt"),
                     HitBox(1025, 200, (750, 0), "hurt"),
                     HitBox(25, 100, (350, 1025), "hurt"),
                     HitBox(575, 150, (350, 1300), "hurt"),
                     HitBox(650, 950, (925, 500), "hurt"),
                     HitBox(900, 350, (1550, 1100), "hurt")), (-150, 0), ("Tightrope", debug_font))
    level20 = Level((HitBox(500, 50, (0, 1150), "hit"),
                     HitBox(50, 650, (0, 500), "hit"),
                     HitBox(1750, 50, (50, 500), "hurt"),
                     HitBox(500, 50, (1850, 500), "hurt"),
                     HitBox(50, 950, (2300, 500), "hit"),
                     HitBox(500, 50, (500, 1150), "hurt"),
                     HitBox(800, 50, (1500, 1150), "hurt"),
                     HitBox(800, 250, (1500, 1200), "hit"),
                     HitBox(50, 600, (1800, 0), "click"),
                     HitBox(210, 210, (-210, 500), "click")), (-210, 0), ("Backtrack 2", debug_font))

    # levels = [level2, level20]
    levels = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12,
              level13, level14, level15, level16, level17, level18, level19, level20]

    levels[0].spawn(camera)
    click = ()
    global CLICKED
    cur_level = 1

    ball = Ball(50, camera)

    time_rect = pygame.Surface((250, 50))
    time_rect_rect = time_rect.get_rect()
    open("simplism/idk_lol.txt", "w")
    hurt_group = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    clickable_group = pygame.sprite.Group()
    for i in levels[LEVEL - 1].layout:
        if i.kind == "hurt":
            hurt_group.add(i)
        elif i.kind == "hit":
            block_group.add(i)
        else:
            clickable_group.add(i)

    image = pygame.image.load("simplism/simplism_comp.png")

    while ball.finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ball.finished = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        screen.blit(image, (0, 0))
        pygame.display.flip()

    level_start_time = pygame.time.get_ticks()
    while not ball.finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                CLICKED = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                CLICKED = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_r:
                    ball.respawn(camera)
                if event.key == pygame.K_h:
                    hints_on = True

        screen.fill((255, 255, 255))
        click_on_block = False
        current_time = pygame.time.get_ticks()
        scrunkly = (current_time - level_start_time) / 1000
        velo_text = debug_font.render(f"{str(int(scrunkly))}:{str(int(scrunkly * 100) - int(scrunkly) * 100)}",
                                      True, (255, 255, 255))
        if cur_level != LEVEL:
            cur_level += 1
            all_times.append(scrunkly)
            with open("simplism/idk_lol.txt", "a") as f:
                f.write(f"level {str(LEVEL - 1)} - time {str(int(scrunkly * 1000) / 1000)}\n")
                acc = 0
                for i in all_times:
                    acc += i
                f.write(f"total time {str(int(acc * 1000) / 1000)}\n")
            for i in hurt_group:
                hurt_group.remove(i)
            for i in block_group:
                block_group.remove(i)
            for i in clickable_group:
                clickable_group.remove(i)

            hints.new_level()

            for j in levels[LEVEL - 1].layout:
                if j.kind == "hurt":
                    hurt_group.add(j)
                elif j.kind == "hit":
                    block_group.add(j)
                else:
                    clickable_group.add(j)
            globals()[f"level {str(LEVEL - 1)}"] = 0
            hints_on = False
            level_start_time = current_time
        if CLICKED:
            for i in clickable_group:
                dummy = pygame.mouse.get_pos()
                if i.rect.x - camera.x_offset + i.rect.width >= dummy[0] >= i.rect.x - camera.x_offset and \
                        i.rect.y - camera.y_offset + i.rect.height >= dummy[1] >= i.rect.y - camera.y_offset:
                    click_on_block = True
            if not click_on_block:
                CLICKED = False
        ball.update(block_group, hurt_group, camera, levels, click)
        camera.update(ball)
        if CLICKED:
            click = pygame.mouse.get_pos()
        else:
            click = ()

        for i in clickable_group:
            screen.blit(i.image, (i.rect.x - camera.x_offset, i.rect.y - camera.y_offset))
            i.update(camera)
        for i in block_group:
            i.update(camera)
            screen.blit(i.image, (i.rect.x - camera.x_offset, i.rect.y - camera.y_offset))
        for i in hurt_group:
            screen.blit(i.image, (i.rect.x - camera.x_offset, i.rect.y - camera.y_offset))
            i.update(camera)
        if CLICKED:
            pygame.draw.line(screen, (0, 0, 0), click, (ball.x, ball.y), 5)

        if hints_on:
            hints.show(screen, camera)
        screen.blit(time_rect, time_rect_rect)
        screen.blit(velo_text, (0, 0))
        screen.blit(levels[LEVEL - 1].name, (WIN_W * 0.1 - camera.x_offset,
                                             WIN_H * 0.9 - camera.y_offset + camera.max_y - 200))

        clock.tick(fps)
        pygame.draw.circle(screen, (150, 200, 255), (ball.x, ball.y), ball.size)
        pygame.display.flip()
    image = pygame.image.load("simplism/winar.png")
    while ball.finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ball.finished = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        screen.blit(image, (0, 0))
        pygame.display.flip()

    pygame.display.set_mode((1, 1))
    time.sleep(0.5)
    pygame.display.quit()
    time.sleep(0.5)
    pygame.quit()
    with open("simplism/idk_lol.txt", "a") as f:
        f.write(f"level {str(LEVEL)} - time {str(int(scrunkly * 1000) / 1000)}\n")
        acc = scrunkly
        for i in all_times:
            acc += i
        f.write(f"total time {str(int(acc * 1000) / 1000)}\n")
    with open("simplism/high_scores.txt", "a") as f:
        acc = scrunkly
        for i in all_times:
            acc += i
        f.write("total time " + str(int(acc * 1000) / 1000) + " seconds - " + str(input("Insert name: \n")) + "\n")
    sys.exit()


def main():
    print("\33[33mWelcome\33[0m to a collection of all my projects this year!")
    print("These are most of my Python projects I have created throughout my time doing Python (up until now)\n")
    print("\33[34m1 - draw something: uses the turtle module to draw a picture of the vocaloid Neutra with her scythe")
    print("\33[95m2 - turtle racing: uses the turtle module to race turtles that move forward randomly")
    print("\33[34m3 - 8 bit drawing: the jankiest way to do pixel art, done with the turtle module")
    print("\33[95m4 - adventure: a story told in terminal, but things might go wrong")
    print("\33[34m5 - guessing: play against a robot or friend to guess the right number \t\t\33[33m2 players optional")
    print("\33[95m6 - pong: an atmospheric take on the very simple game \t\t\t\t\t\t\33[33m2 players required")
    print("\33[34m7 - density: play against your friend to see who can grow larger \t\t\t\33[33m2 players required")
    print("\33[95m8 - raiden: an pseudo-8-bit throwback to the classic")
    print("\33[34m9 - music: a rhythm game proof of concept, using your whole keyboard \t\t\33[31munfinished")
    print("\33[92m10 - simplism (best one): traverse 20 levels of simple but challenging platforming! \33[0m\33[1m\n")
    game_choose = input("Which program would you like to try?\n")
    if game_choose is "1":
        draw_something()
    if game_choose is "2":
        turtle_race()
    if game_choose is "3":
        bit_draw()
    if game_choose is "4":
        adventure()
    if game_choose is "5":
        guessing()
    if game_choose is "6":
        pong()
    if game_choose is "7":
        density()
    if game_choose is "8":
        raiden()
    if game_choose is "9":
        music()
    if game_choose == "10":
        simplism()


if __name__ == "__main__":
    main()
