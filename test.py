from plc.operands.op_and import PLCOperandAND, PLCOperandNAND
from plc.operands.op_or import PLCOperandOR, PLCOperandNOR
from plc.operands.op_not import PLCOperandNOT
from plc.inputs.virtual import PLCInputVirtual
from plc.outputs.virtual import PLCOutputVirtual


a = PLCOperandAND()
na = PLCOperandNAND()
or1 = PLCOperandOR()
nor1 = PLCOperandNOR()

i1 = PLCInputVirtual(False)
i2 = PLCInputVirtual(1)
i3 = PLCInputVirtual(True)
i4 = PLCInputVirtual(True)

o1 = PLCOutputVirtual(a)


def testint(inp, value, direction):
    print("Input {} changed to {} direction {}".format(inp, value, direction))
    o1.update()


print("Input 1: {}".format(i1.value))
print("Input 2: {}".format(i2.value))
print("Input 3: {}".format(i3.value))
print("Input 4: {}".format(i4.value))

i1.add_event_on_change(testint)

a.add_input(i1)
a.add_input(i2)
a.add_input(i3)

na.add_input(i1)
na.add_input(i2)
na.add_input(i3)

or1.add_input(i1)
or1.add_input(a)
nor1.add_input(i1)
nor1.add_input(a)

nt = PLCOperandNOT(a)

print("AND: {}".format(a.output))
print("NAND: {}".format(na.output))
print("NOT: {}".format(nt.output))
print("OR: {}".format(or1.output))
print("NOR: {}".format(nor1.output))

i1.value = True

print("AND: {}".format(a.output))
print("NAND: {}".format(na.output))
print("NOT: {}".format(nt.output))
print("OR: {}".format(or1.output))
print("NOR: {}".format(nor1.output))
