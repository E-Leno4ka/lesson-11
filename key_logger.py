import keyboard

def f(event):
    f = ()

if __name__ == "__main__":
    print("Кейлогер запущен. Нажмите ESC для остановки")
    keyboard.on_press(f)
    keyboard.wait("esc")