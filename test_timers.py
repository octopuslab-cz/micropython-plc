from plc.operands.op_not import PLCOperandNOT
from plc.inputs.virtual import PLCInputVirtual
from plc.outputs.virtual import PLCOutputVirtual
from plc.elements.rs import PLCElementRS
from plc.elements.timers.ton import PLCTimerOn


def testint(inp, value, direction):
    print("Input {} changed to {} direction {}".format(inp, value, direction))


rs1 = PLCElementRS()
ton = PLCTimerOn(rs1, 2000, "Timer 1")

i1 = PLCInputVirtual(False, "vI1")
i2 = PLCInputVirtual(False, "vI2")
o1 = PLCOutputVirtual(ton, "vO1")

rs1.set = i1
rs1.reset = i2

nt = PLCOperandNOT(ton)

from time import sleep
for i in range(12):
    print("Timer DN:{} NDN:{} Accum: {}".format(ton.output, nt.output, ton.accum))
    if i == 2:
        i1.value = True
        i1.value = False

    if i == 8:
        i2.value = True

    
    sleep(0.5)
