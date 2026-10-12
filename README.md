# Conceitos de coleções para a avaliação (lista 3)

Todos os exemplos foram testados no Python 3.13. Sempre que possível, uso o seu próprio código da lista 3.

---

## 0. O mapa da lista

| Ex | Estrutura | Em uma frase | Sintaxe |
|----|-----------|--------------|---------|
| 0, 1 | **list** | sequência ordenada, por posição, que pode mudar | `[1, 2, 3]` |
| 2 | **tuple** | sequência ordenada que **não** muda | `(1, 2, 3)` |
| 3 | **set** | saco de itens **únicos**, sem ordem | `{1, 2, 3}` |
| 4 | **dict** | pares **chave → valor** | `{'sword': 1}` |
| 5 | **gerador** | produz valores **um de cada vez**, sob demanda | `yield` |
| 6 | **comprehension** | jeito curto de **montar** lista/dict/set a partir de outra coleção | `[x for x in ...]` |

A pergunta que o PDF quer que você saiba responder em cada exercício: **por que essa estrutura e não outra?** O prefácio (Twitter) resume: *"your data structure is your algorithm"*. Escolher a estrutura errada não dá erro, só deixa tudo lento.

---

## 1. Variáveis são etiquetas (vale para todas as coleções)

Em Python, uma variável não é uma "caixa" com o valor dentro. É uma **etiqueta** colada num objeto.

```python
a = [1, 2, 3]
b = a            # NÃO copia: b é outra etiqueta no MESMO objeto
b.append(4)
print(a)         # [1, 2, 3, 4]

c = a[:]         # isso sim copia
c.append(5)
print(a, c)      # [1, 2, 3, 4] [1, 2, 3, 4, 5]
```

**Comparação com C:** passar uma lista para uma função em Python é como passar um **ponteiro** para um array em C. A função mexe no array original.

**No seu código (ex5):** `consume_event(events)` faz `events.pop(i)`. Como a lista é a mesma (não uma cópia), o `print(f"Remains in list: {events}")` na `main` mostra a lista diminuindo. Se você passasse uma cópia (`consume_event(events[:])`), o "Remains" ficaria sempre com 10.

### Mutável x imutável

| Mutável (pode mudar depois de criado) | Imutável (não pode) |
|----|----|
| `list`, `dict`, `set` | `tuple`, `str`, `int`, `float` |

Isso decide quem pode ser **chave de dict** e **item de set** (seção 4).

---

## 2. Listas (ex0 e ex1)

```python
args = ['prog', 'a', 'b']
args[0]       # 'prog'   (índice começa em 0, igual a C)
args[-1]      # 'b'      (negativo conta do fim)
args[1:]      # ['a', 'b']  fatiamento: do índice 1 até o fim, cria lista NOVA
args[1:99]    # ['a', 'b']  fatiar além do fim não dá erro
len(args)     # 3
```

Métodos que você usou:
- `lst.append(x)`: põe no fim.
- `lst.pop()`: tira do fim e devolve. `lst.pop(i)`: tira da posição `i` (ex5).

**`sys.argv` (ex0):** é uma `list[str]`. Igual ao `char **argv` de C: `argv[0]` é o nome do programa, o resto são os argumentos, **sempre como texto**. Diferença: não precisa de `argc`, porque `len(sys.argv)` dá o tamanho.

### Três jeitos de pular o nome do programa (o PDF pede para discutir)

```python
for i in range(1, len(args)):          # 1. índice, estilo C (o seu ex0)
    print(f"Argument {i}: {args[i]}")

for arg in args[1:]:                    # 2. fatiamento, estilo Python
    print(arg)

for i, arg in enumerate(args[1:], 1):  # 3. enumerate dá índice + valor
    print(f"Argument {i}: {arg}")
```

`range` e `enumerate` não estão nas autorizadas do ex0. O fatiamento é **sintaxe** da lista, não função, então pode. Com um contador manual (`i += 1`) você imprime o número sem `range`.

**Em Python, prefira `for item in lista`** ao `for i in range(len(lista))`. Você raramente precisa do índice; quando precisa, use `enumerate`.

**Listas podem misturar tipos** (`[1, 'a', 2.5]`), mas o normal é guardar um tipo só. Por isso o type hint é `list[int]`.

**Pergunta provável (ex1):** "Por que criar uma lista nova de scores?" Porque `sys.argv` tem texto, e você quer números para fazer `sum`, `max`, `min`. A lista nova guarda os `int` já convertidos e sem os inválidos.

---

## 3. Tuplas (ex2)

Tupla é uma lista que **não pode mudar** depois de criada. O PDF: *"Tuples are like data written in stone."*

```python
p = (1.0, 2.5, 3.0)
p[0]          # 1.0   (acesso por índice, igual à lista)
p[0] = 9      # TypeError: 'tuple' object does not support item assignment
```

### Desempacotamento (unpacking)

```python
p = (1.0, 2.5, 3.0)
x, y, z = p        # x=1.0, y=2.5, z=3.0
```

É um atalho: o Python distribui os itens da tupla, **em ordem**, entre as variáveis da esquerda. A linha acima faz o mesmo que:

```python
x = p[0]
y = p[1]
z = p[2]
```

A regra é: **a quantidade de variáveis tem que ser igual à quantidade de itens.**

```python
x, y = p           # ValueError: too many values to unpack (expected 2)
a, b, c, d = p     # ValueError: not enough values to unpack (expected 4, got 3)
x, _, z = p        # ok: o _ é a convenção para "esse eu não quero"
```

Analogia: 3 bolas e 2 mãos. Sobra uma bola e o Python não decide sozinho onde colocar, então dá erro.

Você usa isso duas vezes no ex2: `x, y, z = float_num` para montar a tupla e `x1, y1, z1 = p1` na `get_distance`. Também é o que acontece no ex5 com `player, action = next(generator)`.

### Pegadinha: tupla de 1 elemento

```python
type((1))     # <class 'int'>    só parênteses de matemática
type((1,))    # <class 'tuple'>  quem faz a tupla é a VÍRGULA
```

### Por que tupla e não lista para coordenadas?

1. **Significado:** uma posição tem sempre 3 valores que andam juntos. Ninguém deve dar `append` numa coordenada.
2. **Segurança:** se alguém tentar mudar o `y` sem querer, dá erro em vez de bug silencioso.
3. **Pode ser chave de dict e item de set** (seção 4): `{(1, 2): "baú"}` funciona; `{[1, 2]: "baú"}` não.

**Comparação com C:** é parecido com uma `struct` com 3 campos `const`.

### Coisas do ex2 que valem explicar

- `"1.0 , 2.5, 3.0".split(",")` dá `['1.0 ', ' 2.5', ' 3.0']`. Os espaços sobram, mas `float(" 2.5 ")` aceita espaços nas pontas. Por isso o exemplo do PDF com espaços funciona.
- `"hello world".split(",")` dá uma lista com **1** item, por isso cai no `Invalid syntax`.
- `float("inf")` e `float("nan")` são válidos em Python. Por isso você usou o `math.isfinite`.
- `round(4.031128, 4)` dá `4.0311`.

---

## 4. Sets (ex3)

Set é uma coleção de itens **únicos** e **sem ordem**.

```python
{1, 1, 2, 2}      # {1, 2}   repetidos somem
set()             # set vazio
{}                # NÃO é set vazio: é dict vazio
```

**Pergunta do PDF: "how does Python print an empty set, and why?"** Imprime `set()`, porque a notação `{}` já foi reservada para o **dicionário** vazio (o dict veio antes na linguagem). Então o Python escreve o nome do construtor.

### As operações (todas devolvem um set NOVO)

```python
s1 = {1, 2, 3}; s2 = {2, 3, 4}; s3 = {3, 4, 5}

s1.union(s2, s3)          # {1, 2, 3, 4, 5}  está em PELO MENOS UM
s1.intersection(s2, s3)   # {3}              está em TODOS
s1.difference(s2, s3)     # {1}              está em s1 e em NENHUM dos outros
```

| No ex3 | Operação | Pensa como |
|----|----|----|
| All distinct achievements | `alice.union(bob, charlie, dylan)` | "OU" |
| Common achievements | `alice.intersection(bob, charlie, dylan)` | "E" |
| Only Alice has | `alice.difference(bob, charlie, dylan)` | "Alice MENOS os outros" |
| Alice is missing | `todas.difference(alice)` | "tudo MENOS o que ela tem" |

Analogia: diagrama de Venn das aulas de matemática. União é tudo pintado, interseção é só o meio, diferença é a parte de um círculo que não encosta nos outros.

Também existem operadores: `s1 | s2` (união), `s1 & s2` (interseção), `s1 - s2` (diferença). Diferença: o **método** aceita qualquer coleção (`s1.union([9, 9])` funciona), o **operador** só aceita set (`s1 | [9]` dá `TypeError`).

Outros métodos: `s.add(x)`, `s.discard(x)` (remove se existir, sem erro), `x in s`.

### Por que a ordem muda a cada execução?

O set guarda os itens numa **tabela hash**: cada item vira um número (o hash), e esse número decide a "gaveta" onde ele fica. Para strings, o Python muda a fórmula do hash a cada execução (por segurança), então a ordem impressa muda. Por isso o PDF não pede ordem nenhuma. **Nunca conte com a ordem de um set.**

### Hash: por que só imutáveis entram em set (e como chave de dict)

```python
{(1, 2)}      # ok, tupla é imutável
{[1, 2]}      # TypeError: unhashable type: 'list'
```

Se uma lista mudasse depois de entrar no set, o hash dela mudaria e ela ficaria na "gaveta errada", impossível de achar. Então o Python só aceita objetos que não mudam.

### Por que set é rápido (o prefácio do Twitter)

`x in lista` olha item por item (O(n)). `x in set` calcula o hash e vai direto na gaveta (O(1) em média). Testei com 100 000 números, procurando o último, 1000 vezes:

```
lista: 0.58 s
set:   0.00004 s
```

Analogia: procurar um nome numa pilha de papéis (lista) x numa agenda com abas por letra (set).

### `random` no ex3

- `random.randint(a, b)`: inteiro de `a` até `b`, **incluindo** `b`.
- `random.sample(seq, k)`: escolhe `k` itens **diferentes**. Exige uma sequência (lista, tupla); com set dá `TypeError: Population must be a sequence`.
- `random.choice(seq)`: um item (ex5).

---

## 5. Dicionários (ex4)

Dicionário guarda pares **chave → valor**. Você acessa pela chave, não pela posição.

```python
inv = {'sword': 1, 'potion': 5}
inv['potion']        # 5
inv['sword'] = 2     # muda o valor
inv['key'] = 1       # chave nova: cria
'sword' in inv       # True   (o "in" procura nas CHAVES)
1 in inv             # False  (1 é valor, não chave)
inv['x']             # KeyError: 'x'
inv.get('x')         # None, sem erro
inv.get('x', 0)      # 0     (valor padrão)
```

Analogia: dicionário de verdade. Você procura a **palavra** (chave) e lê a **definição** (valor). Ninguém procura "a 3ª palavra do dicionário".

### Métodos do ex4

```python
list(inv.keys())      # ['sword', 'potion', 'key']
list(inv.values())    # [2, 5, 1]
list(inv.items())     # [('sword', 2), ('potion', 5), ('key', 1)]  pares em tuplas
inv.update({'potion': 9, 'magic_item': 1})   # muda as que existem, cria as novas
```

- `for item in inv:` percorre as **chaves** (o que você faz no ex4).
- `for k, v in inv.items():` percorre os pares (o que você faz no ex6). Repare no desempacotamento de tupla.

### Ordem

Desde o Python 3.7, o dict **lembra a ordem de inserção**. É por isso que:
- o `Got inventory` sai na ordem da linha de comando;
- o seu empate funciona: o primeiro item com quantidade máxima é o primeiro a aparecer, e `>` estrito não troca por um igual depois.

Set não tem essa garantia; dict tem.

### Regras das chaves

- Chaves são **únicas**. Por isso o `sword:2` é redundante: o dict só pode ter um `'sword'`. Você testa `if key in inventory` antes, para imprimir o aviso; sem isso o segundo valor **sobrescreveria** o primeiro em silêncio.
- Chaves precisam ser **imutáveis** (hashable), igual aos itens de set. Por baixo, o dict é a mesma tabela hash, com um valor pendurado em cada gaveta.

### Por que dict no inventário

`'sword' in inventory` e `inventory['sword']` são instantâneos, não importa o tamanho. Com uma lista de pares `[('sword', 1), ...]`, você teria que percorrer tudo para achar a espada.

**Comparação com C:** não existe em C puro. Seria um array de `struct { char *nome; int qtd; }` com busca linear, ou uma hash table que você mesma escreveria.

---

## 6. Geradores (ex5)

Uma função com `yield` vira um **gerador**. Ela não roda quando é chamada: só cria um objeto que vai produzindo valores **quando alguém pede**.

```python
def g():
    print("start")
    yield 1
    print("mid")
    yield 2
    print("end")

it = g()          # nada é impresso ainda
next(it)          # imprime "start", devolve 1, PAUSA
next(it)          # imprime "mid",   devolve 2, PAUSA
next(it)          # imprime "end",   e acaba: StopIteration
```

- `return` encerra a função de vez. `yield` **entrega um valor e pausa**, guardando onde parou e o valor das variáveis.
- `next(gen)` pede o próximo valor.
- Quando a função chega ao fim, `next` lança `StopIteration`.
- O `for` chama `next` sozinho e para quando vem o `StopIteration`. Por isso `for event in consume_event(events):` termina quando a lista esvazia.

Analogia: a lista é a padaria que assa 1000 pães de manhã e ocupa a prateleira toda. O gerador é o padeiro que assa um pão cada vez que alguém pede.

### Gerador infinito (`gen_event`)

```python
def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    ...
    while True:
        yield (random.choice(players), random.choice(actions))
```

`while True` aqui **não trava** o programa, porque a função pausa a cada `yield`. Só roda de novo quando a `main` pede com `next()`. Por isso dá para pedir 1000, depois mais 10, do mesmo gerador.

Cuidado: `for e in gen_event():` sem `break` nunca termina, e `list(gen_event())` trava tentando guardar infinitos itens.

### Memória

Testado com 1 milhão de números:

```python
sys.getsizeof([i for i in range(1000000)])   # 8 448 728 bytes (lista)
sys.getsizeof((i for i in range(1000000)))   # 192 bytes (gerador)
```

O gerador ocupa o mesmo tanto com 10 ou 10 bilhões de itens, porque só guarda "onde estou".

### Gerador se esgota

```python
gen = (i * i for i in range(3))
list(gen)     # [0, 1, 4]
list(gen)     # []   já foi consumido
```

Uma lista você percorre quantas vezes quiser; um gerador, uma vez só.

### O type hint

`typing.Generator[tuple[str, str], None, None]` lê-se assim:
1. **o que ele entrega** (`yield`): `tuple[str, str]`;
2. o que ele recebe por `send()`: `None` (não usamos);
3. o que ele devolve no `return` final: `None`.

**Pergunta provável:** "Para que serve na vida real?" Ler um arquivo enorme linha por linha, processar eventos que chegam sem fim (o exemplo do jogo), qualquer coisa grande demais para caber na memória.

---

## 7. Comprehensions (ex6)

É um jeito curto de **criar** uma coleção a partir de outra. As duas formas abaixo dão o mesmo resultado:

```python
capitalized = []
for name in players:
    capitalized.append(name.capitalize())

capitalized = [name.capitalize() for name in players]
```

Leia assim: "**`name.capitalize()`** para cada `name` em `players`".

### Com filtro (`if` no fim)

```python
only_capitalized = [name for name in players if name.capitalize() == name]
pares = [x for x in range(10) if x % 2 == 0]      # [0, 2, 4, 6, 8]
```

O `if` no fim **escolhe quais entram**. Diferente do `if/else` **no começo**, que escolhe **o valor** de cada um (todos entram):

```python
[x if x > 0 else 0 for x in [-1, 2]]              # [0, 2]
```

### Os quatro tipos

```python
[n * 2 for n in nums]                 # lista
{name: random.randint(0, 999) for name in capitalized}   # dict (chave: valor)
{n % 3 for n in range(10)}            # set: {0, 1, 2}
(n * 2 for n in nums)                 # NÃO é "tuple comprehension": é um GERADOR
```

O PDF lembra que dá para usar em sets. E o último liga com o ex5: parênteses criam um **gerador**, que você pode passar direto para `sum`: `sum(x * x for x in range(4))` dá `14` sem criar lista.

### O seu ex6 linha por linha

- `score_dict = {name: random.randint(0, 999) for name in capitalized}`: cada nome vira chave, com um número aleatório de valor.
- `average = sum(score_dict.values()) / len(score_dict)`: `/` sempre dá `float`.
- `high_scores = {name: score for name, score in score_dict.items() if score > average}`: percorre os pares e mantém só os acima da média.

### Quando **não** usar

Se precisa de várias linhas de lógica, `print` no meio, ou `try/except`, use um `for` normal. Comprehension é para transformar/filtrar de forma simples. O PDF pede "each comprehension on a single line": se não cabe numa linha, provavelmente deveria ser um `for`.

---

## 8. Detalhes que aparecem nos exercícios

**`round` arredonda o empate para o par** (banker's rounding):
```python
round(2.5)          # 2
round(3.5)          # 4
round(410.1, 2)     # 410.1     (não mostra o zero)
f"{410.1:.2f}"      # '410.10'  (sempre 2 casas, é o que você usa no ex6)
```

**`int()` e `float()` com texto:**
```python
int(" 42 ")    # 42   aceita espaços nas pontas
int("+7")      # 7
int("4.5")     # ValueError: invalid literal for int() with base 10: '4.5'
float("1e3")   # 1000.0
```

**`split`:** `"a,b,,c".split(",")` dá `['a', 'b', '', 'c']`. Um campo vazio vira `''`, e `float('')` dá `ValueError`, então o ex2 trata `1,,3` sem quebrar.

---

## 9. Tabela de escolha (para responder "por que essa estrutura?")

| Preciso de... | Use |
|----|----|
| ordem + mudar o conteúdo | `list` |
| ordem + valores fixos, ou usar como chave | `tuple` |
| não repetir / testar "já tem?" rápido / Venn | `set` |
| buscar pelo nome | `dict` |
| muitos (ou infinitos) itens, um de cada vez | gerador |
| montar uma coleção a partir de outra | comprehension |

| | list | tuple | set | dict |
|----|----|----|----|----|
| Ordem garantida | sim | sim | **não** | sim (inserção) |
| Repetidos | sim | sim | **não** | chaves não |
| Muda depois de criado | sim | **não** | sim | sim |
| Acesso | `l[i]` | `t[i]` | só `in` | `d[chave]` |
| `x in ...` | lento (O(n)) | lento | **rápido** | **rápido** (chaves) |
| Pode ser chave de dict | não | sim | não | não |

---

## 10. Pedidos ao vivo comuns

O PDF avisa: *"you may be asked to ... extend your analytics systems with new functionality."*

1. **ex0:** trocar o `range` por fatiamento ou `enumerate`.
2. **ex1:** aceitar `float` além de `int`; ou mostrar a mediana (`sorted(scores)` e pegar o meio).
3. **ex2:** guardar várias posições numa lista de tuplas e somar a distância total percorrida; mostrar que `p1[0] = 5` dá erro.
4. **ex3:** adicionar um 5º jogador; usar os operadores `|`, `&`, `-` em vez dos métodos; achar quem tem mais conquistas.
5. **ex4:** remover um item (`del inv['sword']` ou `inv.pop('sword')`); listar só os itens com quantidade > 2 (comprehension); usar `get` para somar ao que já existe em vez de descartar o redundante.
6. **ex5:** contar quantas vezes cada jogador apareceu nos 1000 eventos (dict de contagem); fazer um gerador finito que para depois de N eventos.
7. **ex6:** fazer um set comprehension com as iniciais; inverter o dict (`{v: k for k, v in d.items()}`).

## Perguntas rápidas para treinar em voz alta

1. Qual a diferença entre `b = a` e `b = a[:]` numa lista?
2. O que é `sys.argv`? Em que ele parece com o `argv` de C?
3. Três jeitos de não imprimir o nome do programa no ex0?
4. O que é fatiamento? `argv[1:]` cria uma lista nova?
5. Diferença entre lista e tupla? Por que tupla para coordenadas?
6. Como se cria uma tupla de 1 elemento?
7. O que é desempacotamento? Onde você usa?
8. Como o Python imprime um set vazio, e por quê?
9. O que fazem `union`, `intersection` e `difference`? Qual dá "só a Alice tem"?
10. Por que a ordem do set muda a cada execução?
11. Por que lista não pode ser item de set nem chave de dict?
12. Por que `x in set` é mais rápido que `x in lista`?
13. Como `in` funciona num dict: procura chave ou valor?
14. O dict mantém ordem? Como isso ajuda no empate do ex4?
15. O que acontece se colocar a mesma chave duas vezes num dict?
16. Diferença entre `d['x']` e `d.get('x')`?
17. O que `yield` faz de diferente de `return`?
18. Por que o `while True` do `gen_event` não trava o programa?
19. Por que o `for` com `consume_event` para sozinho?
20. Por que o "Remains in list" diminui, se o `pop` está dentro do gerador?
21. Vantagem do gerador sobre a lista? E a desvantagem?
22. O que significam os 3 tipos em `Generator[tuple[str, str], None, None]`?
23. Reescreva uma comprehension do ex6 como `for` normal.
24. Diferença entre `if` no fim e `if/else` no começo de uma comprehension?
25. `(x for x in ...)` cria uma tupla?
