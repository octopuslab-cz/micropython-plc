from plc import PLCBase, PLCInterrupt


class PLCOutput(PLCBase):
    def __init__(self, input):
        self._value = None
        self._input = input
        self._interrupts = []


    def __interrupt__(self, value, direction):
        for f in self._interrupts:
            f(self, value, direction)


    def add_interrupt(self, func):
        self._interrupts.append(func)


    def update(self):
        tmp = self._input.output
        if tmp == self._value:
            return

        direction = PLCInterrupt.RISING if tmp else PLCInterrupt.FALLING
        self._value = tmp
        self.__interrupt__(tmp, direction)


    @property
    def value(self):
        return self._value
