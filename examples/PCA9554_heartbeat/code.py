import time
import board
import digitalio
import adafruit_pca9554

board.I2C().deinit()
i2c = board.I2C()
tft_io_expander = dict(board.TFT_IO_EXPANDER)
tft_io_expander["i2c_address"] = 0x27

pcf = adafruit_pca9554.PCA9554(i2c, address=tft_io_expander['i2c_address'])
heartbeat = pcf.get_pin(board.BTN_UP)
heartbeat.switch_to_output(False)  # initialize heartbeat LED off

while True:
    heartbeat.switch_to_output(True)
    time.sleep(0.250)
    heartbeat.switch_to_output(False)
    time.sleep(0.250)
