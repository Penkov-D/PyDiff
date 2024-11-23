from abc import ABC, abstractmethod

class expression(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self) -> float:
        pass

    @abstractmethod
    def deriviate(self, var : 'variable') -> 'expression':
        pass

    @abstractmethod
    def isConstant(self) -> bool:
        pass
    
    def __neg__(self) -> 'expression':
        return expression_neg(self)

    def __add__(self, other) -> 'expression':
        return expression_add(self, other)
    
    def __radd__(self, other) -> 'expression':
        return expression_add(other, self)

    def __sub__(self, other) -> 'expression':
        return expression_sub(self, other)
    
    def __rsub__(self, other) -> 'expression':
        return expression_sub(other, self)

    def __mul__(self, other) -> 'expression':
        return expression_mul(self, other)

    def __rmul__(self, other) -> 'expression':
        return expression_mul(other, self)

    def __truediv__(self, other) -> 'expression':
        return expression_div(self, other)

    def __rtruediv__(self, other) -> 'expression':
        return expression_div(other, self)

    def __pow__(self, other) -> 'expression':
        return expression_pow(self, other)

    def __rpow__(self, other) -> 'expression':
        return expression_pow(other, self)
    


class expression_value(expression):

    def __init__(self, value : float = 0.0):
        self._value = value

    def setValue(self, value : float) -> None:
        self._value = value

    def getValue(self) -> float:
        return self._value


class constant(expression_value):
        
    def isConstant(self) -> bool:
        return True
    
    def evaluate(self) -> float:
        return self._value

    def deriviate(self, var : 'variable') -> 'expression':
        return constant(0.0)
    


class variable(expression_value):

    def isConstant(self) -> bool:
        return False
    
    def evaluate(self) -> float:
        return self._value

    def deriviate(self, var : 'variable') -> 'expression':
        return constant(1.0 if self is var else 0.0)



class expression_bin(expression):

    def __init__(self, left : expression, right : expression):
        self._left = left if isinstance(left, expression) else constant(left)
        self._right = right if isinstance(right, expression) else constant(right)

    def isConstant(self) -> bool:
        return self._left.isConstant() and self._right.isConstant()



class expression_uno(expression):

    def __init__(self, inner : expression):
        self._inner = inner if isinstance(inner, expression) else constant(inner)

    def isConstant(self) -> bool:
        return self._inner.isConstant()
    
    
from .operators import *
