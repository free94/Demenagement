from tkinter import *
from chart import *
import random, sys, math

def do(data, canvas, width, g, after=0):
  swapr(data)
  canvas.delete('all')
  chart(data, canvas, width, g)
  canvas.update()
  root.after(after, do, data, canvas, width, g)

def randomize(size):
  data = {}
  for x in range(size):
    for y in range(size):
      data[(x, y)] = random.random()
  return data

def swapr(data):
  ri = lambda data: random.randint(0, math.sqrt(len(data)) - 1)
  r = [ri(data) for i in range(4)]
  d1, d2 = data[(r[0], r[1])], data[(r[2], r[3])]
  data[(r[0], r[1])], data[(r[2], r[3])] = d2, d1

size = 32
csize = 640
data = randomize(size)

root = Tk()
root.wm_title('Window')
canvas = Canvas(root, width=csize, height=csize)
canvas.pack()
do(data, canvas, csize, gradients['green to red'])
mainloop()
