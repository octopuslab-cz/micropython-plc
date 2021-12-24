from time import sleep

from plc.operands.op_not import PLCOperandNOT
from plc.inputs.virtual import PLCInputVirtual
from plc.outputs.virtual import PLCOutputVirtual
from plc.elements.rs import PLCElementRS
from plc.elements.timers.ton import PLCTimerOn
from plc.elements.timers.tof import PLCTimerOff

i1 = PLCInputVirtual(False, "vI1")
toff = PLCTimerOff(i1, 2000, "Timer 1")
o1 = PLCOutputVirtual(toff, "vO1")


for i in range(20):
    toff.loop()
    print("Timer DN:{} EN: {} TT: {} Accum: {}".format(toff.output, toff.enabled.output, toff.activated.output, toff.accum))
    if i == 2:
        i1.value = True

    if i == 6:
        i1.value = False

    
    sleep(0.5)
