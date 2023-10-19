import time
import threading
from pynput.mouse import Button, Controller
import keyboard

delay = 0.001 
button = Button.left 
start_key = "f6" 
exit_key = "f5" 

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

keyboard.add_hotkey(str(start_stop_key), click_thread.start_clicking)
keyboard.add_hotkey(str(exit_key), click_thread.exit)

keyboard.wait()
