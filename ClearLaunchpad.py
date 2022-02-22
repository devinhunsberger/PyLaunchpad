import mido
'''
msg = mido.Message('note_off', note = 25)
msg.copy(channel=6)
port = mido.open_output('Launchpad MK2 1')
port.send(msg)
with mido.open_input() as inport:
    for msg in inport:
        print(msg)

mid = mido.MidiFile('song.mid')
for msg in mid.play():
    port.send(msg)

'''
def RemoveNotes(spec):
    msg = mido.Message('note_off', note = spec)
    msg.copy(channel = 6)
    port = mido.open_output('Launchpad MK2 1')
    port.send(msg)

'''
i = 11
while i < 90:
    if(i % 10 != 0):
        RemoveNotes(i)
    i += 1
'''
def ClearScreen():
    i = 10
    while i < 90:
        if(i % 10 != 0):
            RemoveNotes(i)
        i += 1

ClearScreen()
