import random
import copy

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
  for i in indices:
    row = i // cols
    col = i % cols
    pattern[row][col] = 1
  return pattern

def convertPatternToGrid(pattern, quadrant):
  return

def createRandomPattern(quadrant=None):
  if quadrant == None:
    quadrant = random.randint(1,4)
  indices = [i for i in range(0, 16)]
  squaresToFill = random.sample(indices, 4)
  pattern = convertToPattern(indicesToFill)
  return convertPatternToGrid(pattern, quadrant)

