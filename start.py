#!/usr/bin/env python3
# Soubor:  kameny.py
# Datum:   06.11.2018 10:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################
import pyglet
import random
import glob


# from pyglet.window.key import LEFT, RIGHT, UP, DOWN, LCTRL
# from pyglet.window.mouse import LEFT as MouseLEFT

import pyglet.window.key
import pyglet.window.mouse

FPS = 32

window = pyglet.window.Window(width=800, height=600)
batch = pyglet.graphics.Batch()  # pro optimalizované vyreslování objektů


class SpaceObjects(pyglet.sprite.Sprite):
    speed_x = 0
    speed_y = 0
    speed_modifier = 1

    def __init__(self, img_path: str, speed_x = 0, speed_y = 0, position_x = 0, position_y = 0, batch=batch):
        self.img = pyglet.image.load(img_path)
        super().__init__(img=self.img, batch=batch)
        
        self.speed_x = speed_x
        self.speed_y = speed_y

        self.img = pyglet.image.load(img_path)
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2

    def move(self, dt: float):
        self.x += self.speed_x * dt * FPS/2 * self.speed_modifier
        self.y += self.speed_y * dt * FPS/2 * self.speed_modifier

        if self.x > (window.width - self.img.width):
            self.x = window.width - self.img.width
            self.speed_x = -self.speed_x

        elif self.y > (window.height - self.img.height):
            self.y = window.height - self.img.height
            self.speed_y = -self.speed_y
        
        elif self.x < 0:
            self.x = 0
            self.speed_x = -self.speed_x

        elif self.y < 0:
            self.y = 0
            self.speed_y = -self.speed_y

class Meteor(SpaceObjects):
    img_path = None

    def __init__(self, position_x, position_y, batch):
        super().__init__(self.img_path, batch=batch)
        self.x = position_x
        self.y = position_y

        self.speed_x = random.randint(1,10)
        self.speed_y = random.randint(1,10)

class MeteorBrown(Meteor):
    img_path = "img/meteorBrown_big1.png"

class MeteorGray(Meteor):
    img_path="img/meteorGrey_big1.png"
    speed_modifier = 2

@window.event
def on_draw():
    
    window.clear()
    batch.draw()

@window.event
def on_key_press(sym, mod):
    print(sym, mod)

@window.event
def on_key_release(sym, mod):
    print(sym, mod)
"""
@window.event
def on_mouse_press(x, y, button, mod):
    print(x, y, button)
    ship.x = x
    ship.y = y
"""
def tick(dt):
    for Object in Objects:
        Object.move(dt)
    
Objects = []
Meteors = [MeteorBrown, MeteorGray]
for _ in range(16):
    Type = random.choice(Meteors)
    Object = Type(position_x = random.randint(0,600), position_y = random.randint(0,800), batch=batch)
    Objects.append(Object)

# funkce tick se spustí 30x za sekundu
pyglet.clock.schedule_interval(tick, 1 / FPS)

# nekonečná smyčka ve které se čeká na události, které se následně obsluhují
pyglet.app.run()
