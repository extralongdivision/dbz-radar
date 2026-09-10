"""Process Button"""
import microcontroller

from digitalio import DigitalInOut, Direction, Pull



class UserButton:
    """Processes Button Pushes."""

    def __init__(self):
        self._pressed = True
        self._active_val = False  # active low
        self._was_pressed = False

        self._button = DigitalInOut(microcontroller.pin.GPIO4)
        self._button.direction = Direction.INPUT
        self._button.pull = Pull.UP

    def is_just_pressed(self) -> bool:
        """Check if button was pressed at any point in time since last checking."""
        self.is_pressed()
        return_value = self._was_pressed # utils.copy(self._was_pressed)
        self._was_pressed = False
        return return_value

    def is_pressed(self) -> bool:
        """Check if button is pressed right now."""
        # store old state
        old_pressed = self._pressed

        # check if button is currently pressed
        self._pressed = self._button.value is self._active_val

        # set flag if button was just pressed
        if self._pressed and old_pressed is not self._pressed:
            self._was_pressed = True

        return self._pressed
