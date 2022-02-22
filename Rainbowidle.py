import mido
import random
from ClearLaunchpad import RemoveNotes, ClearScreen
from FirstMido import FillNotes

def columnsRight(x, colour):
    FillNotes(10 + x, colour)
    FillNotes(20 + x, colour)
    FillNotes(30 + x, colour)
    FillNotes(40 + x, colour)
    FillNotes(50 + x, colour)
    FillNotes(60 + x, colour)
    FillNotes(70 + x, colour)
    FillNotes(80 + x, colour)
    FillNotes(90 + x, colour)

def columnsLeft(x, colour):
    FillNotes(90 + x, colour)
    FillNotes(80 + x, colour)
    FillNotes(70 + x, colour)
    FillNotes(60 + x, colour)
    FillNotes(50 + x, colour)
    FillNotes(40 + x, colour)
    FillNotes(30 + x, colour)
    FillNotes(20 + x, colour)
    FillNotes(10 + x, colour)

def rowUp(y, colour):
    FillNotes(y * 10 + 1, colour)
    FillNotes(y * 10 + 2, colour)
    FillNotes(y * 10 + 3, colour)
    FillNotes(y * 10 + 4, colour)
    FillNotes(y * 10 + 5, colour)
    FillNotes(y * 10 + 6, colour)
    FillNotes(y * 10 + 7, colour)
    FillNotes(y * 10 + 8, colour)
    FillNotes(y * 10 + 9, colour)

def rowDown(y, colour):
    FillNotes(y * 10 + 9, colour)
    FillNotes(y * 10 + 8, colour)
    FillNotes(y * 10 + 7, colour)
    FillNotes(y * 10 + 6, colour)
    FillNotes(y * 10 + 5, colour)
    FillNotes(y * 10 + 4, colour)
    FillNotes(y * 10 + 3, colour)
    FillNotes(y * 10 + 2, colour)
    FillNotes(y * 10 + 1, colour)





def randomness():
    rowUp(random.randint(1,9), random.randint(0,127))
    columnsRight(random.randint(1,9), random.randint(0,127))
    rowDown(random.randint(1,9), random.randint(0,127))
    columnsLeft(random.randint(1,9), random.randint(0,127))
ClearScreen()
