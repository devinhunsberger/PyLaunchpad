import mido
import time

from ClearLaunchpad import RemoveNotes, ClearScreen

#Launchpad starts at 11 ends at 89(bottom-left to top-right), every 10s seems to be skipped and currently unsure of how to control the top level.
#Technically I can just skip the 9's as well as it is the volume, pan, send A, etc, etc buttons.

def FillNotes(noteNum, vel):
    msg = mido.Message('note_on', note = noteNum, velocity = vel)
    msg.copy(channel = 6)
    port = mido.open_output('Launchpad MK2 1')
    port.send(msg)
#First Test With Launchpad! SUCCESS
def CoverPad():
    i = 11
    while i < 90:
        if(i % 10 != 0):
            FillNotes(i, 6)
            if(str(2) in str(i) or str(7) in str(i)):
                FillNotes(i, 30)
            elif(str(3) in str(i) and i >= 33 and i <= 36):
                FillNotes(i, 50)
            elif(i % 10 == 3 and i < 70 and i > 23):
                FillNotes(i, 50)
            elif(i % 10 == 6 and i < 70 and i > 23 or str(6) in str(i) and i >= 63 and i <= 66):
                FillNotes(i, 50)
            elif(i % 10 == 1 or i % 10 == 8):
                FillNotes(i, 78)
            else:
                FillNotes(i, 127)


def ColorVel(loc):
    i = 0
    while i < 127:
        FillNotes(loc,i)
        print(i)
        i += 1
        time.sleep(0.5)
    

def TwitchFollow():
    Locations = (14, 15, 23, 32, 41, 26, 37, 48, 51, 61, 58, 68, 72, 73, 77, 76, 64, 65)
    for i in Locations:
        FillNotes(i, 50)

def TwitchLogo():
    Locations = (13, 14, 21, 22, 23, 24, 25, 26, 37, 31, 41, 51, 61, 71, 82, 48, 58, 68, 78, 88, 83, 84, 85, 86, 87, 56, 66, 54, 64)
    for i in Locations:
        FillNotes(i, 50)
    i = 11
    while i < 90:
        if(not i in Locations and i % 10 != 9):
            FillNotes(i, 1)
        i += 1
