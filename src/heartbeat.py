import adafruit_pca9554
import board
import digitalio

from utils import RepeatTimer

LED_STATE = False
HB_PERIOD = 0.250  # in seconds
heartbeat_pin = None
hearteat_timer = RepeatTimer(HB_PERIOD)


class Heartbeat:
    """Heartbeat LED control"""

    def __init__(self):
        self._led_state = False
        self._period = 0.25  # in seconds
        self._timer = RepeatTimer(self._period)

        self.pca9554_set(self._led_state)

    def pca9554_set(self, val: bool) -> None:
        """Set IO pin of PCA95544."""
        board.I2C().deinit()
        i2c = board.I2C()
        tft_io_expander = dict(board.TFT_IO_EXPANDER)
        tft_io_expander["i2c_address"] = 0x27

        pcf = adafruit_pca9554.PCA9554(i2c, address=tft_io_expander['i2c_address'])
        self._heartbeat_pin = pcf.get_pin(board.BTN_UP)
        self._heartbeat_pin.switch_to_output(val)

    def pca9554_toggle(self) -> None:
        self.pca9554_set(not self._led_state)

    def tick(self) -> None:
        """Blink LED if enough time has passed."""

        if self._timer.expired():
            self.pca9554_toggle()
            self._led_state = not self._led_state