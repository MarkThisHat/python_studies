def ajustar(n):
  return n * 1.1

l = [10, 20, 30, 40, 50, 65]
for n in map(ajustar, l):
  print(n) # bug da norma i3e(?)

print("\n")
map(ajustar, l)
list(map(ajustar, l))
print("\n")

def pequeno(n):
  return n < 30

filter(pequeno, l)
list(filter(pequeno, l))

[ajustar(n) for n in l if n < 30]


# lambida

list(filter(lambda n: n < 3, map(lambda n: n * 1.1, l)))

