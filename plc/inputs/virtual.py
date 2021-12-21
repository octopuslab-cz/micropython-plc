from plc.inputs import PLC_input

class PLC_input_virtual(PLC_input):
    def __init__(self, value=0):
        super().__init__()
        self.value = value

