# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import audiocore
import board
import audiobusio

wave_file = open("StreetChicken.wav", "rb")
wave = audiocore.WaveFile(wave_file)

# For Feather M0 Express, ItsyBitsy M0 Express, Metro M0 Express
# audio = audiobusio.I2SOut(board.D1, board.D0, board.D9)
# For Feather M4 Express
# audio = audiobusio.I2SOut(board.D1, board.D10, board.D11)
# For Metro M4 Express
# audio = audiobusio.I2SOut(board.D3, board.D9, board.D8)
i2s_bit_pin = board.A0
i2s_word_pin = board.RX
i2s_data_pin = board.A1
audio = audiobusio.I2SOut(i2s_bit_pin, i2s_word_pin, i2s_data_pin)

while True:
    audio.play(wave)
    while audio.playing:
        pass

