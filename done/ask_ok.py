def ask_ok(prompt, retries=3, reminder ='Plz dolan'):
  while True:
    reply = input(prompt)
    if reply in ('y', 'ye', 'yes'):
      return True
    if reply in ('n', 'no', 'nop', 'nope'):
      return False
    retries = retries - 1
    if retries == 0:
      raise ValueError('invalid in, puto')
    print(reminder)

