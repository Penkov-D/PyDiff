import sys
sys.path.append('..\\')
sys.path.append('.\\')

from pydifferentiator import variable, expression
import matplotlib.pyplot as plt
import math

def factorial(x):
    return 1 if x <= 1 else x * factorial(x - 1)

x = variable(2.0)

f = x - (x **  3) / factorial( 3) \
      + (x **  5) / factorial( 5) \
      - (x **  7) / factorial( 7) \
      + (x **  9) / factorial( 9) \
      - (x ** 11) / factorial(11) \
      + (x ** 13) / factorial(13)

# f = x ** 3 / 4 + x ** 2

# f = math.e ** (- x ** 2)

f = x.pow(2).neg().exp()

fd = f.deriviate(x)
fdd = fd.deriviate(x)
fddd = fdd.deriviate(x)

line = [math.pi * x / 100 for x in range(-100, 101)]

vf = [(x.setValue(v), f.evaluate())[1] for v in line]
vfd = [(x.setValue(v), fd.evaluate())[1] for v in line]
vfdd = [(x.setValue(v), fdd.evaluate())[1] for v in line]
vfddd = [(x.setValue(v), fddd.evaluate())[1] for v in line]

plt.plot(line, vf, label = "$f(x)$")
plt.plot(line, vfd, label = "$f'(x)$")
plt.plot(line, vfdd, label = "$f''(x)$")
plt.plot(line, vfddd, label = "$f'''(x)$")

plt.title('$e^{-x^2}$')
plt.grid(True)
plt.legend()

plt.show()