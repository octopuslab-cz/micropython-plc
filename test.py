from plc.operands.op_and import PLCOperandAND, PLCOperandNAND
from plc.operands.op_or import PLCOperandOR, PLCOperandNOR
from plc.operands.op_not import PLCOperandNOT
from plc.inputs.virtual import PLCInputVirtual
from plc import PLCOverrideDynamic


a = PLCOperandAND()
na = PLCOperandNAND()
or1 = PLCOperandOR()

i1 = PLCInputVirtual(True)
od1 = PLCOverrideDynamic(i1)
i2 = PLCInputVirtual(0)
i3 = PLCInputVirtual("asd")
i4 = PLCInputVirtual(True)


def testint(inp, value, direction):
    print("Input {} changed to {} direction {}".format(inp, value, direction))


print("Input 1: {}".format(i1.value))
print("Input 2: {}".format(i2.value))
print("Input 3: {}".format(i3.value))
print("Input 4: {}".format(i4.value))

i4.add_interrupt(testint)

a.add_input(i1)
a.add_input(i2)
a.add_input(i3)

na.add_input(i1)
na.add_input(i2)
na.add_input(i3)

or1.add_input(od1)
or1.add_input(a)

nt = PLCOperandNOT(a)

print("AND: {}".format(a.output))
print("NAND: {}".format(na.output))
print("NOT: {}".format(nt.output))
print("OR: {}".format(or1.output))
print("OD: {}".format(od1.output))


i4.value = False
od1.enabled = True
print("OR: {}".format(or1.output))
od1.value = False
print("OR: {}".format(or1.output))
od1.enabled = False
print("OR: {}".format(or1.output))
