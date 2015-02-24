#from __future__ import division, unicode_literals
import pyglet
import cocos
import random
from cocos.actions import *
from cocos.director import director
from cocos.layer import base_layers

image_files = ['resources/cat.png', 'resources/rabbit.png', 'resources/deer.png',
               'resources/worm.png', 'resources/martha.png', 'resources/planet.png']
blank_file = 'resources/blank.png'
button = 'resources/button.png'

counter = 0

class Cards(object):
    def __init__(self, image_file, blank_file):
        self.image = cocos.sprite.Sprite(pyglet.image.load(image_file))
        self.blank = cocos.sprite.Sprite(pyglet.image.load(blank_file))
        self.image_file = image_file
        self.image.opacity = 0

class Hand(object):
    def __init__(self, image_files, height, width):
        self.height = height
        self.width = width

        cards = random.sample(image_files, int((height*width)/2))*2
        shuffled = random.sample(cards, len(cards))
        self.shuffled = shuffled

        sprite_size = 100

        x_position = []
        for i in range(width):
            spacex = (640 - (sprite_size*width + 5*(width - 1)))/2
            x_position.append(spacex + (sprite_size/2) + sprite_size*i + 5*i)
        x_position = [x for x in x_position for _ in range(height)]

        y_position = []
        for i in range(height):
            spacey = (640 - (sprite_size*height + 5*(height - 1)))/2
            y_position.append(spacey + (sprite_size/2) + sprite_size*i + 5*i)
        y_position = y_position*width

        self.posxy = zip(x_position, y_position)

class Martha(cocos.layer.ColorLayer):
    """
    here is a dostrimgg

    """
    is_event_handler = True
    def __init__(self, hand, cards):
        super( Martha, self).__init__(0,0,0,255)
        # Set up event handling from previous MouseDisplay() class
        self.hand = hand
        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label(font_size=18, x=10, y=10 , color = (0,0,0,0))
        self.add( self.text )
        self.click = []
        self.click1 = []
        self.click2 = []

        label = cocos.text.Label('Matching Martha',
            font_name='Courier',
            font_size=32,
            anchor_x='center', anchor_y='center')
        label.position = 320,650
        self.add( label )

        self.score = cocos.text.Label(font_size=24, x=320, y=30)
        self.add(self.score)

        self.button = cocos.sprite.Sprite(pyglet.image.load(button))
        self.button.position = 320, 600
        #self.add(self.button)

        for posxy, card in zip(hand.posxy, cards):
            card.blank.position = posxy
            card.image.position = posxy
            self.add(card.blank)
            self.add(card.image)

    #refer to cards instead of to file_name
    def on_mouse_press(self, x, y, buttons, modifiers):
        global counter
        for card in cards:
            if card.blank.contains(x,y) and card.image.opacity == 0:
                card.image.opacity = 255
                counter += 1
                print "Counter is at: %s" % counter
                self.click.append(card)
                if counter == 3 and self.click[0].image_file != self.click[1].image_file:
                    for card in self.click:
                        card.image.opacity = 0
                    counter = 0
                    self.click = []

                elif counter == 3 and self.click[0].image_file == self.click[1].image_file:
                    counter = 1
                    self.click = []
                    self.click.append(card)
                print self.click




if __name__ == "__main__":
    cocos.director.director.init(height = 690, width = 640)
    hand = Hand(image_files, 3, 4)
    cards = [Cards(file, blank_file) for file in hand.shuffled]
    #for i in hand.shuffled:
    #    cards.append(Cards(i, blank_file))
    martha_layer = Martha(hand, cards)
    main_scene = cocos.scene.Scene(martha_layer)
    cocos.director.director.run(main_scene)
