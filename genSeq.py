from midiutil.MidiFile import MIDIFile
import random

#mid C pitch = 60

def genNote():
    note = []
    note.append(random.randint(30,90))
    note.append(random.random()*3)
    note.append(0.3)
    note.append(random.randint(30,107))
    return note


# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Jen")
mf.addTempo(track, time, 120)

channel = 0

for i in range(30):
    note = genNote()
    mf.addNote(track, channel, note[0], note[1], note[2], note[3])

# write it to disk
with open("v1_tests/output3.mid", 'wb') as outf:
    mf.writeFile(outf)

