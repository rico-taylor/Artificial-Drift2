import pyglet
from pyglet import sprite, image
from pyglet.window import key

from math import sin, cos, radians

window = pyglet.window.Window(width=1780, height=580, caption="Images")

logo_image = image.load("images/logo_finished.png")
car_image = image.load("images/car.png")

car_image.anchor_x = car_image.width // 2
car_image.anchor_y = car_image.height // 2

logo = sprite.Sprite(logo_image, x=1, y=1)
car = sprite.Sprite(car_image, x=40, y=40)
car.scale = 0.1
car.rotation = 1

forward = False
backward = False
aclockwise = False
clockwise = False

drive_speed = 7
rotation_speed = 4

@window.event
def on_draw():
  window.clear()
  logo.draw()
  car.draw()

@window.event
def on_key_press(symbol, modifiers):
  global forward
  global backward
  global clockwise
  global aclockwise

  if symbol == key.UP:
    forward = True
  if symbol == key.DOWN:
    backward = True

  if symbol == key.LEFT:
    aclockwise = True
  if symbol == key.RIGHT:
    clockwise = True

@window.event
def on_key_release(symbol, modifiers):
  global forward
  global backward
  global clockwise
  global aclockwise
  
  if symbol == key.UP:
    forward = False
  if symbol == key.DOWN:
    backward = False
  if symbol == key.LEFT:
    aclockwise = False
  if symbol == key.RIGHT:
    clockwise = False

def update(dt):
  if forward == True:
    car.y += drive_speed * cos(radians(car.rotation))
    car.x += drive_speed * sin(radians(car.rotation))
  if backward == True:
    car.y -= drive_speed * cos(radians(car.rotation))
    car.x -= drive_speed * sin(radians(car.rotation))
  
  if forward == True or backward == True: ##should be changed to if drive_speed > 0 once acceleration is added.
    if aclockwise == True:
      car.rotation -= rotation_speed
    if clockwise == True:
      car.rotation += rotation_speed

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()