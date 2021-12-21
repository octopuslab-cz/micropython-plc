from plc import PLCBase, PLCInterrupt


class PLCInput(PLCBase):
    def __init__(self):
        self.__value = None
        self._on_change_events = []


    def _on_change_event(self, value, direction):
        for f in self._on_change_events:
            f(self, value, direction)


    def add_event_on_change(self, func):
        self._on_change_events.append(func)


    def remove_event_on_change(self, func):
        if func in self._on_change_events:
            del self._on_change_events[func]


    @property
    def output(self):
        return self.value


    @property
    def _value(self):
        return self.__value


    @_value.setter
    def _value(self, value):
        tmp = bool(value)
        if tmp == self.__value:
            return

        direction = PLCInterrupt.RISING if tmp else PLCInterrupt.FALLING
        self.__value = tmp
        self._on_change_event(tmp, direction)
