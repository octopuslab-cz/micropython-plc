from machine import I2C, Pin
from plc.inputs.virtual import PLCInputVirtual


i2c = I2C(1, scl=Pin(16), sda=Pin(2), freq=100000)
i2c.scan()

def input_interrupt(cls, value, direction):
    print("Handle change on {} to {}".format(cls,value))
    o1.update()


plc = PLCOctopusLabShield(i2c)

i1 = PLCInputVirtual(False)
o1 = plc.outputs[0]

plcin2 = plc.inputs[1]
plcin2.add_interrupt(input_interrupt)
o1.set_input(plcin2)


while True:
    plcin2.read()
