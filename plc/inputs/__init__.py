from plc import PLC_base


class PLC_input_interrupt(PLC_base):
    FALLING = 0
    RISING = 1


class PLC_input(PLC_base):
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

        direction = PLC_input_interrupt.RISING if tmp else PLC_input_interrupt.FALLING
        self._value = tmp
        self.__interrupt__(tmp, direction)
