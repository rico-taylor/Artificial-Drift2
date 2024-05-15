import pyglet
from pyglet.window import key

class MyWindow(pyglet.window.Window):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.set_location(x=400, y=200)
    self.set_minimum_size(width=400, height=300)
  
    self.batch = pyglet.graphics.Batch()
    self.circle = pyglet.shapes.Circle(x=640, y=360, radius=50, color=(50, 255, 30), batch = self.batch)

    self.directions = {'left': False, 'right': False, 'up': False, 'down': False}
    self.speed = 5
  
  def on_draw(self):
    self.clear()
    self.batch.draw()

  def on_key_press(self, symbol, modifiers):
    if symbol == key.LEFT:
      self.directions['left'] = True
    if symbol == key.RIGHT:
      self.directions['right'] = True
    if symbol == key.UP:
      self.directions['up'] = True
    if symbol == key.DOWN:
      self.directions['down'] = True

  def on_key_release(self, symbol, modifiers):
    if symbol == key.LEFT:
      self.directions['left'] = False
    if symbol == key.RIGHT:
      self.directions['right'] = False
    if symbol == key.UP:
      self.directions['up'] = False
    if symbol == key.DOWN:
      self.directions['down'] = False

  def update(self, dt):
    if self.directions['left']:
      self.circle.x -= self.speed
    if self.directions['right']:
      self.circle.x += self.speed
    if self.directions['up']:
      self.circle.y += self.speed
    if self.directions['down']:
      self.circle.y -= self.speed

window = MyWindow(width=1280, height=720, caption="Hello Pyglet", resizable=True)

pyglet.clock.schedule_interval(window.update, 1/60)


pyglet.app.run()