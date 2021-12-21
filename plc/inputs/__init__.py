from plc import PLCBase, PLCInterrupt


class PLCInput(PLCBase):
    def __init__(self):
        self.__value = None
        self._interrupts = []


    def __interrupt__(self, value, direction):
        for f in self._interrupts:
            f(self, value, direction)


    def add_interrupt(self, func):
        self._interrupts.append(func)


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
        self.__interrupt__(tmp, direction)
