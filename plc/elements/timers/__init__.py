# Base class for PLC Timers

from plc import PLCBase


class PLCTimer(PLCBase):
    def __init__(self, name, input, delay):
        super().__init__(name)
        self._enabled = PLCBase("{}:EN".format(self.name))
        self._active = PLCBase("{}:TT".format(self.name))

        input.add_event_on_change(self.__on_input_change)
        self._input = input

        self._start_time = None
        self._amount = 0
        self.delay = delay


    def __on_input_change(self, input, value, dir):
        if value:
            self._start()
        else:
            self._stop()


    def _start(self):
        raise NotImplementedError()


    def _stop(self):
        raise NotImplementedError()


    @property
    def accum(self):
        return self._amount


    @property
    def activated(self):
        return self._active


    @property
    def delay(self):
        return self._delay


    @delay.setter
    def delay(self, delay):
        if not delay:
            raise ValueError()

        self._delay = delay


    @property
    def enabled(self):
        return self._enabled
