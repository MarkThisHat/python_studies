#!/usr/bin/env python3

"""
>>> main([])
Provide search keywords

>>> main(["cruzeiro"])
U+20A2\t\N{CRUZEIRO SIGN}\tCRUZEIRO SIGN

>>> search(["cat"], 0x1f408, 0x1f640)
U+1F408\t🐈\tCAT
U+1F431\t🐱\tCAT FACE
U+1F638\t😸\tGRINNING CAT FACE WITH SMILING EYES
U+1F639\t😹\tCAT FACE WITH TEARS OF JOY
U+1F63A\t😺\tSMILING CAT FACE WITH OPEN MOUTH
U+1F63B\t😻\tSMILING CAT FACE WITH HEART-SHAPED EYES
U+1F63C\t😼\tCAT FACE WITH WRY SMILE
U+1F63D\t😽\tKISSING CAT FACE WITH CLOSED EYES
U+1F63E\t😾\tPOUTING CAT FACE
U+1F63F\t😿\tCRYING CAT FACE
U+1F640\t🙀\tWEARY CAT FACE


"""
import sys
import unicodedata

def search(query: list[str], first=32, last=sys.maxunicode) -> None:
  query = ' '.join(query).replace('-', ' ').split()
  query = {word.upper() for word in query}
  for code in range(first, last + 1):
    char = chr(code)
    name = unicodedata.name(char, None)
    if name is None:
      continue
    name = set(name.split())
    if query <= name:
      print(f'U+{code:04X}\t{char}\t{unicodedata.name(char)}')

def main(args: list[str]) -> None:
  if not args:
    print("Provide search keywords")
  else:
    search(args)

if __name__ == "__main__":
  import sys
  main(sys.argv[1:])
