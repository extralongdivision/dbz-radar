import audiobusio
import audiocore
import board

from utils import RepeatTimer


class Beeper:
    """Beeper sound control."""

    def __init__(self):
        i2s_bit_pin = board.A0
        i2s_word_pin = board.RX
        i2s_data_pin = board.A1
        self._player = audiobusio.I2SOut(i2s_bit_pin, i2s_word_pin, i2s_data_pin)

        beep_fin = open("beep-short.wav", "rb")
        self._beep = audiocore.WaveFile(beep_fin)

        BEEP_PERIOD = 2  # in seconds
        self._audio_timer = RepeatTimer(period = BEEP_PERIOD)

    def tick(self) -> None:
        """Beep if enough time has passed"""
        if self._audio_timer.expired():
            self._player.play(self._beep)
            while self._player.playing:
                pass
