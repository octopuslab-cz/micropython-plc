from plc import PLCBase, PLCInterrupt


class PLCOutput(PLCBase):
    def __init__(self, input = None):
        self._value = None
        self._input = input
        self._on_change_events = []


    def _on_change_event(self, value, direction):
        for f in self._on_change_events:
            f(self, value, direction)


    def add_event_on_change(self, func):
        self._on_change_events.append(func)


    def remove_event_on_change(self, func):
        if func in self._on_change_events:
            del self._on_change_events[func]


    def set_input(self, input):
        self._input = input


    def update(self):
        if not self._input:
            return

        tmp = self._input.output
        if tmp == self._value:
            return

        direction = PLCInterrupt.RISING if tmp else PLCInterrupt.FALLING
        self._value = tmp
        self._on_change_event(tmp, direction)
