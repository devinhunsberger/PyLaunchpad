#Final File!!!!
#Brings everything including Scanner, draw notes, our log, etc
#This will be our animator, lets just start with a simple 4 by 4 image
import cv2
import mido
import pygame
import pygame_menu
from Scanner import Scan
from ClearLaunchpad import RemoveNotes, ClearScreen
from FirstMido import FillNotes

pygame.init()
screen = pygame.display.set_mode((800,800))

colorSelector = pygame_menu.Menu('Color Selection', 400, 400)

def selectColor(x):
     color = x

for x in Scan():
    buttons = colorSelector.add.button('Velocity:' + x, selectColor(Scan()[x]))
    newStr = Scan()[x][1:len(Scan()[x]) - 1]
    tup = tuple(map(int, newStr.split(', ')))
    buttons.add_underline(tup, 6, 10)

colorSelector.mainloop(screen)
