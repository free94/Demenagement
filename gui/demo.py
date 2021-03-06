from tkinter import *
from chart import *
import random, sys, math

def do(data, canvas, width, g, after=0):
  # swapr(data)
  canvas.delete('all')
  chart(data, canvas, width, g)
  canvas.update()
  root.after(after, do, data, canvas, width, g)

def randomize(size):
  data = {}
  for x in range(size):
    for y in range(size):
      data[(x, y)] = random.choice([random.random(), None])
  return data

def swapr(data):
  ri = lambda data: random.randint(0, math.sqrt(len(data)) - 1)
  r = [ri(data) for i in range(4)]
  d1, d2 = data[(r[0], r[1])], data[(r[2], r[3])]
  data[(r[0], r[1])], data[(r[2], r[3])] = d2, d1

def onmove(event, canvas):
  s = 100
  lx, ly = event.x - s, event.y - s
  ux, uy = event.x + s, event.y + s
  canvas.create_rectangle(lx, ly, ux, uy)
  for d in canvas.find_enclosed(lx, ly, ux, uy):
    canvas.itemconfig(d, fill='#000')

size = 32
csize = 640
data = randomize(size)

root = Tk()
root.wm_title('Window')
canvas = Canvas(root, width=csize, height=csize)
canvas.pack()
# canvas.bind('<Motion>', lambda event : onmove(event, canvas))
do(data, canvas, csize, gradients['green to red'])
mainloop()
