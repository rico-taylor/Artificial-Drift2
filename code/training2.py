import pyglet
from math import sin, cos

window = pyglet.window.Window(width=1280, height=720, caption="Hello Pyglet")
window.set_location(x=400, y=200)

#create a batch object
batch = pyglet.graphics.Batch()

#define shapes
circle = pyglet.shapes.Circle(x=250, y=300, radius=100, color=(50,225,30), batch=batch)

rectangle = pyglet.shapes.Rectangle(x=550, y=300, width=200, height=200, color=(255, 22, 20), batch=batch)
rectangle.anchor_position = (100, 100) # this is relative to the rectangle' x, y position

star = pyglet.shapes.Star(x=1000, y=300, outer_radius=60, inner_radius=40, num_spikes=8, color=(255, 255, 0), batch=batch)



@window.event
def on_draw():
  window.clear()
  batch.draw()

value = 0

def update(dt):
  global value
  value += 0.05
  circle.radius += sin(value)
  rectangle.rotation += 1
  star.rotation += 2

  star.x += cos(value) * 8
  star.y += sin(value) * 8
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()