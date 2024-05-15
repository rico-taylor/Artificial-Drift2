import pyglet
from pyglet.window import key

window = pyglet.window.Window(width=1280, height=720, caption="Hello Pyglet")
window.set_location(x=400, y=200)

#creating a batch object
batch = pyglet.graphics.Batch()

#define the shapes to be brawn and add them to the batch
circle = pyglet.shapes.Circle(x=640, y=360, radius=50, color=(50, 225, 30), batch=batch)

@window.event 
def on_draw():
  window.clear()
  batch.draw()

directions = {'left':False, 'right':False, 'up':False, 'down':False}
speed = 10

@window.event
def on_key_press(symbol, modifiers):
  if symbol == key.LEFT:
    directions['left'] = True
  if symbol == key.RIGHT:
    directions['right'] = True
  if symbol == key.UP:
    directions['up'] = True
  if symbol == key.DOWN:
    directions['down'] = True

@window.event
def on_key_release(symbol, modifiers):
  if symbol == key.LEFT:
    directions['left'] = False
  if symbol == key.RIGHT:
    directions['right'] = False
  if symbol == key.UP:
    directions['up'] = False
  if symbol == key.DOWN:
    directions['down'] = False

def update(float):
  if directions['left'] == True:
    circle.x -=speed
  if directions['right'] == True:
    circle.x +=speed
  if directions['down'] == True:
    circle.y -=speed
  if directions['up'] == True:
    circle.y +=speed


pyglet.clock.schedule_interval(update, 1/60)

pyglet.app.run()