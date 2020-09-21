from pyo import *
import keyboard

s = Server().boot()

sound_dir = r"D:\Squirx_D\Music\Lego Island\Lego Island Cassetes v3"
path = sound_dir + r"\Police Station.wav"

path2 = sound_dir + r"\Cave Theme.wav"

sf = SfPlayer(path, loop=True, mul=0.4).out()
sf_cave = SfPlayer(path2).out()

s.start()
keyboard.wait('esc')
s.stop()