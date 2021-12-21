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
    # Because micropython does not allow calling super().output property
    # This ugly hack must be done
    @property
    def output(self):
        for i in self._inputs:
            val = i.output
            if val:
                return False

        return True
