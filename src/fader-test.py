from pyo import *

s = Server().boot()
s.amp = 0.1

# Infinite sustain for the global envelope.
globalamp = Fader(fadein=2, fadeout=2, dur=4).play()

a = Sine(440, mul=globalamp).out()
b = Sine(220, phase=0.5, mul=globalamp).out()

s.gui(locals())


