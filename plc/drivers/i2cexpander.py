## Generic driver for I2C I/O expander

class I2CExpander():
    def __init__(self, i2c, address=0x20, bussize=8):
        self._i2c = i2c
        self._address = address
        self._bussize = bussize
        self._pins = dict()
        self._read_port()


    def _read_port(self):
        port_value = self._i2c.readfrom(self._address, self._bussize // 8)
        value = port_value[0]

        if self._bussize > 8:
            value += port_value[1] << 8

        self._value = value
        return self._value


    def _write_port(self):
        tmp = bytearray(self._bussize // 8)
        tmp[0] = self._value
        if self._bussize > 8:
            tmp[1] = self._value >> 8

        self._i2c.writeto(self._address, tmp)


    def pin_value(self, pin_num, value = None):
        self._read_port()
        if value is None:
            mask = 0x1 << pin_num
            pin_val = self._value & mask
            return 1 if pin_val == mask else 0

        pin_val = 0x1 << pin_num

        if value:
            self._value |= pin_val
        else:
            self._value &= ~pin_val

        self._write_port()


    def __getitem__(self, pin):
        if type(pin) == slice:
            tmp = []
            for p in range(pin.start, pin.stop, pin.step or 1):
                tmp.append(self.__getitem__(p))
            return tmp

        if not pin in self._pins:
            self._pins[pin] = ExpanderPin(pin, self)
        return self._pins[pin]


class ExpanderPin():
    def __init__(self, pin, expander):
        self._pin = pin
        self._exp = expander

    @property
    def value(self):
        return self._exp.pin_value(self._pin)

    @value.setter
    def value(self, value):
        self._exp.pin_value(self._pin, value)
