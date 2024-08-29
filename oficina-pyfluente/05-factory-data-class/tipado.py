
def tipada(classe):
  print(classe)
  return classe

@tipada
class Pet:
  nome: str
  peso: float
 

#rex = Pet('Rex', 7.5)

print(Pet.__annotations__)


def inicializar(objeto, *args):
  dicas = objeto.__annotations__
  if len(dicas != len(args)):
    raise TypeError(f'Obrigatório informar {", ".join(dicas.keys())}')
  for nome, arg in zip(dicas, args):
    setattr(objeto, nome, arg)

fido = Pet()

inicializar(fido, 'Fido', 6)

print(fido.__dict__)

def representar(objeto):
  valores = [repr(valor) for valor in objeto.__dict__.values()]
  return f'{type(objeto).__name__}({", ".join(valores)})'

def auto(classe)
  return type(class.__name__, (), {
    '__init__': inicializar,
    '__repr__': representar,
    '__annotations__': classe.__annotations__})

@auto
class Pet:
  nome: str
  peso: float

felix = Pet('Felix', 3, 3)

def inicializar_estrito(objeto, *args):
  dicas = objeto.__annotations__
  if len(dicas) != len(args):
    raise TypeError(f'Required {dicas.keys()}')
  for nome, arg in zip(dicas, args):
    if dicas[nome] is float:
      tipo = (int, float)
      arg = float(arg)
    else:
      tipo = dicas[nome]
    if isinstance(arg, dicas[nome]):
      setattr(objeto, nome, arg)
    else:
      raise TypeError(f'Atributo {nome} deve ser {dicas[nome]}')

#tipada passa a usar inicializar estrito ...

@tipada
class Pet:
  nome: str
  peso: float

#um bom repr eh algo que se voce colar no codigo cria uma instancia igual

lulu = Pet('Lulu', 5)
print(lulu)
