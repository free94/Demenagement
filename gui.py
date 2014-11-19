from tkinter import *
from chart import *
from main import *
from prog import *
import random, sys, math

def do(canvas, width, g, after=0):
  round()
  canvas.delete('all')
  data = normalize(matrixCriteria(matrix, criterias['income']))
  chart(data, canvas, width, g)
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

def onkey(event, canvas, width, g):
    round()
    canvas.delete('all')
    data = normalize(matrixCriteria(matrix, criterias['type']))
    chart(data, canvas, width, g)
    canvas.update()

args = parser()
main.sizeMatrix = args.sizeM
main.sizeMaxAccomodation = args.sizeAccomodation
main.percentOfFamilies = args.families/100
size = args.sizeW
main.distanceFunction = args.distance
init()

root = Tk()
root.wm_title('Window')
canvas = Canvas(root, width=size, height=size)
canvas.pack()
# canvas.bind('<Motion>', lambda event : onmove(event, canvas))
# root.bind('<Key>', lambda event : onkey(event, canvas, size, gradients['types']))
layer = StringVar(root)
layers = [c for c in criterias.keys()]
layer.set(layers[0])
layers = OptionMenu(root, layer,*layers)
layers.pack()
do(canvas, size, gradients['types'])

mainloop()
