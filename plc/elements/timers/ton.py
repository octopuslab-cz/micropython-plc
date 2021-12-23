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
        self._start_time = None
        self.delay = delay



    def __on_input_change(self, input, value, dir):
        if value:
            self._start()
        else:
            self._stop()
            self._amount = 0
            self._value = False


    def _start(self):
        if self._kill_thread:
            print("Thread still running, not running new one")
            return

        _thread.start_new_thread(self._loop, ())


    def _stop(self):
        self._kill_thread = True


    def _loop(self):
        self._start_time = ticks_ms()
        print("Loop thread started at {} AM:{} DL:{}".format(self._start_time, self._amount, self.delay))

        while not self._kill_thread:
            self._amount = ticks_ms() - self._start_time

            if self._amount >= self.delay:
                self._value = True
                break

        self._kill_thread = False
        print("Loop thread stopped at {}".format(self._start_time))
                

    @property
    def accum(self):
        return self._amount


    @property
    def delay(self):
        return self._delay


    @delay.setter
    def delay(self, delay):
        if not delay:
            raise ValueError()
        
        self._delay = delay

