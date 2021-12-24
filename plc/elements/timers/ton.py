from utime import ticks_ms
from plc.elements.timers import PLCTimer


class PLCTimerOn(PLCTimer):
    def __init__(self, input, delay, name=None):
        super().__init__(name, input, delay)

    def _start(self):
        if self._active._value:
            return

        self._enabled._value = True


    def _stop(self):
        self._enabled._value = False
        self._active._value = False
        self._value = False
        self._amount = 0


    def loop(self):
        if not self._enabled._value:
            return

        if self._value:
            return

        if not self._active._value:
            self._start_time = ticks_ms()
            self._active._value = True
            print("Loop enabled at {} AM:{} DL:{}".format(self._start_time, self._amount, self.delay))

        self._amount = ticks_ms() - self._start_time

        if self._amount >= self.delay:
            self._value = True
            self._active._value = False
            print("Loop thread stopped after {}ms".format(ticks_ms() - self._start_time))
