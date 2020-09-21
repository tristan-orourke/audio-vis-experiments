import keyboard
import pyo

note_freq = {
  'a': 220.00,
  'b': 233.08,
  'c': 246.94,
  'd': 261.63,
  'e': 277.18,
  'f': 293.66,
  'g': 311.13,
  'h': 329.63,
  'i': 349.23,
  'j': 369.99,
  'k': 392.00,
  'l': 415.30,
  'm': 440.00,
  'n': 466.16,
  'o': 493.88,
  'p': 523.25,
  'q': 554.37,
  'r': 587.33,
  's': 622.25,
  't': 659.25,
  'u': 698.46,
  'v': 739.99,
  'w': 783.99,
  'x': 830.61,
  'y': 880.00,
  'z': 932.33,
}

server = pyo.Server().boot()

sine = pyo.Sine(mul=0.1)
output = pyo.FM()

def handle_keypress(keyboard_event):
  name = keyboard_event.name
  
  if name in note_freq:
    output.carrier = note_freq[name]
    output.out()
  else:
    output.stop()

  print(name)
  if name == 'esc':
    keyboard.unhook_all()


server.start()
keyboard.on_press(handle_keypress)

output.ctrl(title="Frequency modulation controls")
server.gui(locals())

keyboard.wait('esc')
server.stop()