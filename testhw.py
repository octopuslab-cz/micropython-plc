from machine import I2C, Pin
from plc.drivers.octopus_plcshield import PLCOctopusLabShield

from plc.elements.rs import PLCElementRS
from plc.elements.timers.ton import PLCTimerOn
from plc.elements.timers.tof import PLCTimerOff

from plc.operands.op_not import PLCOperandNOT

print("Init I2C")
i2c = I2C(1, scl=Pin(16), sda=Pin(2), freq=100000)
i2c.scan()

print("Init PLC")
plc = PLCOctopusLabShield(i2c)

print("Init PLC Inputs")
plc_i2 = plc.inputs[1]
plc_i3 = plc.inputs[2]


print(("Init PLC Outputs"))
plc_o1 = plc.outputs[0]
plc_o2 = plc.outputs[1]
plc_o3 = plc.outputs[2]
plc_o4 = plc.outputs[3]

# Simple NOTPL
#  Input 2
#  Output 1
nt = PLCOperandNOT(plc_i2)
plc_o1.input = nt

# Test timer 2 sec Power On Delay
#  Input 2
#  Output 2 timer Done bit (output)
#  Output 3 timer Enable bit
#  Output 4 timer Active bit
#rs1 = PLCElementRS(plc_i2, plc_i3)
#ton = PLCTimerOn(rs1, 2000, "TON1")
toff = PLCTimerOff(plc_i2, 2000, "TOFF1")

ton_nt_dn = PLCOperandNOT(toff, "NOT: DN")
plc_o2.input = ton_nt_dn

ton_nt_en = PLCOperandNOT(toff.enabled, "NOT: EN")
plc_o3.input = ton_nt_en

ton_nt_tt = PLCOperandNOT(toff.activated, "NOT: TT")
plc_o4.input = ton_nt_tt

while True:
    toff.loop()
    plc_i2.read()
#    ton.loop()
