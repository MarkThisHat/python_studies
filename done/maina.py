from ask_ok import ask_ok

def main():
  if ask_ok('really?\n', 2, 'spooder plz'):
    print("it's set then")
  else:
    print('no deal then')

if __name__ == "__main__":
  main()
