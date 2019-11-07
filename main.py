# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import time
import argparse
import stimuli
import numpy as np
import pandas as pd


# q1   q2
# q3   q4


####################################
# Draw Functions
####################################

def drawTaskCanvas(canvas, data):
    if data.state == 'copy task canvas':
        canvas.create_text(data.width/2, data.height-2.5*data.margin, text="Go to Reference", font="Arial 16")
        canvas.create_rectangle(data.width/2-100, data.height-3*data.margin, data.width/2+100, data.height-2*data.margin)
        time_remaining = "Time Remaining: " + ("%d" % (data.copy_time_remaining / 1000))
    if data.state == 'recall task canvas':
        time_remaining = "Time Remaining: " + (("%d" % (data.recall_time_remaining / 1000)))
    canvas.create_text(data.width/2, data.margin, text="Canvas", font="Arial 24 bold")
    canvas.create_text(2.25*data.margin,data.height-2.25*data.margin, text=time_remaining, font="Arial 16")
    canvas.create_text(data.width-2.25*data.margin, data.height-2.5*data.margin, text="Done!", font="Arial 16")
    canvas.create_rectangle(data.width-data.margin-150, data.height-3*data.margin, data.width-data.margin, data.height-2*data.margin)
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

def drawTaskRef(canvas, data):
    if data.state == 'copy task ref':
        canvas.create_text(data.width/2, data.height-2.5*data.margin, text="Go to Canvas", font="Arial 16")
        canvas.create_rectangle(data.width/2-100, data.height-3*data.margin, data.width/2+100, data.height-2*data.margin)
        time_remaining = "Time Remaining: " + ("%d" % (data.copy_time_remaining / 1000))
    if data.state == 'recall task ref':
        time_remaining = "Time Remaining: " + (("%d" % (data.recall_presentation_time_remaining / 1000)))
    canvas.create_text(data.width/2, data.margin, text="Reference", font="Arial 24 bold")
    canvas.create_text(2.25*data.margin,data.height-2.25*data.margin, text=time_remaining, font="Arial 16")
    if data.state != 'recall task ref':
        canvas.create_text(data.width-2.25*data.margin, data.height-2.5*data.margin, text="Done!", font="Arial 16")
        canvas.create_rectangle(data.width-data.margin-150, data.height-3*data.margin, data.width-data.margin, data.height-2*data.margin)
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
    for r in range(len(data.stim3)):
        for c in range(len(data.stim3[0])):
            color = 'black' if data.stim3[r][c] != 0 else 'white'
            canvas.create_rectangle(data.rect_width*c+offset+data.grid_width,
                                    data.rect_height*r+2*data.margin+data.grid_width,
                                    data.rect_width*(c+1)+offset+data.grid_width,
                                    data.rect_height*(r+1)+2*data.margin+data.grid_width,
                                    fill=color)

def drawInstructions(canvas, data):
    canvas.create_text(data.width/2, data.height/2,
                       text="You will begin with 2 practice trials.\nClick the mouse on top of the box to fill in color.\nUse the “To Canvas” and “To Reference” button to switch between the reference and canvas boards\nPress [Space] to begin copy task",
                       font="Arial 18")

def drawReadyCopyTask(canvas, data):
    canvas.create_text(data.width/2, data.height/2,
                       text="The time limit is 15 seconds\nYou can refer to reference board at anytime\nClick ‘done’ button after filling out the board\nPress [Space] to begin copy task",
                       font="Arial 18")

def drawReadyRecallTask(canvas, data):
    canvas.create_text(data.width/2, data.height/2,
                       text="You will be given 5 seconds to memorize the board\nYou cannot refer back to the reference board after the 5 seconds\n10 seconds will be the time limit to fill in the board\nPress [Space] to begin recall task",
                       font="Arial 18")

def drawCorrect(canvas, data):
    canvas.create_text(data.width/2, data.height/2, text="CORRECT!", font="Arial 24 bold", fill="green")

def drawWrong(canvas, data):
    txt = str(int(data.correctness / 64 * 100)) + "% Correct"
    canvas.create_text(data.width/2, data.height/2, text=txt, font="Arial 24 bold", fill="red")

def drawCopySwitchCanvas(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill='white', width=0)

def drawCopySwitchRef(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill='white', width=0)

def drawEnd(canvas, data):
    canvas.create_text(data.width/2, data.height/2, text="END!", font="Arial 24 bold")

def drawPaused(canvas, data):
    canvas.create_text(data.width/2, data.height/2, text="PAUSED", font="Arial 24 bold")


####################################
# List Functions
####################################

def create2dlist(width=4, height=4):
    ret = []
    for h in range(height):
        L = [0] * width
        ret.append(L)
    return ret

def reset_exp(data):
    data.exp0 = create2dlist()
    data.exp1 = create2dlist()
    data.exp2 = create2dlist()
    data.exp3 = create2dlist()


####################################
# Canvas Interaction Functions
####################################

def fill_rect(event, data):
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
    assert(data.state == 'copy task ref' or data.state == 'copy task canvas')
    if (event.x > data.width/2-100 and event.x < data.width/2+100 and
        event.y > data.height-3*data.margin and event.y < data.height-2*data.margin):
        return True
    return False

def done_button_pressed(event, data):
    assert(data.state == 'copy task ref' or data.state == 'copy task canvas' or
           data.state == 'recall task canvas')
    if (event.x > data.width-data.margin-150 and event.x < data.width-data.margin and
        event.y > data.height-3*data.margin and event.y < data.height-2*data.margin):
        return True
    return False

def mousePressedCopyRef(event, data):
    if switch_button_pressed(event,data):
        data.state = 'copy switch canvas'
    elif done_button_pressed(event,data):
        data.correctness = None
        check_correctness(data)
        if data.correctness == 8*8:
            data.state = 'copy correct'
        else:
            data.state = 'copy wrong'

def mousePressedCopyCanvas(event, data):
    fill_rect(event,data)
    if switch_button_pressed(event,data):
        data.state = 'copy switch ref'
    elif done_button_pressed(event,data):
        data.correctness = None
        check_correctness(data)
        if data.correctness == 8*8:
            data.state = 'copy correct'
        else:
            data.state = 'copy wrong'

def mousePressedRecallCanvas(event, data):
    fill_rect(event,data)
    if done_button_pressed(event,data):
        data.correctness = None
        check_correctness(data)
        if data.correctness == 8*8:
            data.state = 'recall correct'
        else:
            data.state = 'recall wrong'


####################################
# Utility Functions
####################################

def collect_statistics(data):
    if data.recall:
        q1      = stimuli.getPatternID(data.trial[0][0])
        q2      = stimuli.getPatternID(data.trial[1][0])
        q3      = stimuli.getPatternID(data.trial[2][0])
        q4      = stimuli.getPatternID(data.trial[3][0])
        name    = data.id
        size    = data.condition
        freq    = data.trial[4]
        rt      = 10 * 1000 - data.recall_time_remaining
        correct = data.correctness
        df = pd.DataFrame([[name,size,freq,q1,q2,q3,q4,rt,correct]], columns=['id','size','freq','q1','q2','q3','q4','RT','correct'])
        data.statistics = data.statistics.append(df)

def check_correctness(data):
    assert(data.correctness == None) # otherwise some shit is wrong
    exp_list  = [data.exp0, data.exp1, data.exp2, data.exp3]
    stim_list = [data.stim0, data.stim1, data.stim2, data.stim3]
    correct = 8*8
    incorrect = 0
    for q in range(4): # 4 quadrants
        exp  = exp_list[q]
        stim = stim_list[q]
        for r in range(len(exp)):
            for c in range(len(exp[r])):
                if exp[r][c] != stim[r][c]:
                    incorrect += 1
    correct = correct - incorrect
    data.correctness = correct
    collect_statistics(data)
    reset_exp(data)
    data.copy_time_remaining = 15 * 1000 # reset to 15 seconds
    data.recall_time_remaining = 10 * 1000 # reset to 10 seconds
    if data.recall:
        data.trial = data.trials[data.recall_trial]
    elif data.practice:
        data.trial = data.trials[data.practice_trial]
    elif data.copy:
        data.trial = data.trials[data.copy_trial]
    for p in [data.trial[0], data.trial[1], data.trial[2], data.trial[3]]:
        if p[1] == 1:
            data.stim0 = p[0]
        elif p[1] == 2:
            data.stim1 = p[0]
        elif p[1] == 3:
            data.stim2 = p[0]
        elif p[1] == 4:
            data.stim3 = p[0]
    return correct


####################################
# Kosbie's Functions
####################################

def init(data):
    # load data.xyz as appropriate

    # INITIAL STATE
    cond = "LS" if data.condition == 0 else "HS"
    data.copy_trials = stimuli.generateTrialListCopy(cond)
    data.practice_trials = stimuli.generateTrialListPractice(cond)
    data.recall_trials = stimuli.generateTrialListRecall(cond)
    data.trials = data.practice_trials
    data.practice = True
    data.copy = False
    data.recall = False

    data.practice_trial = 0
    data.total_practice_trials = len(data.practice_trials)

    data.copy_trial = 0
    data.total_copy_trials = len(data.copy_trials)

    data.recall_trial = 0
    data.total_recall_trials = len(data.recall_trials)

    data.trial = data.trials[data.practice_trial]
    data.stim0 = create2dlist()
    data.stim1 = create2dlist()
    data.stim2 = create2dlist()
    data.stim3 = create2dlist()
    for p in [data.trial[0], data.trial[1], data.trial[2], data.trial[3]]:
        if p[1] == 1:
            data.stim0 = p[0]
        elif p[1] == 2:
            data.stim1 = p[0]
        elif p[1] == 3:
            data.stim2 = p[0]
        elif p[1] == 4:
            data.stim3 = p[0]
    data.exp0 = create2dlist()
    data.exp1 = create2dlist()
    data.exp2 = create2dlist()
    data.exp3 = create2dlist()
    data.prev_state = None
    data.margin = 60
    data.rect_width = 90
    data.rect_height = 90
    data.grid_width = data.rect_width * 4
    data.grid_height = data.rect_height * 4
    data.copy_time_remaining = 15 * 1000 # 15 seconds
    data.switch_time = 0.5 * 1000 # half a second
    data.correctness = None
    data.feedback_time = 2 * 1000 # 2 seconds
    data.recall_presentation_time_remaining = 5 * 1000 # 5 seconds
    data.recall_time_remaining = 10 * 1000 # 10 seconds
    data.statistics = pd.DataFrame([[-1,-1,-1,-1,-1,-1,-1,-1,-1]],
                                    columns=['id','size','freq','q1','q2','q3','q4','RT','correct']) # first row will be dummy row

def mousePressed(event, data):
    if data.state == 'copy task ref':
        mousePressedCopyRef(event,data)
    elif data.state == 'copy task canvas':
        mousePressedCopyCanvas(event,data)
    elif data.state == 'recall task canvas':
        mousePressedRecallCanvas(event,data)

def keyPressed(event, data):
    if data.state != 'paused':
        print(event.char == 'p')
        if event.char == 'p':
            data.prev_state = data.state
            data.state = 'paused'
        if data.state == 'instructions':
            if event.char == ' ':
                data.practice = True
                data.state = 'copy task ref'
        elif data.state == 'ready copy task':
            if event.char == ' ':
                data.practice = False
                data.copy = True
                data.state = 'copy task ref'
                data.trials = data.copy_trials
                data.trial = data.trials[data.copy_trial]
                for p in [data.trial[0], data.trial[1], data.trial[2], data.trial[3]]:
                    if p[1] == 1:
                        data.stim0 = p[0]
                    elif p[1] == 2:
                        data.stim1 = p[0]
                    elif p[1] == 3:
                        data.stim2 = p[0]
                    elif p[1] == 4:
                        data.stim3 = p[0]
        elif data.state == 'ready recall task':
            if event.char == ' ':
                data.copy = False
                data.recall = True
                data.state = 'recall task ref'
                data.trials = data.recall_trials
                data.trial = data.trials[data.recall_trial]
                for p in [data.trial[0], data.trial[1], data.trial[2], data.trial[3]]:
                    if p[1] == 1:
                        data.stim0 = p[0]
                    elif p[1] == 2:
                        data.stim1 = p[0]
                    elif p[1] == 3:
                        data.stim2 = p[0]
                    elif p[1] == 4:
                        data.stim3 = p[0]
    else:
        if event.char == 'p':
            data.state = data.prev_state

def timerFired(data):
    if data.state == 'copy task ref' or data.state == 'copy task canvas':
        data.copy_time_remaining -= data.timerDelay * 5
        if data.copy_time_remaining < 0:
            data.correctness = None
            check_correctness(data)
            data.state = 'copy wrong'
            data.copy_time_remaining = 15 * 1000
            return
    elif data.state == 'copy correct' or data.state == 'copy wrong':
        data.feedback_time -= data.timerDelay * 5
        if data.feedback_time < 0:
            data.state = 'copy task ref'
            data.feedback_time = 2 * 1000
            if data.practice:
                data.practice_trial += 1
                if data.practice_trial == data.total_practice_trials:
                    data.practice = False
                    data.practice_trial = -1
                    data.copy = True
                    data.state = 'ready copy task'
                    return
                data.trial = data.trials[data.practice_trial]
                for p in [data.trial[0], data.trial[1], data.trial[2], data.trial[3]]:
                    if p[1] == 1:
                        data.stim0 = p[0]
                    elif p[1] == 2:
                        data.stim1 = p[0]
                    elif p[1] == 3:
                        data.stim2 = p[0]
                    elif p[1] == 4:
                        data.stim3 = p[0]
            if data.copy:
                data.copy_trial += 1
            if data.copy_trial == data.total_copy_trials:
                data.copy = False
                data.recall = True
                data.copy_trial = -1
                data.state = 'ready recall task'
            return
    elif data.state == 'recall correct' or data.state == 'recall wrong':
        data.feedback_time -= data.timerDelay * 5
        if data.feedback_time < 0:
            data.state = 'recall task ref'
            data.feedback_time = 2 * 1000
            data.recall_trial += 1
            if data.recall_trial == data.total_recall_trials:
                data.recall = False
                data.recall_trial = -1
                data.state = 'end'
    elif data.state == 'copy switch canvas':
        data.switch_time -= data.timerDelay * 5
        if data.switch_time < 0:
            data.state = 'copy task canvas'
            data.switch_time = 0.5 * 1000
    elif data.state == 'copy switch ref':
        data.switch_time -= data.timerDelay * 5
        if data.switch_time < 0:
            data.state = 'copy task ref'
            data.switch_time = 0.5 * 1000
    elif data.state == 'recall task ref':
        data.recall_presentation_time_remaining -= data.timerDelay * 5
        if data.recall_presentation_time_remaining < 0:
            data.state = 'recall task canvas'
            data.recall_presentation_time_remaining = 5 * 1000
            return
    elif data.state == 'recall task canvas':
        data.recall_time_remaining -= data.timerDelay * 5
        if data.recall_time_remaining < 0:
            data.correctness = None
            check_correctness(data)
            data.state = 'recall wrong'
            return

def redrawAll(canvas, data):
    if data.state == 'paused':
        drawPaused(canvas,data)
    elif data.state == 'instructions':
        drawInstructions(canvas,data)
    elif data.state == 'ready copy task':
        drawReadyCopyTask(canvas,data)
    elif data.state == 'copy task ref':
        drawTaskRef(canvas,data)
    elif data.state == 'copy task canvas':
        drawTaskCanvas(canvas,data)
    elif data.state == 'recall task ref':
        drawTaskRef(canvas,data)
    elif data.state == 'recall task canvas':
        drawTaskCanvas(canvas,data)
    elif data.state == 'copy switch canvas':
        drawCopySwitchCanvas(canvas,data)
    elif data.state == 'copy switch ref':
        drawCopySwitchRef(canvas,data)
    elif data.state == 'ready recall task':
        drawReadyRecallTask(canvas,data)
    elif data.state == 'copy correct':
        drawCorrect(canvas,data)
    elif data.state == 'copy wrong':
        drawWrong(canvas,data)
    elif data.state == 'recall correct':
        drawCorrect(canvas,data)
    elif data.state == 'recall wrong':
        drawWrong(canvas,data)
    elif data.state == 'end':
        drawEnd(canvas,data)
    else:
        return # we should never reach this state

####################################
# use the run function as-is
####################################

def run(name, condition, width=300, height=300): # thanks koz
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
    data.id = name
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
    print(data.statistics)
    csv_name = "data/" + data.id + ".csv"
    data.statistics.to_csv(csv_name)
    print("bye!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=str, help="Participant ID")
    parser.add_argument('--cond', type=int, help="Experiment Condition", default=0)
    args = parser.parse_args()
    run(args.id, args.cond, 1920, 1080)
main()