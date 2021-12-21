from plc.inputs import PLCInput

class PLCInputVirtual(PLCInput):
    def __init__(self, value=0):
        super().__init__()
        self._value = value


    @property
    def value(self):
        return self._value


    @value.setter
    def value(self, value):
        self._value = value
