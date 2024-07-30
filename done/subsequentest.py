def main():

#  def f(a, L=[]):
#    L.append(a)
#    return L

  def f(a, L=None):
    if L is None:
      L = []
    L.append(a)
    return L

  lista = []

  print(f(1, lista))
  print(f(3))
  print(f('banana', lista))

if __name__ == "__main__":
  main()

