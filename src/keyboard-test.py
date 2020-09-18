import keyboard  # using module keyboard

def handle_keypress(keyboard_event):
  name = keyboard_event.name
  print(name)
  if name == 'esc':
    keyboard.unhook_all()

keyboard.on_press(handle_keypress)
keyboard.wait('esc')