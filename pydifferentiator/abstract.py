from abc import ABC, abstractmethod

class expression(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self) -> float:
        pass

    def e(self) -> float:
        return self.evaluate()

    @abstractmethod
    def deriviate(self, var : 'variable') -> 'expression':
        pass

    def d(self, var : 'variable') -> 'expression':
        return self.deriviate(var)

    @abstractmethod
    def isConstant(self) -> bool:
        pass
    
    def __neg__(self) -> 'expression':
        return neg(self)
    
    def neg(self) -> 'expression':
        return neg(self)

    def __add__(self, other) -> 'expression':
        return add(self, other)

    def add(self, other) -> 'expression':
        return add(self, other)
    
    def __radd__(self, other) -> 'expression':
        return add(other, self)

    def __sub__(self, other) -> 'expression':
        return sub(self, other)

    def sub(self, other) -> 'expression':
        return sub(self, other)
    
    def __rsub__(self, other) -> 'expression':
        return sub(other, self)

    def __mul__(self, other) -> 'expression':
        return mul(self, other)

    def mul(self, other) -> 'expression':
        return mul(self, other)

    def __rmul__(self, other) -> 'expression':
        return mul(other, self)

    def __truediv__(self, other) -> 'expression':
        return div(self, other)

    def div(self, other) -> 'expression':
        return div(self, other)

    def __rtruediv__(self, other) -> 'expression':
        return div(other, self)

    def __pow__(self, other) -> 'expression':
        return pow(self, other)

    def pow(self, other) -> 'expression':
        return pow(self, other)

    def __rpow__(self, other) -> 'expression':
        return pow(other, self)
    
    def exp(self) -> 'expression':
        return exp(self)
    
    def log(self) -> 'expression':
        return log(self)
    

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


# Include for all the basic functions
from .math_basic import *