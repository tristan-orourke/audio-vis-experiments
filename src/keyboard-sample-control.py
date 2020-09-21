import keyboard
import pyo
import string
from os import listdir
from os.path import isfile, join

sound_dir = r"D:\Squirx_D\Music\Lego Island\Lego Island Cassetes v3"
sound_files = [f for f in listdir(sound_dir) if isfile(join(sound_dir, f)) and f.endswith(".wav")]

key_samples = {}
letters = list(string.ascii_lowercase)
for index, letter in enumerate(letters):
  key_samples[letter] = sound_files[index % len(sound_files)]

print(key_samples)

server = pyo.Server().boot()

players = []

output_string = []

def make_char_sound(name):
  path = join(sound_dir, key_samples[name])
  decay_amp = pyo.SigTo(value=0.0, time=2.0, init=1)
  sf = pyo.SfPlayer(path, mul=decay_amp)
  return sf

def make_new_word(name):
  path = join(sound_dir, key_samples[name])
  decay_amp = pyo.SigTo(value=0.0, time=4.0, init=1)
  sf = pyo.SfPlayer(path, mul=decay_amp)
  return pyo.Harmonizer(sf)

def make_sf_player(path):
  # Envelope for discrete events, sharp attack, long release.
  env = pyo.Adsr(attack=0.0, decay=0.1, sustain=0.5, release=1.5, dur=2, mul=0.5)
  sf = pyo.SfPlayer(path, mul=env)
  new_word = pyo.Harmonizer(sf)
  new_line = pyo.Sine(440, mul=env)
  return {'sf': sf, 'env': env, 'word': new_word, 'line': new_line}

key_outputs = {key: make_sf_player(join(sound_dir, f)) for (key, f) in key_samples.items()}
print(key_outputs)

def handle_keypress(keyboard_event):
  name = keyboard_event.name
  
  if name in key_outputs:
    sf = key_outputs[name]['sf']
    sf.stop()
    sf.out()

    if len(output_string) > 0 and output_string[-1] == "space":
      word = key_outputs[name]['word']
      word.stop()
      word.out

    if len(output_string) > 0 and output_string[-1] == "enter":
      line = key_outputs[name]['line']
      line.stop()
      line.out

    key_outputs[name]['env'].play()

  print(name)
  if name == 'esc':
    keyboard.unhook_all()
  
  output_string.append(name)

server.start()
keyboard.on_press(handle_keypress)
keyboard.wait('esc')
server.stop()