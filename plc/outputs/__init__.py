from plc import PLCBase, PLCInterrupt


class PLCOutput(PLCBase):
    def __init__(self, input = None):
        self._value = None
        self._input = input
        self._interrupts = []


    def __interrupt__(self, value, direction):
        for f in self._interrupts:
            f(self, value, direction)


    def add_interrupt(self, func):
        self._interrupts.append(func)


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
        self.__interrupt__(tmp, direction)
