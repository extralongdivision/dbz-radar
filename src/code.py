from audio import Beeper
from button import UserButton
from display import display_bitmap, display_clear, display_init
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


display_init()
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
            display_clear()
            state = AppState.IDLE

    if state == AppState.WAKEUP:
        print("Waking up...")
        display_bitmap("/radar-bg.bmp")
        print("WAKEUP->SENSING")
        state = AppState.SENSING
    elif state == AppState.SENSING:
        beeper.tick()
