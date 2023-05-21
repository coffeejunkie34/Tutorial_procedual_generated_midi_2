import random

def make_rythm(beat = 4, max_bars = 0):
    doubletripplet = False
    rythm_list = []
    for bar in range(max_bars):
        bar_list = []
        while beat > 0.1:
            choice = random.randint(0,10)
            if choice < 3:
                bar_list.append(0.5)
                if random.randint(0,10) < 4:
                    bar_list.append(0.25)
                    bar_list.append(0.25)
                else:
                    bar_list.append(0.5)
                beat-=1
            if choice == 3 or choice == 4:
                bar_list.append(0.25)
                bar_list.append(0.25)
                if random.randint(0,10) < 7:
                    bar_list.append(0.25)
                    bar_list.append(0.25)
                else:
                    bar_list.append(0.5)
                beat -= 1
            if choice == 5 or doubletripplet:
                bar_list.append(0.3333)
                bar_list.append(0.3333)
                bar_list.append(0.3333)
                if random.randint(0,10) == 3 or  random.randint(0,10) == 4:
                    doubletripplet = True
                else:
                    doubletripplet = False
        rythm_list.append(bar_list)
        beat = 4

    return rythm_list

def make_b_rythm(beat = 4, max_bars = 0):
    b_rythm_list = []
    return_rythm_list = []
    times = 2
    save_beat = beat
    while(times):

        temp_bar = []
        while (beat > 0.1):
            choice = random.randint(0, 10)
            if (choice < 5):
                temp_bar.append(1.0)
                beat -= 1
            elif (choice >= 5 and choice < 8):
                temp_bar.append(0.5)
                temp_bar.append(0.5)
                beat -= 1
            else:
                temp_bar.append(0.25)
                temp_bar.append(0.25)
                temp_bar.append(0.25)
                temp_bar.append(0.25)
                beat -= 1
        b_rythm_list.append(temp_bar)
        times -=1
        beat = save_beat
    max_bars = int(max_bars / 2)
    for bar in range(max_bars):
        return_rythm_list.append(b_rythm_list[0])
        return_rythm_list.append(b_rythm_list[1])
    return return_rythm_list

print(make_b_rythm(max_bars=20))
