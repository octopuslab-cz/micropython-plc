from plc.operands.op_and import PLCOperandAND, PLCOperandNAND
from plc.operands.op_or import PLCOperandOR, PLCOperandNOR
from plc.operands.op_not import PLCOperandNOT
from plc.inputs.virtual import PLCInputVirtual
from plc.outputs.virtual import PLCOutputVirtual
from plc.elements.rs import PLCElementRS


a = PLCOperandAND()
na = PLCOperandNAND()
or1 = PLCOperandOR()
nor1 = PLCOperandNOR()
rs1 = PLCElementRS()

i1 = PLCInputVirtual(False, "vI1")
i2 = PLCInputVirtual(False, "vI2")
i3 = PLCInputVirtual(True, "vI3")
i4 = PLCInputVirtual(True, "vI4")

o1 = PLCOutputVirtual(a, "vO1")


def testint(inp, value, direction):
    print("Input {} changed to {} direction {}".format(inp, value, direction))


print("Input 1: {}".format(i1.output))
print("Input 2: {}".format(i2.output))
print("Input 3: {}".format(i3.output))
print("Input 4: {}".format(i4.output))

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

rs1.set = i1
rs1.reset = i2

print("AND: {}".format(a.output))
print("NAND: {}".format(na.output))
print("NOT: {}".format(nt.output))
print("OR: {}".format(or1.output))
print("NOR: {}".format(nor1.output))

i1.value = True
i1.value = False

i2.value = True
i2.value = False

i1.value = True
i2.value = True

print("AND: {}".format(a.output))
print("NAND: {}".format(na.output))
print("NOT: {}".format(nt.output))
print("OR: {}".format(or1.output))
print("NOR: {}".format(nor1.output))

i2.value = True

print("AND: {}".format(a.output))
print("NAND: {}".format(na.output))
print("NOT: {}".format(nt.output))
print("OR: {}".format(or1.output))
print("NOR: {}".format(nor1.output))
