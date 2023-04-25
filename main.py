import random
from midiutil import MIDIFile
import Make_rythm as mr

MF = MIDIFile(1)

TRACK = 0
CHANNEL = 0
TIME = 0
DURATION = 1

VOLUME = 100
TEMPO = 100

NOTES = [30, 32, 33]

MF.addTempo(TRACK, TIME, TEMPO)

rythm_list = mr.make_rythm(max_bars=30)


for bar in rythm_list:
    for note in bar:
        MF.addNote(TRACK, CHANNEL, random.choice(NOTES), TIME, note, VOLUME)
        TIME += note

with open("output1.mid", "wb") as output:
    MF.writeFile(output)