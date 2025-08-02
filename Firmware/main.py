# I am aware that one direction of the knob does not work, I am unsure on how to fix this, please make a PR if you find out how.

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Tap, Release
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

macros = Macros()
encoder_handler = EncoderHandler()
keyboard.modules = [macros, encoder_handler]
keyboard.extensions.append(MediaKeys())

PINS = [board.D2, board.D4, board.D6, board.D1, board.D5, board.D3, board.D9]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)
encoder_handler.pins = ((board.D8, board.D7),)


# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
print(KC.Macro)


keyboard.keymap = [
    [
        KC.MACRO(Press(KC.LCTL), Tap(KC.A), Release(KC.LCTL)),
        KC.MACRO(Press(KC.LCTL), Tap(KC.X), Release(KC.LCTL)),
        KC.MACRO(Press(KC.LCTL), Tap(KC.C), Release(KC.LCTL)),
        KC.MACRO(Press(KC.LCTL), Tap(KC.S), Release(KC.LCTL)),
        KC.MACRO(Press(KC.LCTL), Tap(KC.Z), Release(KC.LCTL)),
        KC.MACRO(Press(KC.LCTL), Tap(KC.Y), Release(KC.LCTL)),
        KC.MACRO(Tap(KC.MUTE)),
    ]
]

encoder_handler.map = [
    [ [KC.VOLU], [KC.VOLD] ]
]



if __name__ == '__main__':
    
    keyboard.go()
    

