from plc import PLCBase, PLCInterrupt


class PLCOutput(PLCBase):
    def __init__(self, input = None):
        super().__init__()
        self._value = None
        self._input = input


    def set_input(self, input):
        self._input = input


    def update(self):
        if not self._input:
            return

        self._value = self._input.output
