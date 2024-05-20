import pyglet
from pyglet import sprite, image
from pyglet.window import key

from math import sin, cos, radians

window = pyglet.window.Window(width=2280, height=1580, caption="Images")

logo_image = image.load("images/track V4.png")
car_image = image.load("images/car.png")

car_image.anchor_x = car_image.width // 2
car_image.anchor_y = car_image.height // 2

logo = sprite.Sprite(logo_image, x=1, y=1)
car = sprite.Sprite(car_image, x=40, y=40)
car.scale = 0.1
logo.scale = 3
car.rotation = 1

forward = False
backward = False
aclockwise = False
clockwise = False

drift = False
backDict = {}

velocity = 0
max_velocity = 8
friction = 0.07
acceleration = 0.1
rotation_speed = 3

drift_time = 8
rounds = 0

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
  global drift
  global rounds
  global rotation_speed

  if symbol == key.UP:
    forward = True
  if symbol == key.DOWN:
    backward = True

  if symbol == key.LEFT:
    aclockwise = True
  if symbol == key.RIGHT:
    clockwise = True

  if symbol == key.LSHIFT or symbol == key.RSHIFT:
    drift = True
    rotation_speed = 4
    rounds = 0

@window.event
def on_key_release(symbol, modifiers):
  global forward
  global backward
  global clockwise
  global aclockwise
  global drift
  global rotation_speed

  if symbol == key.UP:
    forward = False
  if symbol == key.DOWN:
    backward = False
  if symbol == key.LEFT:
    aclockwise = False
  if symbol == key.RIGHT:
    clockwise = False
  if symbol == key.LSHIFT or symbol == key.RSHIFT:
    drift = False
    rotation_speed = 3

def update(dt):
  global velocity
  global rounds
  if velocity > 0:
    velocity -= friction
  if velocity < 0:
    velocity += friction
  if velocity > max_velocity:
    velocity = max_velocity
  if velocity < -max_velocity:
    velocity = -max_velocity

  if forward == True:
    velocity += acceleration
  if backward == True:
    velocity -= acceleration

  dy = velocity * cos(radians(car.rotation))
  dx = velocity * sin(radians(car.rotation))
  
  new = {dy:dx}
  backDict.update(new)
  if len(backDict) > drift_time:
    backDict.pop(list(backDict)[0])
  
  rounds += 1
  if drift == True:
    if rounds >= drift_time:
      car.y += list(backDict)[0]
      car.x += backDict[list(backDict)[1]]
    else:
      car.y += dy
      car.x += dx
  else:
    car.y += dy
    car.x += dx
  
  if forward == True or backward == True or velocity > friction or velocity < -friction:
    if aclockwise == True:
      car.rotation -= rotation_speed
    if clockwise == True:
      car.rotation += rotation_speed

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()