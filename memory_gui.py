#from __future__ import division, unicode_literals
import os, sys
import pyglet
import cocos
import random
from cocos.actions import *
from cocos.layer import base_layers
from cocos.director import director
from cocos.layer import Layer, ColorLayer
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.sprite import Sprite
from pyglet import gl, font
from pyglet.window import key
#################### Global Variables #################

image_files = ['resources/cat.png', 'resources/rabbit.png', 'resources/deer.png',
               'resources/worm.png', 'resources/martha.png', 'resources/planet.png']
blank_file = 'resources/blank.png'
button = 'resources/button.png'
counter = 0
score = 0

#######################################################

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
        sprite_size = (480 - 5*(width-1))/width
        self.sprite_size = sprite_size

        x_position = []
        for i in range(width):
            x_position.append(80 + (sprite_size/2) + sprite_size*i + 5*i)
        x_position = [x for x in x_position for _ in range(height)]

        y_position = []
        for i in range(height):
            y_position.append(80 + (sprite_size/2) + sprite_size*i + 5*i)
        y_position = y_position*width

        self.posxy = zip(x_position, y_position)

class Martha(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self, hand, cards):
        super( Martha, self).__init__(0,0,0,255)

        self.hand = hand
        self.click = []

        label = cocos.text.Label('Matching Martha',
            font_name='Courier',
            font_size=32,
            anchor_x='center', anchor_y='center')
        label.position = 320,650
        self.add( label )

        self.scorelabel = cocos.text.Label("Score: %s" % str(score),
            font_name = "Courier",
            font_size=24,
            y = director.get_window_size()[1] - 100,
            x = director.get_window_size()[0]/2 - 100)
        self.add(self.scorelabel)

        for posxy, card in zip(hand.posxy, cards):
            card.blank.position = posxy
            card.image.position = posxy
            card.image.scale = hand.sprite_size/float(card.image.image.width)
            card.blank.scale = hand.sprite_size/float(card.blank.image.width)
            self.add(card.blank)
            self.add(card.image)

    def update_text (self, score):
        text = "Score: %s" % str(score)
        self.scorelabel.element.text = text
        self.scorelabel.element.y = director.get_window_size()[1] - 100
        self.scorelabel.element.x = director.get_window_size()[0]/2 - 100

    def on_mouse_press(self, x, y, buttons, modifiers):
        global counter, score
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
                    score -= 1
                    self.click = []
                    self.update_text(score)

                elif counter == 3 and self.click[0].image_file == self.click[1].image_file:
                    counter = 1
                    score += 2
                    self.click = []
                    self.click.append(card)
                    self.update_text(score)
                print self.click
                print score

class WelcomeScreen(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        super( WelcomeScreen, self).__init__(0,0,0,255)

        self.text_title = cocos.text.Label("Matching Martha",
                                font_size = 32,
                                font_name ='Courier',
                                y = director.get_window_size()[1] - 200,
                                x = director.get_window_size()[0]/2,
                                anchor_x = "center",
                                anchor_y = "center")

        self.text_subtitle = cocos.text.Label("Hit Enter to play!",
                                font_size=18,
                                font_name = 'Courier',
                                y = director.get_window_size()[1] - 300,
                                x = director.get_window_size()[0]/2,
                                anchor_x="center",
                                anchor_y="center")

    def draw(self):
        self.text_title.draw()
        self.text_subtitle.draw()

    def on_key_press(self, k, m):
        if k == key.ENTER:
            director.replace(FadeTransition(
                settings_scene,
                1)
            )

class Settings(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super(Settings, self).__init__()

        self.label = cocos.text.Label('Pick a name:',
            font_name='Courier',
            font_size=32,
            anchor_x='center', anchor_y='center',
            x = director.get_window_size()[0]/2,
            y = director.get_window_size()[1] - 200)

        self.text = cocos.text.Label("", x = director.get_window_size()[0]/2 - 30,
            y = director.get_window_size()[1] - 300,
            font_name = "Courier",
            font_size = 18,
            anchor_x='center')

        self.dim_label = cocos.text.Label('...and board size:',
            font_name='Courier',
            font_size=24,
            anchor_x='center', anchor_y='center',
            x = director.get_window_size()[0]/2,
            y = director.get_window_size()[1] - 400)

        self.dim_x = cocos.text.Label("", x = director.get_window_size()[0]/2 - 50,
            y = director.get_window_size()[1] - 500,
            font_name = "Courier",
            font_size = 24,
            anchor_x='center')

        self.by = cocos.text.Label("_____ x _____", x = director.get_window_size()[0]/2,
            y = director.get_window_size()[1] - 500,
            font_name = "Courier",
            font_size = 24,
            anchor_x='center')

        self.dim_y = cocos.text.Label("", x = director.get_window_size()[0]/2 + 50,
            y = director.get_window_size()[1] - 500,
            font_name = "Courier",
            font_size = 24,
            anchor_x='center')

        self.text_fields = [self.text, self.dim_x, self.dim_y]
        self.active_text_field_index = 0

    def draw(self):
        self.label.draw()
        self.text.draw()
        self.dim_label.draw()
        self.dim_x.draw()
        self.by.draw()
        self.dim_y.draw()

    def append_text_to_active_field(self, key_pressed):
        print "attempting to append ", key_pressed
        if (self.active_text_field_index == 1 or self.active_text_field_index == 2) and self.is_number(key_pressed):
            self.text_fields[self.active_text_field_index].element.text += self.key_press_to_char(key_pressed)
        else:
            self.text_fields[self.active_text_field_index].element.text += self.key_press_to_char(key_pressed)

    def key_press_to_char(self, key_pressed):
        if self.is_number(key_pressed):
            # if it's a number, subtract the key_pressed value for '0' and append
            return str(key_pressed - 48)
        else:
            return pyglet.window.key.symbol_string(key_pressed)

    def delete_text_from_active_field(self):
        # remove from the end of the active text field
        self.text_fields[self.active_text_field_index].element.text = \
            self.text_fields[self.active_text_field_index].element.text[:-1]

    def cycle_active_text_field(self):
        self.active_text_field_index = (self.active_text_field_index + 1) % 3
        print ("active text field: %s" % self.active_text_field_index)

    def is_number(self, k):
        return (k >= 48 and k <= 57)

    def on_key_press(self, k, m):
        print(k)
        if (k <= key.Z and k >= key.A) or self.is_number(k):
            self.append_text_to_active_field(k)

        elif k == key.BACKSPACE:
            self.delete_text_from_active_field()

        elif k == key.TAB:
            self.cycle_active_text_field()

        elif k == key.ENTER:
            director.replace(FadeTransition(
                main_scene, 1))

if __name__ == "__main__":
    cocos.director.director.init(height = 690, width = 640)

    welcome = WelcomeScreen()
    settings = Settings()

    #hand = Hand(image_files, height = int(settings.dim_x.element.text), width = int(settings.dim_y.element.text))
    hand = Hand(image_files, height = 3, width = 4)
    cards = [Cards(file, blank_file) for file in hand.shuffled]
    martha = Martha(hand, cards)

    welcome_scene = cocos.scene.Scene(welcome)
    settings_scene = cocos.scene.Scene(settings)
    main_scene = cocos.scene.Scene(martha)

    cocos.director.director.run(welcome_scene)