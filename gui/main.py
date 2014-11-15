import chart

size = 640 # Taille du graphique
data = {} # Matrice de couples (x, y) de donnees

root = Tk()
root.wm_title('Window')
canvas = Canvas(root, width=csize, height=csize)
canvas.pack()
do(data, canvas, size, gradients['green to red'])
mainloop()

def do(data, canvas, width, g, after=0):
  # ...

  canvas.delete('all')
  chart(data, canvas, width, g)
  canvas.update()
  root.after(after, do, data, canvas, width, g)
