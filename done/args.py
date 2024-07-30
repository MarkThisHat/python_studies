def main():
  def stdarg(arg):
    print(arg)

  def posonly(arg, /):
    print(arg)

  def kwdarg(*, arg):
    print(arg)

  def combind(positional, /, stdandard, *, keywordarg):
    print(positional, stdandard, keywordarg)

  stdarg(3)
  stdarg(arg="batata")

  posonly(4)
  posonly(' ')
  
  kwdarg(arg="bototo")

  combind(3, stdandard=3, keywordarg=4)
  combind(4, 4, keywordarg=4) 

if __name__ == "__main__":
  main()
