from utime import ticks_ms
from plc.elements.timers import PLCTimer


class PLCTimerOff(PLCTimer):
    def __init__(self, input, delay, name=None):
        super().__init__(name, input, delay)
        self._trigger = False

    def _start(self):
        self._amount = 0
        self._enabled._value = True
        self._active._value = False
        self._value = True
        self._trigger = False


    def _stop(self):
        self._enabled._value = False

        if self._value is None:
            self._value = False
            self._active._value = False

        if self._value:
            self._trigger = True


    def loop(self):
        if not self._trigger:
            return

        if not self._active._value:
            self._start_time = ticks_ms()
            self._active._value = True
            print("Loop enabled at {} AM:{} DL:{}".format(self._start_time, self._amount, self.delay))

        self._amount = ticks_ms() - self._start_time

        if self._amount <= self.delay:
            return

        print("Loop thread timeout after {}ms".format(ticks_ms() - self._start_time))
        self._value = False
        self._active._value = False
        self._trigger = False
        print("Loop thread stopped after {}ms".format(ticks_ms() - self._start_time))
