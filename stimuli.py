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

def createRandomPattern(quadrant=None):
  if quadrant == None:
    quadrant = random.randint(1,4)
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

###############################################################

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

