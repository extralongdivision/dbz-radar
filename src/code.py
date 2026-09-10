from audio import Beeper
from button import UserButton
from display import display_init
from heartbeat import Heartbeat

button = UserButton()
heartbeat = Heartbeat()
display_init()
beeper = Beeper()

while True:
    heartbeat.tick()
    beeper.tick()
    button.is_pressed()
    if button.is_just_pressed():
        print("Doing something cool")
    pass  # infinite loop to keep image on display
