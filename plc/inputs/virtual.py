from plc.inputs import PLCInput

class PLCInputVirtual(PLCInput):
    def __init__(self, value=0):
        super().__init__()
        self.value = value
