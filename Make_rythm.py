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
