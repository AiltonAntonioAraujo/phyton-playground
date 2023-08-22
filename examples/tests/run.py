from calculadora import Calculadora
from operations.add import AddOperation
from operations.sub import SubOperation

calc = Calculadora(AddOperation(), SubOperation())
op1 = calc.add(2, 5, True)
op2 = calc.sub(5, 3, False)

print(op1)
print(op2)