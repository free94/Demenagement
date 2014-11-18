from tkinter import *
from chart import *
from main import *
import random, sys, math

def do(canvas, width, g, after=0):
  round()
  canvas.delete('all')
  chart(normalize(matrixCriteria(matrix, criterias['type'])), canvas, width, g)
  canvas.update()
  root.after(after, do, canvas, width, g)

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

def onmove(event, canvas):
  s = 100
  lx, ly = event.x - s, event.y - s
  ux, uy = event.x + s, event.y + s
  canvas.create_rectangle(lx, ly, ux, uy)
  for d in canvas.find_enclosed(lx, ly, ux, uy):
    canvas.itemconfig(d, fill='#000')

csize = 640

init()

root = Tk()
root.wm_title('Window')
canvas = Canvas(root, width=csize, height=csize)
canvas.pack()
# canvas.bind('<Motion>', lambda event : onmove(event, canvas))
layer = StringVar(root)
layers = [c for c in criterias.keys()]
layer.set(layers[0])
layers = OptionMenu(root, layer,*layers)
layers.pack()
do(canvas, csize, gradients['types'])
mainloop()
