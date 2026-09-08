import adafruit_pca9554
import board
import digitalio
import time


last_blink = time.monotonic()
LED_STATE = False
HB_PERIOD = 0.250  # in seconds
heartbeat_pin = None


def heartbeat_init() -> None:
    """Initialize Heartbeat LED."""
    global heartbeat_pin, last_blink
    last_blink = time.monotonic()

    board.I2C().deinit()
    i2c = board.I2C()
    tft_io_expander = dict(board.TFT_IO_EXPANDER)
    tft_io_expander["i2c_address"] = 0x27

    pcf = adafruit_pca9554.PCA9554(i2c, address=tft_io_expander['i2c_address'])
    hb = pcf.get_pin(board.BTN_UP)
    heartbeat_pin = hb
    heartbeat_pin.switch_to_output(LED_STATE)


def heartbeat() -> None:
    """Blink LED if enough time has passed."""
    global heartbeat_pin, last_blink, LED_STATE

    time_to_blink = False
    current_time = time.monotonic()

    # overflow
    if current_time < last_blink:
        time_to_blink = True
    
    # blink period elapsed
    if (current_time - last_blink) > HB_PERIOD:
        time_to_blink = True
    
    if time_to_blink:
        heartbeat_pin.switch_to_output(not LED_STATE)
        LED_STATE = not LED_STATE
        last_blink = current_time