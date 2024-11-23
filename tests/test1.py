import sys
sys.path.append('..\\')
sys.path.append('.\\')

import pydifferentiator as pyd

x = pyd.variable()
f = 2 * x + 3

print(f.evaluate())