from plc.operands import PLCOperand


class PLCOperandNOT(PLCOperand):
    def __init__(self, input, name=None):
        super().__init__(name)
        self._input = input


    @property
    def output(self):
        return not self._input.output
