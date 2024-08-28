
class DemoPlainClass:
    a: int
    b: float = 1.1
    c = 'spam'

#print(DemoPlainClass.a)
#nao consegue instanciar pois o que for herdado de object nao aceita parametro no construtor, necessario overload

print(DemoPlainClass.b)
print(DemoPlainClass.c)

print(DemoPlainClass.__annotations__)

from typing import NamedTuple

class DemoNTClass(NamedTuple):
  a: int
  b: float = 1.1
  c = 'spam'

print(DemoNTClass.__annotations__)

t= DemoNTClass(a=1, b=2.0)

print(t.a)

#print(DemoNTClass.__slots__)

class DemoSlots:
  __slots__ = {'x', 'y'}

s = DemoSlots()

s.x = 'X'

print(s.x)

#s.a = 'A' da atributte error

