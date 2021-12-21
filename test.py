from plc.operands.op_and import PLC_operand_AND, PLC_operand_NAND
from plc.operands.op_or import PLC_operand_OR, PLC_operand_NOR
from plc.operands.op_not import PLC_operand_NOT
from plc.inputs.dummy import PLC_input_dummy
from plc import Override_DYNAMIC


a = PLC_operand_AND()
na = PLC_operand_NAND()
or1 = PLC_operand_OR()

i1 = PLC_input_dummy(True)
od1 = Override_DYNAMIC(i1)
i2 = PLC_input_dummy(0)
i3 = PLC_input_dummy("asd")
i4 = PLC_input_dummy(True)

print("Input 1: {}".format(i1.value))
print("Input 2: {}".format(i2.value))
print("Input 3: {}".format(i3.value))
print("Input 4: {}".format(i4.value))

a.add_input(i1)
a.add_input(i2)
a.add_input(i3)

na.add_input(i1)
na.add_input(i2)
na.add_input(i3)

or1.add_input(od1)
or1.add_input(a)

nt = PLC_operand_NOT(a)

print("AND: {}".format(a.output))
print("NAND: {}".format(na.output))
print("NOT: {}".format(nt.output))
print("OR: {}".format(or1.output))
print("OD: {}".format(od1.output))


i4._value = False
od1.enabled = True
print("OR: {}".format(or1.output))
od1.value = False
print("OR: {}".format(or1.output))
od1.enabled = False
print("OR: {}".format(or1.output))
