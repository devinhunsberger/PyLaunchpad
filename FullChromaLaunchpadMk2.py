import mido
import time

from ClearLaunchpad import RemoveNotes, ClearScreen
from FirstMido import FillNotes

#Increases color wheel and location by 1 to maximum (89) in order to determine best usage
#of colors. Need to assign each color their own RGB value first though.

def FullChroma():
    i = 0
    x = 10
    while i < 100:
            FillNotes(x, i)
            i += 1
            x += 1
FullChroma()
