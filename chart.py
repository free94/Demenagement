import math

# Degrades
gradients = {
  'cyan to black' : [(0, 1, 1), (0, 1, 0), (1, 1, 0), (1, 0, 0), (0, 0, 0)],
  'blue to red'   : [(0, 0, 1), (0, 1, 1), (0, 1, 0), (1, 1, 0), (1, 0, 0)],
  'green to red'  : [(0, 1, 0), (1, 1, 0), (1, 0, 0)],
  'yellow to red' : [(1, 1, 0), (1, 0, 0)],
  'types'         : [(0, 0, 1), (0, 0, 0), (1, 0, 0)]
}

def normalize(data):
  """
  Nomaliser les valeur d'une liste de donnees entre 0 et 1
  data : matrice de donnees
  """
  values = []
  values = {d for d in data.values() if d is not None}
  l, u = min(values), max(values)
  return {p: None if d is None else (d - l) / (u - l) for p, d in data.items()}

def chart(data, canvas, width, colors=[(0, 0, 0), (1, 1, 1)], default=(0, 0, 0), highlight=False, border=1):
  """
  Tracer des donnees
  data : matrice de donnees
  canvas : support tkinter.Canvas
  colors : liste de point d'arrets au format (r, v, b)
  border : eppaisseur en pixels de la bordure au survol
  """
  s = width / math.sqrt(len(data))
  for p, d in data.items():
    c = '#%02x%02x%02x' % (default if d is None else tuple(c * 255 for c in color(colors, d)))
    draw(p, canvas, s, c, border, '#fff' if highlight else c, '#fff', d)

def draw(position, canvas, size, color, border, outline, active, tags):
  """
  Tracer une donnee
  position : couple de coordonees (x, y)
  canvas : support tkinter.Canvas
  size : taille en pixels de la donnee
  border : eppaisseur en pixels de la bordure
  outline : couleur en hexadecimal de la bordure
  active : couleur en hexadecimal de la bordure au survol
  """
  canvas.create_rectangle(
    position[0] * size + border, position[1] * size + border,
    position[0] * size + size, position[1] * size + size,
    width=border, activeoutline=active, fill=color, outline=outline,
    tags=('data', tags)
  )

def color(g, v):
  """
  Obtenir la couleur correspondante a une valeur dans un degrade
  g : liste de point d'arrets au format (r, v, b)
  v : valeur reelle dans l'intervalle [0, 1]
  """
  s = 1 / (len(g) - 1)
  c = 0
  while v > s:
    c += 1
    v -= s
  start, end = g[c], g[c + 1]
  ch = lambda c1, c2, i: c1 + i * (c2 - c1)
  v /= s
  return (
    ch(start[0], end[0], v),
    ch(start[1], end[1], v),
    ch(start[2], end[2], v)
  )
