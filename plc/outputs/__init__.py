from plc import PLCBase, PLCInterrupt


class PLCOutput(PLCBase):
    def __init__(self, input=None, name=None):
        super().__init__(name)
        self._value = None
        input.add_event_on_change(self.__on_input_change)
        self._input = input


    def __on_input_change(self, input, value, dir):
        self.update()


    def update(self):
        if not self._input:
            return

        self._value = self._input.output
