from display import display_bitmap, display_init
from heartbeat import heartbeat, heartbeat_init

heartbeat_init()
display_init()

display_bitmap("/round-display-ruler-720p.bmp")

while True:
    heartbeat()
    pass  # infinite loop to keep image on display