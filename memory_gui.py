from __future__ import division, print_function, unicode_literals
import pyglet
import cocos
from cocos.actions import *
from cocos.director import director
from cocos.layer import base_layers

class HelloWorld(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        super( HelloWorld, self ).__init__(20,64,20,255)
        # Set up event handling from previous MouseDisplay() class
        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label('No mouse events yet', font_size=18, x=self.posx, y=self.posy )
        self.add( self.text )

        label = cocos.text.Label('This is a game.',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center')

        label.position = 320,440
        self.add( label )

        img1 = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/mola.png')
        img2 = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/mola.png')
        img3 = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/mola.png')
        img4 = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/mola.png')
        sprite1 = cocos.sprite.Sprite(img1)
        sprite2 = cocos.sprite.Sprite(img2)
        sprite3 = cocos.sprite.Sprite(img3)
        sprite4 = cocos.sprite.Sprite(img4)

        self.my_sprites = [sprite1, sprite2, sprite3, sprite4]

        sprite1.position = 200,350
        sprite2.position = 400,350
        sprite3.position = 200,150
        sprite4.position = 400,140
        self.add(sprite1)
        self.add(sprite2)
        self.add(sprite3)
        self.add(sprite4)

    def update_text (self, x, y):
        text = 'Mouse @ %d,%d' % (x, y)
        self.text.element.text = text
        self.text.element.x = self.posx
        self.text.element.y = self.posy

    def on_mouse_motion (self, x, y, dx, dy):
        self.update_text (x, y)

    def in_sprite (self, x, y):
        pass


    def on_mouse_drag (self, x, y, dx, dy, buttons, modifiers):
        self.update_text (x, y)

    def on_mouse_press (self, x, y, buttons, modifiers):
        self.posx, self.posy = director.get_virtual_coordinates (x, y)
        self.update_text (x,y)
        # add if to check if sprite contains point



if __name__ == "__main__":
    cocos.director.director.init(resizable=True)
    # We create a new layer, an instance of HelloWorld
    hello_layer = HelloWorld ()
    main_scene = cocos.scene.Scene(hello_layer)
    cocos.director.director.run(main_scene)

