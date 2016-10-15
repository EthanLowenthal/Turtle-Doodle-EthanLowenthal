import turtle
tur = turtle.Turtle()

def set_up():
    #Set up the turtle and move it to the correct position
    # tur = turtle.Turtle()
    tur.pensize(1)
    tur.penup()
    tur.goto(-turtle.window_width()//2, turtle.window_height()//2)
    tur.pendown()
    tur.speed(0)


def draw_grid(im):
    from values import dist
    #A var to keep what row the turtle is on
    row = 0

    #Draws Columns
    for i in range(im.size[0] - 1):
        tur.penup()
        tur.forward(dist)
        tur.pendown()
        tur.right(90)
        tur.forward(im.size[1] * dist)
        tur.left(180)
        tur.forward(im.size[1] * dist)
        tur.right(90)

    #Move back to the start
    tur.penup()
    tur.goto(-turtle.window_width()//2, turtle.window_height()//2)
    tur.pendown()

    #Draws Rows
    for i in range(im.size[1] - 1):
        tur.penup()
        tur.right(90)
        tur.forward(dist)
        tur.left(90)
        tur.pendown()
        tur.forward(im.size[0] * dist)
        tur.left(180)
        tur.forward(im.size[0] * dist)
        tur.left(180)

    row += dist

    #Move back to the start
    tur.penup()
    tur.goto(-turtle.window_width()//2, turtle.window_height()//2 - dist)
    tur.pendown()

    return row

def draw_pixels(pix_str, im, row):
    from values import dist
    #A counter for the number  of imes the for loop has run
    num = 0

    #The for loop that does the drawing
    for i, pix in enumerate(pix_str):
        print(pix)
        #Tests if the turtle is at the end of the line. If so, it puts it on a new line a row lower
        if i != 0 and num % im.size[0] == 0:
            row += dist
            tur.penup()
            tur.goto(-turtle.window_width()//2, turtle.window_height()//2 - row)

        #Tests if it should draw a white pixel
        if pix == 1:
            tur.penup()
            tur.forward(dist)

        #Tests if iit should draw a black pixel.
        # I put both tests just in case there is a number that is not a 1 or 0 in pix_str
        elif pix == 0:
            tur.pendown()
            tur.begin_fill()
            for i in range(4):
                tur.forward(dist)
                tur.left(90)
            tur.forward(dist)
            tur.end_fill()

        #Moves the clock forward one
        num += 1
