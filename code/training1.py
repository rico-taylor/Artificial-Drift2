import pyglet
#create windows
def two():
  window = pyglet.window.Window(width=1280, height=720, caption="Hello Pyglet")
  window.set_location(400,200)

window = pyglet.window.Window(width=1280, height=720, caption="Hello Pyglet")
window.set_location(400,200)

#creating a batch object
batch = pyglet.graphics.Batch()

#defining shapes
circle = pyglet.shapes.Circle(x=700, y=150, radius=100, color=(50, 255, 30), batch=batch)

square = pyglet.shapes.Rectangle(x=200, y=200, width=200, height = 200, color = (255, 22, 20), batch=batch)

rectangle = pyglet.shapes.Rectangle(x=250, y=300, width=400, height=200, color = (55, 22, 200), batch=batch)
rectangle.opacity = 100
rectangle.rotation = 33

line = pyglet.shapes.Line(x=100, y=200, x2=100, y2=570, color=(255,255,255), width=19, batch=batch)

star = pyglet.shapes.Star(x=800, y=400, outer_radius=100, inner_radius=30, num_spikes=30, color=(255, 255, 0), batch=batch)

@window.event
def on_draw():
  #window.clear()
  #circle.draw()
  #square.draw()
  #line.draw()
  #rectangle.draw()
  #star.draw()
  batch.draw()






pyglet.app.run()


