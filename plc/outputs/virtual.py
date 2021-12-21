from plc.outputs import PLCOutput

class PLCOutputVirtual(PLCOutput):
    def __init__(self, input):
        super().__init__(input)

        self.add_event_on_change(self._on_change)
    
    def _on_change(self, obj, value, direction):
        print("Output changed to {}".format(value))
