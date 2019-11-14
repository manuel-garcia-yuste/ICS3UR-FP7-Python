#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : November 2019
# Circuit python 6


import ugame
import stage
import constants


def menu_scene():
    # menu
    NEW_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\ \n
                   xff\xff\xff\xff\xff\xff\xff\xff\xff'
                   b'\xff\xff\xff\xff\xff\xff\xff\xff\ \n
                   xff\xff\xff\xff\xff\xff\xff\xff')

    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)
    sprites = []

    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=NEW_PALETTE,
                       buffer=None)
    text1.move(20, 30)
    text1.text("MT GAME STUDIOS")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=NEW_PALETTE,
                       buffer=None)
    text2.move(35, 80)
    text2.text("PRESS START")
    text.append(text2)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + sprites + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        # print (keys)

        if keys & ugame.K_START != 0:
            game_scene()


def game_scene():
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

    a_button = constants.button_state["button_up"]

    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)

    sprites = []

    ship = stage.Sprite(image_bank_1, 5, int(constants.SCREEN_X / 2 -
                        constants.SPRITE_SIZE / 2),
                        int(constants.SCREEN_Y - constants.SPRITE_SIZE +
                        constants.SPRITE_SIZE / 2))
    sprites.append(ship)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = sprites + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        # print (keys)

        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_RIGHT != 0:
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + 1, ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)

        # if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    menu_scene()
