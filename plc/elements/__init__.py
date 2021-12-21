from plc import PLCBase


class PLCElement(PLCBase):
    def __init__(self, initialvalue=False):
        self._value = initialvalue

    @property
    def output(self):
        return self._value
