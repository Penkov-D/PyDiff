from .abstract import expression_uno, expression_bin, variable, expression, constant
import math


class expression_neg(expression_uno):

    def evaluate(self) -> float:
        return -self._inner.evaluate()

    def deriviate(self, var : 'variable') -> 'expression':
        return -self._inner.deriviate(var)


class expression_add(expression_bin):

    def evaluate(self) -> float:
        return self._left.evaluate() + self._right.evaluate()

    def deriviate(self, var : 'variable') -> 'expression':
        return self._left.deriviate(var) + self._right.deriviate(var)


class expression_sub(expression_bin):

    def evaluate(self) -> float:
        return self._left.evaluate() - self._right.evaluate()

    def deriviate(self, var : 'variable') -> 'expression':
        return self._left.deriviate(var) - self._right.deriviate(var)


class expression_mul(expression_bin):

    def evaluate(self) -> float:
        return self._left.evaluate() * self._right.evaluate()

    def deriviate(self, var : 'variable') -> 'expression':
        return self._left * self._right.deriviate(var) + self._left.deriviate(var) * self._right


class expression_div(expression_bin):

    def evaluate(self) -> float:
        return self._left.evaluate() / self._right.evaluate()

    def deriviate(self, var : 'variable') -> 'expression':
        return (- self._left * self._right.deriviate(var) + self._left.deriviate(var) * self._right) / (self._right * self._right)


class log(expression_uno):

    def evaluate(self) -> float:
        return math.log(self._inner.evaluate())

    def deriviate(self, var : 'variable') -> 'expression':
        return self._inner.deriviate(var) / self._inner


class expression_pow(expression_bin):

    def evaluate(self) -> float:
        return self._left.evaluate() ** self._right.evaluate()

    def deriviate(self, var : 'variable') -> 'expression':

        if self._right.isConstant():
            if self._right.evaluate() == 1:
                return self._left.deriviate(var)
            else:
                return self._right * (self._left ** (self._right - 1)) * self._left.deriviate(var)

        return self * (log(self._left) * self._right).deriviate(var)

