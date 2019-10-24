# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

# exp0   exp1
# exp2   exp3
# same for stim

# states:
# instructions, copy task ref, copy task canvas, setup

def drawCopyTaskCanvas(canvas, data):
    canvas.create_text(data.width/2, data.height-2.5*data.margin, text="Go to Reference", font="Arial 16")
    canvas.create_rectangle(data.width/2-100, data.height-3*data.margin, data.width/2+100, data.height-2*data.margin)
    canvas.create_text(data.width/2, data.margin, text="Canvas", font="Arial 24 bold")
    if data.condition == 0:
        offset = data.width/2 - data.grid_width/2 # for centering grid
        for r in range(len(data.exp0)):
            for c in range(len(data.exp0[0])):
                color = 'black' if data.exp0[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset,
                                        data.rect_height*r+2*data.margin,
                                        data.rect_width*(c+1)+offset,
                                        data.rect_height*(r+1)+2*data.margin,
                                        fill=color)
    elif data.condition == 1:
        offset = data.width/2 - data.grid_width # for centering grid
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
                                        data.rect_height*r+2*data.margin+data.grid_width,
                                        data.rect_width*(c+1)+offset,
                                        data.rect_height*(r+1)+2*data.margin+data.grid_width,
                                        fill=color)
        for r in range(len(data.exp3)):
            for c in range(len(data.exp3[0])):
                color = 'black' if data.exp3[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset+data.grid_width,
                                        data.rect_height*r+2*data.margin+data.grid_width,
                                        data.rect_width*(c+1)+offset+data.grid_width,
                                        data.rect_height*(r+1)+2*data.margin+data.grid_width,
                                        fill=color)

def create2dlist(width=4, height=4):
    ret = []
    for h in range(height):
        L = [0] * width
        ret.append(L)
    return ret

def init(data):
    # load data.xyz as appropriate
    data.stim0 = create2dlist()
    data.stim1 = create2dlist()
    data.stim2 = create2dlist()
    data.stim3 = create2dlist()
    data.exp0 = create2dlist()
    data.exp1 = create2dlist()
    data.exp2 = create2dlist()
    data.exp3 = create2dlist()
    data.condition = 0 # default
    data.margin = 60
    data.rect_width = 90
    data.rect_height = 90
    data.grid_width = data.rect_width * 4
    data.grid_height = data.rect_height * 4

def fillRect(event, data):
    if data.condition == 0:
        offset = data.width/2 - data.grid_width/2 # for centering grid
    elif data.condition == 1:
        offset = data.width/2 - data.grid_width # for centering grid
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

def switch_button_pressed(event, data):
    if (event.x > data.width/2-100 and event.x < data.width/2+100 and
        event.y > data.height-3*data.margin and event.y < data.height-2*data.margin):
        print(data.state)
        return True
    return False

def mousePressedCopyRef(event, data):
    if switch_button_pressed(event,data):
        data.state = 'copy task canvas'

def mousePressedCopyCanvas(event, data):
    fillRect(event,data)
    if switch_button_pressed(event,data):
        data.state = 'copy task ref'

def mousePressed(event, data):
    if data.state == 'copy task ref':
        mousePressedCopyRef(event,data)
    elif data.state == 'copy task canvas':
        mousePressedCopyCanvas(event,data)

def keyPressed(event, data):
    if data.state == 'instructions':
        if event.char == '0':
            data.conditon = 0
            data.state = 'copy task ref'
        elif event.char == '1':
            data.condition = 1
            data.state = 'copy task ref'

def timerFired(data):
    pass

def drawCopyTaskRef(canvas, data):
    canvas.create_text(data.width/2, data.height-2.5*data.margin, text="Go to Canvas", font="Arial 16")
    canvas.create_rectangle(data.width/2-100, data.height-3*data.margin, data.width/2+100, data.height-2*data.margin)
    canvas.create_text(data.width/2, data.margin, text="Reference", font="Arial 24 bold")
    if data.condition == 0:
        offset = data.width/2 - data.grid_width/2 # for centering grid
        for r in range(len(data.stim0)):
            for c in range(len(data.stim0[0])):
                color = 'black' if data.stim0[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset,
                                        data.rect_height*r+2*data.margin,
                                        data.rect_width*(c+1)+offset,
                                        data.rect_height*(r+1)+2*data.margin,
                                        fill=color)
    elif data.condition == 1:
        offset = data.width/2 - data.grid_width # for centering grid
        for r in range(len(data.stim0)):
            for c in range(len(data.stim0[0])):
                color = 'black' if data.stim0[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset,
                                        data.rect_height*r+2*data.margin,
                                        data.rect_width*(c+1)+offset,
                                        data.rect_height*(r+1)+2*data.margin,
                                        fill=color)
        for r in range(len(data.stim1)):
            for c in range(len(data.stim1[0])):
                color = 'black' if data.stim1[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset+data.grid_width,
                                        data.rect_height*r+2*data.margin,
                                        data.rect_width*(c+1)+offset+data.grid_width,
                                        data.rect_height*(r+1)+2*data.margin,
                                        fill=color)
        for r in range(len(data.stim2)):
            for c in range(len(data.stim2[0])):
                color = 'black' if data.stim2[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset,
                                        data.rect_height*r+2*data.margin+data.grid_width,
                                        data.rect_width*(c+1)+offset,
                                        data.rect_height*(r+1)+2*data.margin+data.grid_width,
                                        fill=color)
        for r in range(len(data.stim2)):
            for c in range(len(data.stim2[0])):
                color = 'black' if data.stim2[r][c] != 0 else 'white'
                canvas.create_rectangle(data.rect_width*c+offset+data.grid_width,
                                        data.rect_height*r+2*data.margin+data.grid_width,
                                        data.rect_width*(c+1)+offset+data.grid_width,
                                        data.rect_height*(r+1)+2*data.margin+data.grid_width,
                                        fill=color)

def drawInstructions(canvas, data):
    canvas.create_text(data.width/2, data.height/2, text="Instructions Go Here\nPress [Space] to Continue")


def redrawAll(canvas, data):
    if data.state == 'setup':
        drawSetup(canvas,data)
    elif data.state == 'instructions':
        drawInstructions(canvas,data)
    elif data.state == 'copy task ref':
        drawCopyTaskRef(canvas,data)
    elif data.state == 'copy task canvas':
        drawCopyTaskCanvas(canvas,data)
    else:
        return # we should never reach this state

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
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
    data.state = 'instructions'
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

run(1920, 1080)