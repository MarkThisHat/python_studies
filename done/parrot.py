def main():
  def parrot(volt, state="stiff", action="voom", type="norblu") -> str:
    print("this parrot wouldn't", action, end=' ')
    print("if you put", volt, "volts through it")
    print("lovely plumage, the", type)
    print("it's", state, end='!\n')
    return "batata" + ' ' + "frita"

  pog = parrot(10, 'dead')

  print("\n", parrot.__annotations__)
  print(pog)

if __name__ == "__main__":
  main()

