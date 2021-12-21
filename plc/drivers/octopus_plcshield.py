# Driver for OctopusLab PLC shield

from plc import PLCBase
from plc.inputs import PLCInput
from plc.outputs import PLCOutput
from plc.drivers.i2cexpander import I2CExpander, ExpanderPin



class PLCOctopusLabShield(PLCBase):
    def __init__(self, i2c):
        self._i2c = i2c
        self._expander = I2CExpander(self._i2c, 0x22, 8)
        self.inputs = [PLCInputPin(x) for x in self._expander[0:4]]
        self.outputs = [PLCOutputPin(x) for x in self._expander[4:8]]


class PLCPin():
    def __init__(self, pin):
        self._pin = pin
    
    @property
    def value(self):
        return self._pin.value
    
    @value.setter
    def value(self, value):
        self._pin.value = value



class PLCOutputPin(PLCPin, PLCOutput):
    def __init__(self, pin):
        PLCPin.__init__(self, pin)
        PLCOutput.__init__(self)
        self.add_interrupt(self.__handle_interrupt)
    
    def __handle_interrupt(self, obj, value, direction):
        print("Output changed to {}".format(value))
        self.value = value


class PLCInputPin(PLCPin, PLCInput):
    def __init__(self, pin):
        PLCPin.__init__(self, pin)
        PLCInput.__init__(self)


    def read(self):
        self._value = self._pin.value
