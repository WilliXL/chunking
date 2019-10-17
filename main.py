# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

# exp0   exp1
# exp2   exp3


def drawLeft(canvas, data):
    if data.condition == 0:
        for r in range(len(data.stimulus)):
            for c in range(len(data.stimulus[0])):
                color = 'black' if data.stimulus[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+data.margin,
                                        data.rect_height*r+2*data.margin,
                                        data.rect_width*(c+1)+data.margin,
                                        data.rect_height*(r+1)+2*data.margin,
                                        fill=color)
    else:
        for r in range(len(data.stimulus)):
            for c in range(len(data.stimulus[0])):
                color = 'black' if data.stimulus[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+data.margin,
                                        data.rect_height*r+2*data.margin,
                                        data.rect_width*(c+1)+data.margin,
                                        data.rect_height*(r+1)+2*data.margin,
                                        fill=color)

def drawRight(canvas, data):
    offset = data.width/2 + data.margin
    if data.condition == 0:
        for r in range(len(data.exp0)):
            for c in range(len(data.exp0[0])):
                color = 'black' if data.exp0[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset,
                                        data.rect_height*r+2*data.margin,
                                        data.rect_width*(c+1)+offset,
                                        data.rect_height*(r+1)+2*data.margin,
                                        fill=color)
    else:
        for r in range(len(data.exp0)):
            for c in range(len(data.exp0[0])):
                color = 'black' if data.exp0[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset,
                                        data.rect_height*r+2*data.margin,
                                        data.rect_width*(c+1)+offset,
                                        data.rect_height*(r+1)+2*data.margin,
                                        fill=color)
        for r in range(len(data.exp1)):
            for c in range(len(data.exp1[0])):
                color = 'black' if data.exp1[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset+data.grid_width,
                                        data.rect_height*r+2*data.margin,
                                        data.rect_width*(c+1)+offset+data.grid_width,
                                        data.rect_height*(r+1)+2*data.margin,
                                        fill=color)
        for r in range(len(data.exp2)):
            for c in range(len(data.exp2[0])):
                color = 'black' if data.exp2[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset,
                                        data.rect_height*r+2*data.margin+data.grid_height,
                                        data.rect_width*(c+1)+offset,
                                        data.rect_height*(r+1)+2*data.margin+data.grid_height,
                                        fill=color)
        for r in range(len(data.exp3)):
            for c in range(len(data.exp3[0])):
                color = 'black' if data.exp3[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset+data.grid_width,
                                        data.rect_height*r+2*data.margin+data.grid_height,
                                        data.rect_width*(c+1)+offset+data.grid_width,
                                        data.rect_height*(r+1)+2*data.margin+data.grid_height,
                                        fill=color)

def create2dlist(width=4, height=4):
    ret = []
    for h in range(height):
        L = [0] * width
        ret.append(L)
    return ret

def init(data):
    # load data.xyz as appropriate
    data.stimulus = create2dlist()
    data.exp0 = create2dlist()
    data.exp1 = create2dlist()
    data.exp2 = create2dlist()
    data.exp3 = create2dlist()
    data.margin = 120
    data.rect_width = 90
    data.rect_height = 90
    data.grid_width = data.rect_width * 4
    data.grid_height = data.rect_height * 4

def fillRect(event, data):
    offset = data.width/2 + data.margin
    for r in range(len(data.exp0)):
        for c in range(len(data.exp0[0])):
            if (event.x > data.rect_width*c+offset and
                event.y > data.rect_height*r+2*data.margin and
                event.x < data.rect_width*(c+1)+offset and
                event.y < data.rect_height*(r+1)+2*data.margin):
                data.exp0[r][c] = 1 if data.exp0[r][c] == 0 else 0
    for r in range(len(data.exp1)):
        for c in range(len(data.exp1[0])):
            if (event.x > data.rect_width*c+offset+data.grid_width and
                event.y > data.rect_height*r+2*data.margin and
                event.x < data.rect_width*(c+1)+offset+data.grid_width and
                event.y < data.rect_height*(r+1)+2*data.margin):
                data.exp1[r][c] = 1 if data.exp1[r][c] == 0 else 0
    for r in range(len(data.exp2)):
        for c in range(len(data.exp2[0])):
            if (event.x > data.rect_width*c+offset and
                event.y > data.rect_height*r+2*data.margin+data.grid_height and
                event.x < data.rect_width*(c+1)+offset and
                event.y < data.rect_height*(r+1)+2*data.margin+data.grid_height):
                data.exp2[r][c] = 1 if data.exp2[r][c] == 0 else 0
    for r in range(len(data.exp3)):
        for c in range(len(data.exp3[0])):
            if (event.x > data.rect_width*c+offset+data.grid_width and
                event.y > data.rect_height*r+2*data.margin+data.grid_height and
                event.x < data.rect_width*(c+1)+offset+data.grid_width and
                event.y < data.rect_height*(r+1)+2*data.margin+data.grid_height):
                data.exp3[r][c] = 1 if data.exp3[r][c] == 0 else 0

def mousePressed(event, data):
    fillRect(event, data)

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    drawLeft(canvas,data)
    canvas.create_line(data.width/2,
                       0,
                       data.width/2,
                       data.height)
    drawRight(canvas,data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300, condition=0):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 5 # milliseconds
    data.condition = condition
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1920, 1080, 1)