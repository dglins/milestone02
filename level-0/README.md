# Level 0 - Exercícios Básicos

## Visão Geral

O Level 0 representa o nível mais básico do Exam 02, focando em fundamentos essenciais da programação em C. Estes exercícios testam sua compreensão de conceitos fundamentais que são a base para todos os níveis subsequentes.

**Total de exercícios**: 12

**Tempo estimado de estudo**: 4-6 horas

## Conceitos Principais

### 1. **Loops (Laços de Repetição)**
Os loops são estruturas fundamentais que permitem executar código repetidamente. No Level 0, você trabalhará principalmente com:

- **while loop**: Executa enquanto uma condição for verdadeira
  ```c
  while (str[i] != '\0')
      i++;
  ```
- **Iteração sobre strings**: Percorrer caracteres até encontrar o terminador nulo `\0`
- **Contadores**: Usar variáveis para controlar iterações

**Por que é importante**: Loops são essenciais para processar dados sequenciais como strings e arrays.

### 2. **Condicionais (if/else)**
Estruturas de decisão que permitem executar código baseado em condições:

- **if simples**: Executa código se condição for verdadeira
- **if-else**: Escolhe entre duas alternativas
- **if-else if-else**: Múltiplas condições em cascata
- **Operadores lógicos**: `&&` (E), `||` (OU), `!` (NÃO)

**Por que é importante**: Condicionais permitem que programas tomem decisões e respondam a diferentes situações.


### 3. **Manipulação de Strings**
Strings em C são arrays de caracteres terminados por `\0`:

- **Iteração**: Percorrer caracteres um por um
- **Comparação de caracteres**: Verificar se um caractere é letra, dígito, espaço, etc.
- **Modificação**: Transformar caracteres (maiúscula/minúscula)
- **Tabela ASCII**: Entender valores numéricos dos caracteres
  - `'A'` a `'Z'`: 65 a 90
  - `'a'` a `'z'`: 97 a 122
  - Diferença entre maiúscula e minúscula: 32

**Por que é importante**: Manipulação de strings é uma das tarefas mais comuns em programação.

### 4. **Input/Output (I/O)**
Comunicação com o usuário através de entrada e saída:

- **write()**: Função para escrever na saída padrão
  ```c
  write(1, "texto", 5);  // 1 = stdout, 5 = número de bytes
  ```
- **argc/argv**: Argumentos da linha de comando
  - `argc`: número de argumentos
  - `argv`: array de strings com os argumentos
- **Saída formatada**: Imprimir números, caracteres e strings

**Por que é importante**: Todo programa precisa interagir com o usuário ou sistema.

## Dicas de Estudo para Iniciantes

### 🎯 Estratégias de Aprendizado

1. **Comece pelo mais simples**: Resolva os exercícios na ordem apresentada
2. **Entenda antes de memorizar**: Não decore código, entenda a lógica
3. **Pratique sem consultar**: Tente resolver sozinho antes de ver a solução
4. **Escreva à mão**: Praticar no papel ajuda a fixar conceitos
5. **Teste edge cases**: Sempre teste com entradas vazias, nulas, ou extremas


### ⚠️ Armadilhas Comuns

1. **Esquecer o terminador nulo**: Strings em C sempre terminam com `\0`
2. **Off-by-one errors**: Cuidado com índices de arrays (começam em 0)
3. **Não verificar argc**: Sempre valide o número de argumentos
4. **Esquecer o newline**: Muitos exercícios exigem `\n` no final
5. **Usar funções não permitidas**: Leia atentamente quais funções pode usar
6. **Não compilar com flags**: Sempre use `-Wall -Wextra -Werror`

### 📚 Recursos para Estudo Complementar

- **Tabela ASCII**: Memorize os valores de 'A', 'Z', 'a', 'z', '0', '9'
- **Operadores**: Pratique operadores aritméticos e lógicos
- **Debugging**: Aprenda a usar `printf` para debug (remova antes de entregar)
- **Man pages**: Use `man write`, `man 3 printf` para consultar funções

### 🔧 Como Compilar e Testar

**Compilação básica**:
```bash
gcc -Wall -Wextra -Werror nome_do_arquivo.c
./a.out [argumentos]
```

**Exemplo prático**:
```bash
# Compilar
gcc -Wall -Wextra -Werror first_word.c

# Testar com diferentes entradas
./a.out "hello world"           # Saída: hello
./a.out "   hello world"        # Saída: hello
./a.out ""                      # Saída: (newline)
./a.out                         # Saída: (newline)
```

**Dicas de teste**:
- Teste com string vazia: `./a.out ""`
- Teste sem argumentos: `./a.out`
- Teste com espaços: `./a.out "   "`
- Teste com caracteres especiais: `./a.out "hello\tworld"`


## Exercícios do Level 0

### 1. fizzbuzz
**Arquivo**: `fizzbuzz.c`  
**Funções permitidas**: `write`

**Descrição**: Programa que imprime números de 1 a 100, substituindo múltiplos de 3 por "fizz", múltiplos de 5 por "buzz", e múltiplos de ambos por "fizzbuzz".

**Conceitos-chave**:
- Loops (while)
- Operador módulo (%)
- Condicionais em cascata
- Conversão de número para string

**Abordagem**:
1. Iterar de 1 a 100
2. Verificar divisibilidade por 3 E 5 primeiro (ordem importante!)
3. Depois verificar apenas por 3
4. Depois verificar apenas por 5
5. Caso contrário, imprimir o número

**Exemplo de uso**:
```bash
./a.out
# Saída:
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# ...
```

**Complexidade**: O(1) - sempre 100 iterações

**Dicas**:
- A ordem das condições importa! Teste `(i % 3 == 0 && i % 5 == 0)` primeiro
- Use uma função auxiliar para imprimir números
- Não esqueça o newline após cada saída

---

### 2. first_word
**Arquivo**: `first_word.c`  
**Funções permitidas**: `write`

**Descrição**: Programa que imprime a primeira palavra de uma string. Uma palavra é delimitada por espaços/tabs.

**Conceitos-chave**:
- Argumentos de linha de comando (argc/argv)
- Iteração sobre strings
- Identificação de whitespace
- Validação de entrada

**Abordagem**:
1. Verificar se argc == 2
2. Pular espaços e tabs iniciais
3. Imprimir caracteres até encontrar espaço, tab ou fim da string
4. Sempre imprimir newline no final

**Exemplo de uso**:
```bash
./a.out "hello world"
# Saída: hello

./a.out "   hello world"
# Saída: hello

./a.out ""
# Saída: (apenas newline)
```

**Complexidade**: O(n) onde n é o comprimento da string

**Dicas**:
- Whitespace inclui espaço (' ') e tab ('\t')
- Sempre imprima newline, mesmo sem argumentos
- Cuidado com strings vazias

---

### 3. ft_putstr
**Arquivo**: `ft_putstr.c`  
**Funções permitidas**: `write`

**Descrição**: Função que imprime uma string na saída padrão.

**Conceitos-chave**:
- Iteração sobre strings
- Função write
- Ponteiros

**Abordagem**:
1. Iterar pela string até encontrar '\0'
2. Escrever cada caractere usando write

**Exemplo de uso**:
```c
ft_putstr("Hello");  // Imprime: Hello
```

**Complexidade**: O(n) onde n é o comprimento da string

**Dicas**:
- Não adicione newline (a menos que especificado)
- Trate strings vazias corretamente

---

### 4. ft_strcpy
**Arquivo**: `ft_strcpy.c`  
**Funções permitidas**: Nenhuma

**Descrição**: Função que copia uma string para outra, incluindo o terminador nulo.

**Conceitos-chave**:
- Manipulação de ponteiros
- Cópia de strings
- Terminador nulo

**Abordagem**:
1. Iterar pela string origem
2. Copiar cada caractere para o destino
3. Não esquecer de copiar o '\0'
4. Retornar o ponteiro para o destino

**Exemplo de uso**:
```c
char dest[20];
ft_strcpy(dest, "Hello");  // dest agora contém "Hello"
```

**Complexidade**: O(n) onde n é o comprimento da string

**Dicas**:
- Sempre copie o '\0' final
- Retorne o ponteiro original do destino
- Assuma que o destino tem espaço suficiente

---

### 5. ft_strlen
**Arquivo**: `ft_strlen.c`  
**Funções permitidas**: Nenhuma

**Descrição**: Função que retorna o comprimento de uma string (sem contar o '\0').

**Conceitos-chave**:
- Iteração sobre strings
- Contadores
- Terminador nulo

**Abordagem**:
1. Inicializar contador em 0
2. Iterar até encontrar '\0'
3. Incrementar contador a cada caractere
4. Retornar o contador

**Exemplo de uso**:
```c
int len = ft_strlen("Hello");  // Retorna: 5
```

**Complexidade**: O(n) onde n é o comprimento da string

**Dicas**:
- Não conte o '\0'
- String vazia retorna 0

---

### 6. ft_swap
**Arquivo**: `ft_swap.c`  
**Funções permitidas**: Nenhuma

**Descrição**: Função que troca os valores de dois inteiros usando ponteiros.

**Conceitos-chave**:
- Ponteiros
- Passagem por referência
- Variável temporária

**Abordagem**:
1. Usar variável temporária para guardar um valor
2. Fazer a troca dos valores
3. Usar dereferência (*) para acessar valores

**Exemplo de uso**:
```c
int a = 5, b = 10;
ft_swap(&a, &b);  // Agora: a = 10, b = 5
```

**Complexidade**: O(1)

**Dicas**:
- Sempre use variável temporária
- Lembre-se de dereferênciar os ponteiros com *

---

### 7. repeat_alpha
**Arquivo**: `repeat_alpha.c`  
**Funções permitidas**: `write`

**Descrição**: Programa que repete cada letra alfabética de acordo com sua posição no alfabeto (a=1x, b=2x, z=26x).

**Conceitos-chave**:
- Tabela ASCII
- Cálculo de posição no alfabeto
- Loops aninhados
- Argumentos de linha de comando

**Abordagem**:
1. Verificar argc == 2
2. Para cada caractere:
   - Se for letra minúscula: calcular posição com `c - 'a' + 1`
   - Se for letra maiúscula: calcular posição com `c - 'A' + 1`
   - Repetir o caractere N vezes
3. Caracteres não-alfabéticos são impressos uma vez

**Exemplo de uso**:
```bash
./a.out "abc"
# Saída: abbccc

./a.out "Abc"
# Saída: Abbccc
```

**Complexidade**: O(n * m) onde n é o tamanho da string e m é a posição média no alfabeto

**Dicas**:
- 'a' - 'a' = 0, então adicione 1
- Maiúsculas e minúsculas são tratadas separadamente
- Não-letras são impressas normalmente

---

### 8. rev_print
**Arquivo**: `rev_print.c`  
**Funções permitidas**: `write`

**Descrição**: Programa que imprime uma string em ordem reversa.

**Conceitos-chave**:
- Iteração reversa
- Cálculo de comprimento
- Argumentos de linha de comando

**Abordagem**:
1. Verificar argc == 2
2. Encontrar o comprimento da string
3. Iterar de trás para frente
4. Imprimir cada caractere

**Exemplo de uso**:
```bash
./a.out "hello"
# Saída: olleh

./a.out "abc"
# Saída: cba
```

**Complexidade**: O(n) onde n é o comprimento da string

**Dicas**:
- Primeiro encontre o final da string
- Depois itere de trás para frente
- Não esqueça o newline final

---

### 9. rot_13
**Arquivo**: `rot_13.c`  
**Funções permitidas**: `write`

**Descrição**: Programa que aplica a cifra ROT13 (rotaciona cada letra 13 posições no alfabeto).

**Conceitos-chave**:
- Cifra de substituição
- Aritmética modular
- Tabela ASCII
- Preservação de case

**Abordagem**:
1. Para cada caractere:
   - Se for letra minúscula: rotacionar dentro de 'a'-'z'
   - Se for letra maiúscula: rotacionar dentro de 'A'-'Z'
   - Outros caracteres permanecem inalterados
2. Usar aritmética: `(c - 'a' + 13) % 26 + 'a'`

**Exemplo de uso**:
```bash
./a.out "hello"
# Saída: uryyb

./a.out "uryyb"
# Saída: hello (ROT13 é reversível!)
```

**Complexidade**: O(n) onde n é o comprimento da string

**Dicas**:
- ROT13 é sua própria inversa (aplicar duas vezes retorna ao original)
- Use módulo 26 para "dar a volta" no alfabeto
- Mantenha maiúsculas como maiúsculas e minúsculas como minúsculas

---

### 10. rotone
**Arquivo**: `rotone.c`  
**Funções permitidas**: `write`

**Descrição**: Programa que rotaciona cada letra 1 posição no alfabeto (a→b, z→a).

**Conceitos-chave**:
- Rotação de caracteres
- Casos especiais (z→a, Z→A)
- Tabela ASCII

**Abordagem**:
1. Para cada caractere:
   - Se for 'z', vira 'a'
   - Se for 'Z', vira 'A'
   - Se for outra letra minúscula, adiciona 1
   - Se for outra letra maiúscula, adiciona 1
   - Outros caracteres permanecem inalterados

**Exemplo de uso**:
```bash
./a.out "abc"
# Saída: bcd

./a.out "xyz"
# Saída: yza
```

**Complexidade**: O(n) onde n é o comprimento da string

**Dicas**:
- Trate 'z' e 'Z' como casos especiais
- Não use módulo, use if simples
- Mais simples que ROT13

---

### 11. search_and_replace
**Arquivo**: `search_and_replace.c`  
**Funções permitidas**: `write`

**Descrição**: Programa que substitui todas as ocorrências de um caractere por outro em uma string.

**Conceitos-chave**:
- Substituição de caracteres
- Validação de argumentos
- Verificação de comprimento de string

**Abordagem**:
1. Verificar se argc == 4
2. Verificar se argv[2] e argv[3] têm exatamente 1 caractere
3. Iterar pela string
4. Substituir caractere quando encontrado

**Exemplo de uso**:
```bash
./a.out "hello world" "o" "a"
# Saída: hella warld

./a.out "hello" "l" "r"
# Saída: herro
```

**Complexidade**: O(n) onde n é o comprimento da string

**Dicas**:
- Valide que os argumentos 2 e 3 têm apenas 1 caractere
- Se validação falhar, imprima apenas newline
- Substitua TODAS as ocorrências

---

### 12. ulstr
**Arquivo**: `ulstr.c`  
**Funções permitidas**: `write`

**Descrição**: Programa que inverte maiúsculas/minúsculas de uma string (maiúsculas viram minúsculas e vice-versa).

**Conceitos-chave**:
- Conversão de case
- Tabela ASCII
- Diferença entre maiúsculas e minúsculas (32)

**Abordagem**:
1. Para cada caractere:
   - Se for minúscula ('a'-'z'): subtrair 32
   - Se for maiúscula ('A'-'Z'): adicionar 32
   - Outros caracteres permanecem inalterados

**Exemplo de uso**:
```bash
./a.out "Hello World"
# Saída: hELLO wORLD

./a.out "aBc123"
# Saída: AbC123
```

**Complexidade**: O(n) onde n é o comprimento da string

**Dicas**:
- A diferença entre 'A' e 'a' é exatamente 32 na tabela ASCII
- Não afete números ou caracteres especiais
- Simples e direto

---

## Resumo de Preparação

### Checklist de Conceitos para Dominar

- [ ] Escrever loops while corretamente
- [ ] Usar condicionais if/else/else if
- [ ] Iterar sobre strings até '\0'
- [ ] Usar argc e argv corretamente
- [ ] Escrever com write() corretamente
- [ ] Entender tabela ASCII básica
- [ ] Converter entre maiúsculas e minúsculas
- [ ] Calcular posição no alfabeto
- [ ] Validar entrada de argumentos
- [ ] Compilar com flags -Wall -Wextra -Werror

### Ordem Sugerida de Estudo

1. **Primeiro**: ft_strlen, ft_putstr (mais simples)
2. **Segundo**: first_word, ulstr (manipulação básica)
3. **Terceiro**: repeat_alpha, rotone, rot_13 (transformações)
4. **Quarto**: search_and_replace, rev_print (mais complexos)
5. **Quinto**: fizzbuzz (lógica condicional)
6. **Por último**: ft_strcpy, ft_swap (ponteiros)

### Tempo de Prática Recomendado

- **Primeira vez**: 30-45 minutos por exercício
- **Revisão**: 10-15 minutos por exercício
- **No exame**: 5-10 minutos por exercício

Boa sorte nos seus estudos! 🚀
