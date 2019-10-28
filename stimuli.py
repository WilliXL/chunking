import random
import copy

# quadrants:
# [1  2]
# [3  4]

patternTemp = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

gridTemp = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

def convertToPattern(indicesToFill):
  rows, cols = 4, 4
  pattern = copy.deepcopy(patternTemp)
  for i in indicesToFill:
    row = i // cols
    col = i % cols
    pattern[row][col] = 1
  return pattern

def convertPatternToGrid(pattern, quadrant):
  grid = copy.deepcopy(gridTemp)
  if quadrant == 1:
    for row in range(4):
      for col in range(4):
        grid[row][col] = pattern[row % 4][col % 4]
  elif quadrant == 2:
    for row in range(4):
      for col in range(4, 8):
        grid[row][col] = pattern[row % 4][col % 4]
  elif quadrant == 3:
    for row in range(4, 8):
      for col in range(4):
        grid[row][col] = pattern[row % 4][col % 4]
  elif quadrant == 4:
    for row in range(4, 8):
      for col in range(4, 8):
        grid[row][col] = pattern[row % 4][col % 4]
  else:
    print("Error: Invalid quadrant (%d)" % quadrant)
  return grid

patternsUsed = []

def isUsed(pattern):
  for p in patternsUsed:
    if pattern == p: return True
  return False

def createRandomPattern(quadrant, filled=True):
  if not filled:
    return (copy.deepcopy(patternTemp), quadrant)
  indices = [i for i in range(0, 16)]
  while(True):
    indicesToFill = random.sample(indices, 4)
    pattern = convertToPattern(indicesToFill)
    if not isUsed(pattern): 
      patternsUsed.append(pattern)
      break
  # return convertPatternToGrid(pattern, quadrant)
  return (pattern, quadrant)

def superpose(g1, g2):
  resultGrid = copy.deepcopy(gridTemp)
  for i in range(8):
    for j in range(8):
      resultGrid[i][j] = g1[i][j] + g2[i][j]
  return resultGrid

###############################################################################

# Helper function for print2dList.
# This finds the maximum length of the string
# representation of any item in the 2d list
def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in range(rows):
        for col in range(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen

# Because Python prints 2d lists on one row,
# we might want to write our own function
# that prints 2d lists a bit nicer.
def print2dList(a):
    if (a == []):
        # So we don't crash accessing a[0]
        print([])
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = maxItemLength(a)
    print("[ ", end="")
    for row in range(rows):
        if (row > 0): print("\n  ", end="")
        print("[ ", end="")
        for col in range(cols):
            if (col > 0): print(", ", end="")
            # The next 2 lines print a[row][col] with the given fieldWidth
            formatSpec = "%" + str(fieldWidth) + "s"
            print(formatSpec % str(a[row][col]), end="")
        print(" ]", end="")
    print("]")

###############################################################################

from patterns import *

# p1, p2, p3, p4 <---- high frequency
# p5, p6, p7, p8 <---- low frequency

stimListLS =  [ 
                [p1, blank(2), blank(3), blank(4)],
                [blank(1), p2, blank(3), blank(4)],
                [blank(1), blank(2), p3, blank(4)],
                [blank(1), blank(2), blank(3), p4],
                [p5, blank(2), blank(3), blank(4)],
                [blank(1), p6, blank(3), blank(4)],
                [blank(1), blank(2), p7, blank(4)],
                [blank(1), blank(2), blank(3), p8]
              ]

# (p1, p2), (p3, p4), (p9, p11), (p10, p12) <---- high frequency
# (p5, p6), (p7, p8), (p13, p16), (p14, p15) <---- low frequency

stimListHS =  [ 
                [p1, p2, blank(3), blank(4)],
                [blank(1), blank(2), p3, p4],
                [p9, blank(2), p11, blank(4)],
                [blank(1), p10, blank(3), p12],
                [p5, p6, blank(3), blank(4)],
                [blank(1), blank(2), p7, p8],
                [p13, blank(2), blank(3), p16],
                [blank(1), p14, p15, blank(4)]
              ]

def generateTrialList(condition):
  stimList = []
  L = []
  if condition == "LS":
    stimList = stimListLS
  elif condition == "HS":
    stimList = stimListHS
  else:
    print("ERROR: invalid condition")
    return L
  for i in range(4):
    for freq in range(8):
      L.append(stimList[i])
  for i in range(4, 8):
    for freq in range(2):
      L.append(stimList[i])
  random.shuffle(L)
  return L
