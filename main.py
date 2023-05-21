import random
from midiutil import MIDIFile
import Make_rythm as mr


C_MAJOR = [60, 62, 64, 65, 67, 69, 71, 72]
C_MINOR = [60, 62, 63, 65, 67, 68, 70, 72]
F_Minor = [65, 67, 68, 70, 72, 73, 75, 77]
B_MAJOR = [70, 73, 75, 76, 78, 80, 82]

SCALE_DICTIONARY = {"C_MAJOR": C_MAJOR, "C_MINOR": C_MINOR, "F_Minor": F_Minor, "B_Major": B_MAJOR}

def make_midi(cycle=1):

    num = 1
    for i in range(cycle):
        mf = MIDIFile(2)

        voices = 2

        for ii in range(voices):
            print(ii)
            track = ii
            channel = ii
            time = 0
            volume = 100

            mf.addProgramChange(track, channel, time, random.randint(0, 127))
            TEMPO = random.randint(40, 180)


            mf.addTempo(track, time, TEMPO)
            if (voices == 0):
                rythm_list = mr.make_b_rythm(max_bars=70)
            else:
                rythm_list = mr.make_rythm(max_bars=70)

            for bar in rythm_list:
                scale = random.choice(list(SCALE_DICTIONARY.values()))
                note = random.choice(scale)
                for step in bar:
                    if random.randint(0, 9) > 2:
                        note = random.choice(scale)
                    mf.addNote(track, channel, note, time, step, volume)
                    time += step

        with open(f"output{num}.mid", "wb") as output:
            mf.writeFile(output)
        num+=1



make_midi(20)