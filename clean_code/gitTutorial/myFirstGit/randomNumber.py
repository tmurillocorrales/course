#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: elisabeth, wanqi, tati

import random
import time
import sys

def get_random_number(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename + ".log", "a")
    f.write("Our randomly generated number is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()


def get_color_by_dice_roll(spots):
    colors = ["blue", "green", 'red', 'yellow', 'purple', 'orange']
    return colors[spots-1]

def amazing_function_by_elsa():
    pass


if __name__ == "__main__":
    outputfilename = "randomNumber"
    roll = get_random_number(1, 6)
    color = get_color_by_dice_roll(roll)
    write_log_file(outputfilename, color)

rollos=[]
for i in range(6):
    roll = get_random_number(1, 6)
    rollos.append(roll)
print(rollos)
sys.stdout.flush()
import matplotlib.pyplot as plt

plt.barh(range(6),rolls)
plt.show()

#June 16, 2020




