---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# 1. O modelo de dados do Python

## 1.2. Um baralho pythônico



### 1.2.1. Classe `Card`



`Card` é um `namedtuple` que representa uma carta de baralho.

```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
```

O "sete belo" é conhecido como "beer card" nos EUA:

```python
beer_card = Card('7', 'diamonds')
beer_card
```

```python
beer_card.rank, beer_card.suit
```

```python
beer_card[0], beer_card[1]
```

Uma limitação de `namedtuple` é não permitir a declaração de métodos como em uma classe.

Não é recomendado, mas é possível acrescentar métodos por [monkey-patch](https://en.wikipedia.org/wiki/Monkey_patch): você define uma função e atribui ela à classe, da mesma forma que criamos atributos em instâncias:

```python
def card_to_str(card):
    return '%s of %s' % card

card_to_str(beer_card)
```

Agora podemos atribuir a função à classe com o nome especial `__str__`:

```python
Card.__str__ = card_to_str
print(beer_card)
```

### 1.2.2. Classe `FrenchDeck`

`FrenchDeck` é uma classe que representa um "baralho francês", o tipo mais comum no Brasil, com 52 cartas em 4 naipes de 13 cartas.

```python
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
```

Veja as operações possíveis com um baralho:

```python
deck = FrenchDeck()
len(deck)
```

```python
deck[3]
```

```python
deck[:3]
```

**Nota**: nesse contexto o Python não usa o `__str__` de `Card`. Se você exibir com `print` uma carta de cada vez, daí o `__str__` é usado.

Como `FrenchDeck` implementa `__len__` e `__getitem__`, Python entende que é uma `Sequence` (sequência), então o operador `in` funciona:

```python
Card('Q', 'hearts') in deck
```

#### Exercício

Crie uma carta que não existe, e verifique que o `in` devolve `False`

```python
# sua resposta aqui
```

O laço `for` sabe lidar com sequências:

```python
for card in deck:
    print(card)
```

Muitos métodos da biblioteca padrão lidam com sequências:

```python
from random import choice
choice(deck)
```

Mas a função `shuffle` não funciona. Resolver isso será um exercício logo mais:

```python
from random import shuffle

# This should raise a TypeError
# shuffle(deck)
```

Podemos usar `sorted` para percorrer o baralho em pela ordem de comparação dos elementos das tuplas `Card`:

```python
for card in sorted(deck):
    print(card)
```

Podemos criar uma função que estabelece um critério de ordenação melhor:

```python
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high_ordering(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
```

```python
spades_high_ordering(Card('2', 'clubs'))
```

```python
spades_high_ordering(Card('A', 'spades'))
```

Daí usamos a função como parâmetro `key` em `sorted`. Várias outras funções da biblioteca padrão que envolvem comparação de itens aceitam o parâmetro `key`.

```python
for card in sorted(deck, key=spades_high_ordering):
    print(card)
```

#### Exercício

Defina uma nova ordem que classifique as cartas primeiro por naipe e depois por valor, de forma que todos os paus venham primeiro, seguidos por todos os ouros, etc.

```python
# resposta
```

#### Exercício

Escreva um método chamado `setcard` que pega um baralho, um índice e uma carta e atribui a carta ao baralho na posição dada.

Em seguida, faça um monkey-patch em `FrenchDeck` para fornecer `__setitem__` como método. Teste atribuindo uma nova carta assim:

```meu_baralho[0] = Card('A', 'spades')```

Então tenter embaralhar usando `random.shuffle`.

```python
# resposta
```

#### Exercício bônus

A operação de fatiamento `x[a:b]` normalmente devolve uma instância da mesma classe de `x`.

Será necessário alterar `FrenchDeck` para fazer isso acontecer? Como?

**Dica 1:** O compilador de Python transforma `x[a:b]` em `x.__getitem__(slice(a, b))`.  

**Dica 2:** Será preciso mexer no construtor de `FrenchDeck`, aceitando uma lista opcional de cartas.
