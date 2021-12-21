# PLC main module
# Input / Output
# Operand_AND / Operand_NAND / Operand_OR

class PLCBase():
    pass


class PLCException(Exception):
    pass


class PLCInterrupt(PLCBase):
    FALLING = 0
    RISING = 1


class PLCOverride(PLCBase):
    def __init__(self, input, enabled=False, value=False):
        self._input = input
        self._enabled = enabled
        self._value = value


    @property
    def enabled(self):
        return self._enabled


    @enabled.setter
    def enabled(self, en):
        self._enabled = en


    @property
    def output(self):
        if self._enabled:
            return self._value
        else:
            return self._input.output


    @property
    def value(self):
        return self._value


    @value.setter
    def value(self, value):
        self._value = value
