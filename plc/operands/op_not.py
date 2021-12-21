from plc.operands import PLCOperand


class PLCOperandNOT(PLCOperand):
    def __init__(self, input):
        self._input = input


    @property
    def output(self):
        return not self._input.output
