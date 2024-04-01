import keyboard

def on_key_event(e):
    print(e.name)

keyboard.on_press(on_key_event)

keyboard.wait('esc')