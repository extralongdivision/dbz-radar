import time

class RepeatTimer:
    """
    Notify if a certain amount of time has elapsed.
    May trigger before period if internal timer overflows.
    Always will trigger after period.
    """

    def __init__(self, period: int = 1):
        self._period = None
        self._last_time = time.monotonic()

        self.set_period(period)

    def set_period(self, period: int) -> None:
        """Set the timer period."""
        self._period = period
    
    def expired(self) -> bool:
        """Returns if elapsed time has expired."""
        expired = False

        current_time = time.monotonic()

        # overflow
        if current_time < self._last_time:
            expired = True

        # timer exlapsed
        if (current_time - self._last_time) > self._period:
            expired = True
        
        if expired:
            self._last_time = current_time
        return expired
        
