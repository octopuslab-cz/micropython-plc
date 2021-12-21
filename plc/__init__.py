# PLC main module
# Input / Output
# Operand_AND / Operand_NAND / Operand_OR

class PLCBase():
    pass


class PLCException(Exception):
    pass


class Output():
    def set_value(self):
        raise "Not implemented"

    def get_value(self):
        raise "Not implemented"


class PLCOverride(PLCBase):
    def __init__(self, input):
        self._input = input
        self._value = False
        self._enabled = False

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

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
