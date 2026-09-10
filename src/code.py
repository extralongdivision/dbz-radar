from audio import Beeper
from button import UserButton
from display import Display
from heartbeat import Heartbeat

button = UserButton()
heartbeat = Heartbeat()

#
# FIXME this should really be a state machine...
#

class AppState:
    """Different App States."""
    IDLE = 1
    WAKEUP = 2
    SENSING = 3


display = Display()
beeper = Beeper()
state = AppState.IDLE


while True:
    heartbeat.tick()
    if button.is_just_pressed():
        if state == AppState.IDLE:
            print("IDLE->WAKEUP")
            state = AppState.WAKEUP
        elif state == AppState.SENSING:
            print("SENSING->IDLE")
            display.clear()
            state = AppState.IDLE

    if state == AppState.WAKEUP:
        print("Waking up...")
        beeper.tick()
        display.radar_bg()
        print("WAKEUP->SENSING")
        state = AppState.SENSING
    elif state == AppState.SENSING:
        beeper.tick()
