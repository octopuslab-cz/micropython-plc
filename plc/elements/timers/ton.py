from utime import ticks_ms
import _thread

from plc import PLCBase
from plc.elements.timers import PLCTimer

class PLCTimerOn(PLCTimer):
    def __init__(self, input, delay, name=None):
        super().__init__(name)
        self._amount = 0
        self._kill_thread = False
        self._value = False
        input.add_event_on_change(self.__on_input_change)
        self._input = input
        self._enabled = PLCBase("{}:Enabled".format(self.name))
        self._active = PLCBase("{}:Active".format(self.name))
        self.delay = delay
        self._start_time = None


    def __on_input_change(self, input, value, dir):
        if value:
            self._start()
        else:
            self._stop()

            # Wait for thread to fiish
            while self._active.output:
                pass

            self._amount = 0
            self._value = False
            self._tt = False

        self._enabled._value = value


    def _start(self):
        _thread.start_new_thread(self._loop, ())


    def _stop(self):
        self._kill_thread = True


    def _loop(self):
        self._start_time = ticks_ms()
        self._active._value = True

        print("Loop thread started at {}".format(self._start_time))

        while not self._kill_thread:
            self._amount = ticks_ms() - self._start_time

            if self._amount >= self.delay:
                self._value = True
                self._stop()

        self._active._value = False
        print("Loop thread stopped at {}".format(self._start_time))
                

    @property
    def accum(self):
        return self._amount


    @property
    def active(self):
        return self._active


    @property
    def enabled(self):
        return self._enabled


    @property
    def delay(self):
        return self._delay


    @delay.setter
    def delay(self, delay):
        if not delay:
            raise ValueError()
        
        self._delay = delay

