# In this example we will make Toliet FAN delay
# When light will turn on we will wait 5 seconds and turn on FAN.
# After turn off light we will wait another 10 seconds before turn off FAN

# Wiring
#   DI2 - Switch
#   DO1 - Light
#   DO2 - FAN
#
#   DO3 - Timer On active
#   DO4 - Timer Off active


# Logical diagram
# ================
#
#                    --[TON EN:bit]----------------->[LIGHT:DO1]
#                   /
#[SW:DI2]--+-->[TON 5sec]-->[OR]-->[TOFF 10sec]--+-->[FAN:DO2]
#          |                  ^                  |
#          |                  |                  |
#           \ -------------->[AND]<--------------/



from machine import I2C, Pin
from plc.drivers.octopus_plcshield import PLCOctopusLabShield

from plc.elements.timers.ton import PLCTimerOn
from plc.elements.timers.tof import PLCTimerOff

from plc.operands.op_and import PLCOperandAND
from plc.operands.op_or import PLCOperandOR

print("Init I2C")
i2c = I2C(1, scl=Pin(16), sda=Pin(2), freq=100000)
i2c.scan()

print("Init PLC")
plc = PLCOctopusLabShield(i2c)

print("Init PLC Inputs")
# Switch input
plc_i2 = plc.inputs[1]


print(("Init PLC Outputs"))

# Light output (optional, can be connected directly to switch)
plc_o1 = plc.outputs[0]

# FAN output
plc_o2 = plc.outputs[1]

# Diag outputs
plc_o3 = plc.outputs[2]
plc_o4 = plc.outputs[3]


# Start up delay timer - 5sec - DI2 input
ton = PLCTimerOn(plc_i2, 5000, "FAN-ON")

# OR operand to turn Off timer
or1 = PLCOperandOR()

# Turn off delay timer - 10 sec - Timer On input
toff = PLCTimerOff(or1, 10000, "FAN-OFF")

# AND operand to keep FAN running if light is turn on again,
# but Delay On timer will not catch extend time
and1 = PLCOperandAND()
and1.add_input(plc_i2)
and1.add_input(toff)

or1.add_input(ton)
or1.add_input(and1)

# D1 copy input state (timer on enable status)
plc_o1.input = ton.enabled

# D2 output connected to Timer off
plc_o2.input = toff

# D3 output - timer on active
plc_o3.input = ton.activated

# D4 output - timer off active
plc_o4.input = toff.activated


print("Starting main loop")
while True:
    plc_i2.read()
    ton.loop()
    toff.loop()
