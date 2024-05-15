import pyglet
from pyglet import shapes
from pyglet.window import mouse

window = pyglet.window.Window(width=1280,height=720, caption ="Hello pyglet")
window.set_location(x=400, y=200)
window.set_mouse_visible(False)

#create a batch object
batch = pyglet.graphics.Batch()

#define the shapes to be drawn and add them to the batch
circle1 = shapes.Circle(x=700, y=150, radius=10, color=(50,255,30), batch=batch)
circle2 = shapes.Circle(x=100, y=150, radius=25, color=(255, 0,0), batch=batch)

@window.event 
def on_draw():
  window.clear()
  batch.draw()

@window.event 
def on_mouse_motion(x:int, y:int, dx:int, dy:int):
  circle1.position = (x,y)

@window.event 
def on_mouse_press(x:int, y:int, button:int, modifier:int):
  if button == mouse.LEFT:
    circle2.position = (x,y)

pyglet.app.run()