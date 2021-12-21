from plc.outputs import PLCOutput

class PLCOutputVirtual(PLCOutput):
    def __init__(self, input):
        super().__init__(input)

        self.add_interrupt(self.__handle_interrupt)
    
    def __handle_interrupt(self, obj, value, direction):
        print("Output changed to {}".format(value))
