from plc import PLCBase


class PLCOperand(PLCBase):
    def inputs(self):
        raise NotImplementedError()


    @property
    def output(self):
        raise NotImplementedError()
