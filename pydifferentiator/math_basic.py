from .abstract import expression, expression_bin, expression_uno
from .abstract import variable, constant
import math

# Euler constant
E = e = math.e


class neg(expression_uno):

    def evaluate(self) -> float:
        return -self._inner.evaluate()

    def deriviate(self, var : variable) -> expression:
        return -self._inner.deriviate(var)


class add(expression_bin):

    def evaluate(self) -> float:
        return self._left.evaluate() + self._right.evaluate()

    def deriviate(self, var : variable) -> expression:
        return self._left.deriviate(var) + self._right.deriviate(var)


class sub(expression_bin):

    def evaluate(self) -> float:
        return self._left.evaluate() - self._right.evaluate()

    def deriviate(self, var : variable) -> expression:
        return self._left.deriviate(var) - self._right.deriviate(var)


class mul(expression_bin):

    def evaluate(self) -> float:
        return self._left.evaluate() * self._right.evaluate()

    def deriviate(self, var : variable) -> expression:
        return self._left * self._right.deriviate(var)      \
             + self._left.deriviate(var) * self._right


class div(expression_bin):

    def evaluate(self) -> float:
        return self._left.evaluate() / self._right.evaluate()

    def deriviate(self, var : variable) -> expression:
        return (- self._left * self._right.deriviate(var)       \
                + self._left.deriviate(var) * self._right)      \
                / (self._right * self._right)


class log(expression_uno):

    def evaluate(self) -> float:
        return math.log(self._inner.evaluate())

    def deriviate(self, var : variable) -> expression:
        return self._inner.deriviate(var) / self._inner


class pow(expression_bin):

    def evaluate(self) -> float:
        return self._left.evaluate() ** self._right.evaluate()

    def deriviate(self, var : variable) -> expression:

        if self._right.isConstant():
            if self._right.evaluate() == 1:
                return self._left.deriviate(var)
            else:
                return self._right * (self._left ** (self._right - 1)) * self._left.deriviate(var)

        return self * (log(self._left) * self._right).deriviate(var)


class exp(expression_uno):

    def evaluate(self):
        return math.exp(self._inner.evaluate())
    
    def deriviate(self, var):
        return self * self._inner.deriviate(var)



