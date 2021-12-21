from plc import PLCBase, PLCInterrupt


class PLCInput(PLCBase):
    def __init__(self):
        self._value = None
        self._interrupts = []


    def __interrupt__(self, direction, value):
        for f in self._interrupts:
            f(self, direction, value)


    def add_interrupt(self, func):
        self._interrupts.append(func)


    @property
    def output(self):
        return self.value


    @property
    def value(self):
        return self._value


    @value.setter
    def value(self, value):
        tmp = bool(value)
        if tmp == self._value:
            return

        direction = PLCInterrupt.RISING if tmp else PLCInterrupt.FALLING
        self._value = tmp
        self.__interrupt__(tmp, direction)
