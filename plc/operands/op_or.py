from plc.operands import PLCOperand


class PLCOperandOR(PLCOperand):
    def __init__(self, inputs=None):
        self._inputs = inputs or list()


    def add_input(self, input):
        self._inputs.append(input)


    @property
    def output(self):
        for i in self._inputs:
            val = i.output
            if val:
                return True

        return False


class PLCOperandNOR(PLCOperandOR):
    @property
    def output(self):
        return not super().output
