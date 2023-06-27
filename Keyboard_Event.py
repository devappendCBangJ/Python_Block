# ==============================================================
# 0. 라이브러리 불러오기
# ==============================================================
from pynput import keyboard

# ==============================================================
# 0. 함수 정의
# ==============================================================
def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(
            key.char))
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

def on_release(key):
    print('Key released: {0}'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# ==============================================================
# 1. Keyboard 값 받기
# ==============================================================
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
