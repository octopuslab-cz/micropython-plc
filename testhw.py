from machine import I2C, Pin
from plc.inputs.virtual import PLCInputVirtual
from plc.drivers.octopus_plcshield import PLCOctopusLabShield

from plc.operands.op_not import PLCOperandNOT

i2c = I2C(1, scl=Pin(16), sda=Pin(2), freq=100000)
i2c.scan()

def on_value_change(cls, value, direction):
    print("Handle change on {} to {}".format(cls,value))

plc = PLCOctopusLabShield(i2c)

i1 = PLCInputVirtual(False)

plc_i2 = plc.inputs[1]
plc_o1 = plc.outputs[0]

plc_i2.add_event_on_change(on_value_change)
plc_o1.add_event_on_change(on_value_change)

nt = PLCOperandNOT(plc_i2)
nt.add_event_on_change(on_value_change)

plc_o1.set_input(nt)


while True:
    plc_i2.read()
