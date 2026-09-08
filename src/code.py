from audio import Beeper
from display import display_bitmap, display_init
from heartbeat import Heartbeat

heartbeat = Heartbeat()
display_init()
beeper = Beeper()

while True:
    heartbeat.tick()
    beeper.tick()
    pass  # infinite loop to keep image on display
