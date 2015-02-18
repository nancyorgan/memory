from __future__ import division, print_function, unicode_literals
import pyglet
import cocos
from cocos.actions import *
from cocos.director import director
from cocos.layer import base_layers

class HelloWorld(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        super( HelloWorld, self ).__init__(0,0,0,255)
        # Set up event handling from previous MouseDisplay() class
        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label(font_size=18, x=10, y=10)
        self.add( self.text )

        label = cocos.text.Label('Matching Martha',
            font_name='Courier',
            font_size=32,
            anchor_x='center', anchor_y='center')
        label.position = 320,440
        self.add( label )

        blank = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/blank.png')
        cat = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/cat.png')
        rabbit = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/rabbit.png')
        deer = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/deer.png')
        worm = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/worm.png')

        blank1 = cocos.sprite.Sprite(blank)
        blank2 = cocos.sprite.Sprite(blank)
        blank3 = cocos.sprite.Sprite(blank)
        blank4 = cocos.sprite.Sprite(blank)
        blank5 = cocos.sprite.Sprite(blank)
        blank6 = cocos.sprite.Sprite(blank)
        cat  = cocos.sprite.Sprite(cat)
        rabbit = cocos.sprite.Sprite(rabbit)
        deer = cocos.sprite.Sprite(deer)
        worm = cocos.sprite.Sprite(worm)

        blank1.position = 150,300
        blank2.position = 300,300
        blank3.position = 450,300
        blank4.position = 150,150
        blank5.position = 300,150
        blank6.position = 450,150

        cat.position = 150,300
        rabbit.positon = 300,300
        deer.position = 450,300


        self.add(blank1)
        self.add(blank2)
        self.add(blank3)
        self.add(blank4)
        self.add(blank5)
        self.add(blank6)
        self.add(cat)
        self.add(rabbit)
        self.add(deer)
        self.add(worm)

        self.blank1 = blank1
        self.blank2 = blank2
        self.blank3 = blank3
        self.blank4 = blank4
        self.blank5 = blank5
        self.blank6 = blank6
        self.cat = cat
        self.rabbit = rabbit
        self.deer = deer
        self.worm = worm

        cat.opacity = 0
        rabbit.opacity = 0
        deer.opacity = 0
        worm.opacity = 0


    def update_text (self, x, y):
        if self.blank1.contains(x,y) or \
                self.blank2.contains(x,y) or \
                self.blank3.contains(x,y) or \
                self.blank4.contains(x,y) or \
                self.blank5.contains(x,y) or \
                self.blank6.contains(x,y):
            text = 'IN SPRITE'
            self.text.element.text = text
            self.text.element.x = 10
            self.text.element.y = 10
        else:
            text = 'Nope'
            self.text.element.text = text
            self.text.element.x = 10
            self.text.element.y = 10

    def on_mouse_motion (self, x, y, dx, dy):
            self.update_text (x, y)

    def on_mouse_press (self, x, y, buttons, modifiers):
        #self.posx, self.posy = director.get_virtual_coordinates (x, y)
        if self.blank1.contains(x,y) == True :
            self.cat.opacity = 255
        if self.blank2.contains(x,y) == True :
            self.rabbit.opacity = 255
        if self.blank3.contains(x,y) == True :
            self.deer.opacity = 255

if __name__ == "__main__":
    cocos.director.director.init(resizable=True)
    # We create a new layer, an instance of HelloWorld
    hello_layer = HelloWorld ()
    main_scene = cocos.scene.Scene(hello_layer)
    cocos.director.director.run(main_scene)

