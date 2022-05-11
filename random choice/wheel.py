import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import exp, linspace
from random import shuffle, choice
from sys import argv

with open(argv[1]) as infile:
    labels = [line.strip() for line in infile]

with open("winnerdict.txt") as infile:
    winner = {int(k): int(v) for k, v in [x.strip().split() for x in infile]}

shuffle(labels)
colors = ["#" + "".join([choice("0123456789abcdef") for i in range(6)]) for i in range(len(labels))]
nums = [1] * len(labels)



def yieldn():
    x = linspace(0,4,100)
    y = exp(-x)
    for v in y:
        yield([v])
    yield(False,v)

fig, ax = plt.subplots()

def update(num):
    ax.clear()
    ax.set_title("|")
    if num[0]:
        ax.pie(nums, labels=labels, startangle=num[0]*720, colors = colors)
    else:
        _, l = ax.pie(nums, labels=labels, startangle=num[1]*720, colors = colors)
        l[winner[len(labels)]].set_color("red")




ani = FuncAnimation(fig, update, frames=yieldn(), repeat=False, interval = 30)
plt.show()
