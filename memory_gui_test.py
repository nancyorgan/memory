from __future__ import division, unicode_literals
import pyglet
import cocos
import random
from cocos.actions import *
from cocos.director import director
from cocos.layer import base_layers

image_files = ['resources/cat.png', 'resources/rabbit.png', 'resources/deer.png',
               'resources/worm.png', 'resources/martha.png', 'resources/planet.png']
blank_file = 'resources/blank.png'

class Cards(object):
    def __init__(self, image_file, blank_file):
        self.image = cocos.sprite.Sprite(pyglet.image.load(image_file))
        self.blank = cocos.sprite.Sprite(pyglet.image.load(blank_file))
        self.unique_id = image_file
        self.image.opacity = 0


def build_deck(options, height, width):
     cards = random.sample(options, ((height*width)/2))*2
     shuffled = random.sample(cards, len(cards))
     x_position = []
     for i in range(width):
         x_position.append(40 + (120/2) + 120*i + 20*i)
     x_position = [x for x in x_position for _ in range(height)]
     y_position = []
     for i in range(height):
         y_position.append(40 + (120/2) + 120*i + 20*i)
     y_position = y_position*width
     deck = zip(shuffled, x_position, y_position)
     print deck
     print len(deck)

class Martha(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self, deck):
        super( Martha, self).__init__(0,0,0,255)
        # Set up event handling from previous MouseDisplay() class
        self.deck = deck
        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label(font_size=18, x=10, y=10)# , color = (0,0,0,0))
        self.add( self.text )

        label = cocos.text.Label('Matching Martha',
            font_name='Courier',
            font_size=32,
            anchor_x='center', anchor_y='center')
        label.position = 320,440
        self.add( label )

        positions = [(150,300), (300,300), (450,300), (150,150), (300,150), (450,150)]
        for position, card in zip(positions, deck):
            card.blank.position = position
            card.image.position = position
            self.add(card.blank)
            self.add(card.image)

    def update_text (self, x, y):
        in_sprite = False
        for card in deck:
            if card.blank.contains(x,y):
                text = 'IN SPRITE'
                self.text.element.text = text
                self.text.element.x = 10
                self.text.element.y = 10
                in_sprite = True
        if not in_sprite:
            text = 'Mouse @ %d,%d' % (x, y)
            self.text.element.text = text
            self.text.element.x = 10
            self.text.element.y = 10

    def on_mouse_motion (self, x, y, dx, dy):
            self.update_text (x, y)

    def on_mouse_press (self, x, y, buttons, modifiers):
        for card in deck:
            if card.blank.contains(x,y) == True :
                card.image.opacity = 255

if __name__ == "__main__":
    cocos.director.director.init(resizable=True)
    deck = [Cards(file, blank_file) for file in image_files] #replace with real deck via deck function
    martha_layer = Martha(deck)
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

# Card deck global function
    # spacing
    # scrambling

# Main
    # create instance of card class by looping over file names
    # create instance of Martha and call add method on cards