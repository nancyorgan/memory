from __future__ import division, print_function, unicode_literals
import pyglet
import cocos
from cocos.actions import *
from cocos.director import director
from cocos.layer import base_layers

class Martha(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self, ):
        super( Martha, self).__init__(0,0,0,255)
        # Set up event handling from previous MouseDisplay() class
        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label(font_size=18, x=10, y=10) #, color = (0,0,0,0))
        self.add( self.text )

        label = cocos.text.Label('Matching Martha',
            font_name='Courier',
            font_size=32,
            anchor_x='center', anchor_y='center')
        label.position = 320,440
        self.add( label )


        ###### Load images and make sprites ######
        image_files = ['resources/cat.png',
                       'resources/rabbit.png', 'resources/deer.png',
                       'resources/worm.png']

        loaded_images = []
        for file in image_files:
            loaded_images.append(pyglet.image.load(file))

        print(loaded_images)

        blank = pyglet.image.load('resources/blank.png')
        #cat = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/cat.png')
        #rabbit = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/rabbit.png')
        #deer = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/deer.png')
        #worm = pyglet.image.load('/Users/nancyorgan/Documents/memory/resources/worm.png')

        sprites = []
        for image in loaded_images:
            sprites.append([cocos.sprite.Sprite(image), cocos.sprite.Sprite(blank)])

        #blank1 = cocos.sprite.Sprite(blank)
        #blank2 = cocos.sprite.Sprite(blank)
        #blank3 = cocos.sprite.Sprite(blank)
        ##blank4 = cocos.sprite.Sprite(blank)
        #blank5 = cocos.sprite.Sprite(blank)
        #blank6 = cocos.sprite.Sprite(blank)
        #cat  =   cocos.sprite.Sprite(cat)
        #rabbit = cocos.sprite.Sprite(rabbit)
        #deer = cocos.sprite.Sprite(deer)
        #worm = cocos.sprite.Sprite(worm)

        positions = [(150,300), (300,300), (450,300), (150,150), (300,150), (450,150)]
        for position, sprite in zip(positions, sprites):
            sprite[0].position = position
            sprite[1].position = position
            self.add(sprite[0])
            self.add(sprite[1])



       # sprints[0][0].position = 150, 300
       # sprints[0][0].position = 150, 300
       # blank1.position = 150,300
       # blank2.position = 300,300
       # blank3.position = 450,300
       # blank4.position = 150,150
       # blank5.position = 300,150
       # blank6.position = 450,150

        #cat.position = 150,300
        #rabbit.position = 300,150
        #deer.position = 450,300
        #worm.position = 150,150


        #self.add(blank1)
        #self.add(blank2)
        #self.add(blank3)
        #self.add(blank4)
        #self.add(blank5)
        #self.add(blank6)
        #self.add(cat)
        #self.add(rabbit)
        #self.add(deer)
        #self.add(worm)

        #self.blank1 = blank1
        #self.blank2 = blank2
        #self.blank3 = blank3
        #self.blank4 = blank4
        #self.blank5 = blank5
        #self.blank6 = blank6
        #self.cat = cat
        #self.rabbit = rabbit
        #self.deer = deer
        #self.worm = worm


        #cat.opacity = 0
        #rabbit.opacity = 0
        #deer.opacity = 0
        #worm.opacity = 0

        #animals = [cat, rabbit, deer, worm]
        #for a in animals:
        #    a.opacity = 0

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
        if self.blank5.contains(x,y) == True :
            self.rabbit.opacity = 255
        if self.blank3.contains(x,y) == True :
            self.deer.opacity = 255
        if self.blank4.contains(x,y) == True :
            self.worm.opacity = 255

if __name__ == "__main__":
    cocos.director.director.init(resizable=True)
    # We create a new layer, an instance of HelloWorld
    martha_layer = Martha()
    main_scene = cocos.scene.Scene(martha_layer)
    cocos.director.director.run(main_scene)


# Store images outside somewhere

# Martha layer class
    # label etc.
    # keep on_mouse_press
    # .add card method

# Card class
    # load images from resources folder
    # create sprite from image and blank
    # give position
    # find out which one was clicked using contains
    # give opacities, and method to change opacity with clicking


# Main
    # create instance of card class by looping over file names
    # create instance of Martha and call add method on cards