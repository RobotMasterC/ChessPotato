# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
encoder_handler = EncoderHandler()
keyboard.modules.append(macros)
keyboard.modules = [layers, holdtap, encoder_handler]

# Define your pins here!
PINS = [board.D2, board.D4, board.D6, board.D1, board.D5, board.D3]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)
encoder_handler.pins = (
    (board.D8, board.D7, board.D9)
    )

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md

keyboard.keymap = [
    [KC.Macro(Press(KC.LCTL), Tap(KC.A), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.X), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.C), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.S), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.Z), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.Y), Release(KC.LCTL)),]
]

encoder_handler.map = [((KC.UP, KC.DOWN, KC.MUTE),)]

# Start kmk!
if __name__ == '__main__':
    
    keyboard.go()
    
