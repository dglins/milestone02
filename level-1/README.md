# Nível 1 - Intermediário

## Visão Geral

O Nível 1 representa um salto significativo em complexidade em relação ao Nível 0. Aqui você encontrará exercícios que exigem compreensão mais profunda de conceitos fundamentais de C, incluindo manipulação de ponteiros, alocação dinâmica de memória, operações bit a bit, e algoritmos mais elaborados.

Este nível é crucial para desenvolver as habilidades necessárias para os níveis mais avançados. Os exercícios aqui testam não apenas sua capacidade de escrever código funcional, mas também sua compreensão de como a memória funciona e como manipular dados em nível mais baixo.

## Conceitos Principais

### 1. **Ponteiros e Aritmética de Ponteiros**

Ponteiros são variáveis que armazenam endereços de memória. Dominar ponteiros é essencial em C.

```c
char *str = "Hello";  // str aponta para o primeiro caractere
str++;                // agora aponta para 'e'
*str                  // acessa o valor apontado ('e')
```

**Por que é importante**: Ponteiros permitem manipulação eficiente de strings, arrays e estruturas de dados. São fundamentais para passar dados por referência e trabalhar com memória dinâmica.

### 2. **Alocação Dinâmica de Memória (malloc)**

A função `malloc()` aloca memória no heap durante a execução do programa.

```c
char *str = (char *)malloc(sizeof(char) * 10);
if (!str)
    return (NULL);  // Sempre verificar se malloc falhou!
// ... usar a memória ...
free(str);  // Liberar quando não precisar mais
```

**Por que é importante**: Permite criar estruturas de dados de tamanho variável e gerenciar memória de forma flexível. É essencial para programas que precisam adaptar-se a diferentes volumes de dados.

**⚠️ Armadilhas Comuns**:
- Esquecer de verificar se `malloc()` retornou NULL
- Esquecer de adicionar +1 para o terminador nulo em strings
- Não liberar memória (memory leak) - embora no exame isso não seja sempre testado
- Acessar memória após `free()` (dangling pointer)

### 3. **Manipulação de Bits**

Operações bit a bit trabalham diretamente com os bits individuais de um número.

```c
unsigned char n = 5;  // 00000101 em binário

// Operadores bit a bit:
n & 1     // AND: testa se bit menos significativo é 1
n >> 1    // Shift direita: desloca bits para direita (divide por 2)
n << 1    // Shift esquerda: desloca bits para esquerda (multiplica por 2)
n | 1     // OR: define bit menos significativo como 1
n ^ 1     // XOR: inverte bit menos significativo
~n        // NOT: inverte todos os bits
```

**Por que é importante**: Operações bit a bit são extremamente eficientes e são usadas em otimizações, criptografia, compressão e manipulação de hardware.

### 4. **Conversão de Strings para Números (atoi)**

Converter representações textuais de números em valores numéricos é uma habilidade fundamental.

```c
"123" -> 123
"-456" -> -456
"  +789" -> 789
```

**Algoritmo básico**:
1. Pular espaços em branco
2. Verificar sinal (+ ou -)
3. Para cada dígito: `result = result * 10 + (digit - '0')`

### 5. **Algoritmos de Conjunto (Interseção e União)**

Operações de conjunto sobre strings tratam caracteres como elementos de conjuntos.

- **Interseção**: caracteres que aparecem em ambas as strings
- **União**: todos os caracteres únicos de ambas as strings

**Técnica comum**: Usar array de 256 posições para marcar caracteres já vistos (ASCII table).

### 6. **Comparação e Busca em Strings**

Algoritmos para comparar strings, encontrar substrings, ou verificar presença de caracteres.

```c
// strcmp: compara caractere por caractere
while (*s1 && *s1 == *s2)
{
    s1++;
    s2++;
}
return (*s1 - *s2);
```

## Dicas de Estudo

### 📚 Estratégias de Resolução

1. **Leia o subject com atenção**: Identifique exatamente o que é pedido, quais funções são permitidas, e quais arquivos devem ser entregues.

2. **Desenhe exemplos**: Antes de codificar, escreva exemplos de entrada e saída esperada. Isso clarifica o problema.

3. **Pense em edge cases**: 
   - String vazia
   - NULL pointers
   - Números negativos
   - Overflow
   - Caracteres especiais

4. **Teste incrementalmente**: Não escreva todo o código de uma vez. Teste cada parte conforme avança.

5. **Use papel**: Para exercícios de bits, desenhe os bits no papel. Para ponteiros, desenhe diagramas de memória.

### ⚠️ Erros Frequentes

1. **Off-by-one errors**: Esquecer de alocar espaço para '\0', ou iterar um índice a mais/menos.

2. **Não verificar malloc**: Sempre verifique se `malloc()` retornou NULL antes de usar o ponteiro.

3. **Confundir & e &&**: `&` é operador bit a bit, `&&` é operador lógico.

4. **Esquecer o '\0'**: Strings em C sempre terminam com '\0'. Ao criar strings, sempre adicione.

5. **Modificar string literal**: `char *str = "Hello"` cria uma string read-only. Use `char str[] = "Hello"` se precisar modificar.

### 🎯 Dicas de Gerenciamento de Memória

1. **Sempre calcule o tamanho correto**:
   ```c
   // Para string: tamanho + 1 (para '\0')
   char *str = malloc(sizeof(char) * (len + 1));
   ```

2. **Verifique retorno de malloc**:
   ```c
   if (!ptr)
       return (NULL);
   ```

3. **Inicialize memória quando necessário**:
   ```c
   int array[256] = {0};  // Inicializa tudo com 0
   ```

4. **No exame, free() geralmente não é necessário**: O programa termina logo após, então o OS limpa a memória. Mas é boa prática incluir.

## Exercícios do Nível 1

### Conversão e Comparação
- **ft_atoi**: Converte string para inteiro
- **ft_strcmp**: Compara duas strings lexicograficamente
- **ft_strcspn**: Encontra primeiro caractere de s1 que está em s2
- **do_op**: Calculadora simples com operações básicas

### Alocação de Memória
- **ft_strdup**: Duplica uma string com malloc

### Manipulação de Bits
- **print_bits**: Imprime byte em formato binário
- **swap_bits**: Troca nibbles de um byte
- **is_power_of_2**: Verifica se número é potência de 2

### Transformação de Strings
- **alpha_mirror**: Espelha letras do alfabeto (a↔z, b↔y, etc.)
- **camel_to_snake**: Converte camelCase para snake_case
- **snake_to_camel**: Converte snake_case para camelCase

### Operações de Conjunto
- **inter**: Interseção de duas strings (caracteres comuns)
- **union**: União de duas strings (todos caracteres únicos)

### Auxiliares
- **last_word**: Extrai última palavra de uma string
- **max**: Encontra maior valor em array de inteiros

---

## Explicações Detalhadas por Exercício


### 📝 alpha_mirror

**Arquivos esperados**: `alpha_mirror.c`  
**Funções permitidas**: `write`

#### Descrição
Escreva um programa que recebe uma string e exibe a string com cada letra do alfabeto substituída pela letra oposta (a↔z, b↔y, c↔x, etc.). Letras maiúsculas e minúsculas são tratadas separadamente. Caracteres não-alfabéticos permanecem inalterados.

#### Conceitos-chave
- Manipulação de caracteres ASCII
- Operações aritméticas com caracteres
- Preservação de case (maiúscula/minúscula)

#### Abordagem
Para espelhar uma letra:
- Para minúsculas: `'a' + 'z' - letra`
- Para maiúsculas: `'A' + 'Z' - letra`

Exemplo: 'a' (primeira letra) → 'z' (última letra)
- `'a' + 'z' - 'a'` = `97 + 122 - 97` = `122` = 'z' ✓

#### Como testar
```bash
gcc -Wall -Wextra -Werror alpha_mirror.c
./a.out "abc"           # Esperado: zyx
./a.out "My horse is Amazing." # Esperado: Nb slihv rh Znzarmt.
./a.out                 # Esperado: (newline)
```

#### Edge Cases
- String vazia
- Apenas caracteres não-alfabéticos
- Mix de maiúsculas, minúsculas e símbolos

---

### 📝 camel_to_snake

**Arquivos esperados**: `camel_to_snake.c`  
**Funções permitidas**: `malloc`, `free`, `write`

#### Descrição
Converte uma string em camelCase para snake_case. Letras maiúsculas são convertidas para minúsculas precedidas por underscore.

#### Conceitos-chave
- Detecção de letras maiúsculas
- Conversão de case
- Escrita caractere por caractere

#### Abordagem
1. Percorrer a string
2. Se encontrar maiúscula:
   - Escrever '_'
   - Escrever a letra em minúscula (letra + 32)
3. Caso contrário, escrever o caractere normalmente

#### Como testar
```bash
gcc -Wall -Wextra -Werror camel_to_snake.c
./a.out "hereIsACamelCaseWord" # Esperado: here_is_a_camel_case_word
./a.out "helloWorld"            # Esperado: hello_world
./a.out "camelCase"             # Esperado: camel_case
```

---

### 📝 do_op

**Arquivos esperados**: `do_op.c`  
**Funções permitidas**: `atoi`, `printf`, `write`

#### Descrição
Programa que realiza operações aritméticas simples (+, -, *, /, %) entre dois números.

#### Conceitos-chave
- Parsing de argumentos
- Conversão string para int (atoi)
- Operadores aritméticos
- Formatação de output

#### Abordagem
1. Verificar se há exatamente 3 argumentos
2. Converter primeiro e terceiro argumento para int
3. Verificar qual operação (segundo argumento)
4. Realizar operação e imprimir resultado

#### Como testar
```bash
gcc -Wall -Wextra -Werror do_op.c
./a.out "123" "*" "456"  # Esperado: 56088
./a.out "9828" "/" "234" # Esperado: 42
./a.out "1" "+" "-43"    # Esperado: -42
./a.out                  # Esperado: (newline)
```

#### Edge Cases
- Divisão por zero (comportamento indefinido, mas geralmente não testado)
- Números negativos
- Operador inválido

---

### 📝 ft_atoi

**Arquivos esperados**: `ft_atoi.c`  
**Funções permitidas**: Nenhuma

#### Descrição
Reproduz o comportamento da função `atoi()` da libc. Converte uma string para inteiro, lidando com espaços em branco e sinais.

#### Conceitos-chave
- Parsing de strings
- Conversão caractere para dígito
- Acumulação de resultado
- Tratamento de sinais

#### Abordagem
1. **Pular whitespace**: espaços, tabs, newlines (ASCII 9-13 e 32)
2. **Verificar sinal**: se '-' ou '+', guardar e avançar
3. **Converter dígitos**: 
   - Para cada dígito: `result = result * 10 + (char - '0')`
   - Parar ao encontrar não-dígito
4. **Aplicar sinal**: multiplicar resultado pelo sinal

#### Como testar
```bash
gcc -Wall -Wextra -Werror ft_atoi.c main.c
./a.out "42"        # Esperado: 42
./a.out "   -123"   # Esperado: -123
./a.out "+456"      # Esperado: 456
./a.out "  \t\n789" # Esperado: 789
```

#### Edge Cases
- Múltiplos espaços
- Tabs e newlines
- Sinal positivo explícito
- Números seguidos de caracteres não-numéricos ("123abc" → 123)

---

### 📝 ft_strcmp

**Arquivos esperados**: `ft_strcmp.c`  
**Funções permitidas**: Nenhuma

#### Descrição
Reproduz o comportamento da função `strcmp()`. Compara duas strings lexicograficamente.

#### Conceitos-chave
- Comparação caractere por caractere
- Valores ASCII
- Retorno de diferença

#### Abordagem
1. Percorrer ambas strings simultaneamente
2. Enquanto caracteres forem iguais E não for '\0', continuar
3. Retornar diferença entre os caracteres atuais

**Retorno**:
- `0`: strings são iguais
- `< 0`: s1 vem antes de s2 lexicograficamente
- `> 0`: s1 vem depois de s2 lexicograficamente

#### Como testar
```bash
gcc -Wall -Wextra -Werror ft_strcmp.c main.c
# Testar: "abc" vs "abc" → 0
# Testar: "abc" vs "abd" → negativo
# Testar: "abd" vs "abc" → positivo
# Testar: "abc" vs "abcd" → negativo
```

---

### 📝 ft_strcspn

**Arquivos esperados**: `ft_strcspn.c`  
**Funções permitidas**: Nenhuma

#### Descrição
Calcula o comprimento do segmento inicial de s1 que não contém nenhum caractere de s2.

#### Conceitos-chave
- Busca de caracteres
- Contagem de posições
- Nested loops

#### Abordagem
1. Para cada caractere de s1:
   - Verificar se existe em s2
   - Se existir, retornar posição atual
   - Se não existir, continuar
2. Se percorrer toda s1, retornar seu tamanho

#### Como testar
```bash
gcc -Wall -Wextra -Werror ft_strcspn.c main.c
# "hello" e "aeiou" → 1 (primeiro 'e' está na posição 1)
# "world" e "aeiou" → 1 (primeiro 'o' está na posição 1)
# "xyz" e "abc" → 3 (nenhum caractere comum)
```

---

### 📝 ft_strdup

**Arquivos esperados**: `ft_strdup.c`  
**Funções permitidas**: `malloc`

#### Descrição
Duplica uma string alocando memória dinamicamente. Retorna ponteiro para nova string ou NULL se falhar.

#### Conceitos-chave
- Alocação dinâmica de memória
- Cálculo de tamanho de string
- Cópia de dados
- Tratamento de erro

#### Abordagem
1. **Calcular tamanho**: percorrer string até '\0'
2. **Alocar memória**: `malloc(sizeof(char) * (len + 1))`
   - +1 é crucial para o '\0'!
3. **Verificar malloc**: se retornou NULL, retornar NULL
4. **Copiar dados**: copiar cada caractere
5. **Adicionar '\0'**: não esquecer o terminador
6. **Retornar ponteiro**: retornar ponteiro para nova string

#### Como testar
```bash
gcc -Wall -Wextra -Werror ft_strdup.c main.c
# Testar com várias strings
# Verificar se cópia é independente (modificar uma não afeta outra)
# Testar string vazia ""
```

#### ⚠️ Armadilhas
- Esquecer +1 no malloc → buffer overflow
- Não verificar retorno de malloc → segfault se falhar
- Não adicionar '\0' → string não terminada

---

### 📝 inter

**Arquivos esperados**: `inter.c`  
**Funções permitidas**: `write`

#### Descrição
Exibe caracteres que aparecem em ambas as strings (interseção), sem duplicatas, na ordem da primeira string.

#### Conceitos-chave
- Operações de conjunto
- Array de marcação (seen array)
- Busca em string

#### Abordagem
1. **Criar array de marcação**: `int seen[256] = {0}`
   - Índice = valor ASCII do caractere
   - Valor = 0 (não visto) ou 1 (já impresso)
2. **Para cada caractere de s1**:
   - Se já foi impresso, pular
   - Buscar em s2
   - Se encontrado: imprimir e marcar como visto

#### Como testar
```bash
gcc -Wall -Wextra -Werror inter.c
./a.out "padinton" "paqefwtdjetyiytjneytjoeyjnejeyj" # Esperado: padinto
./a.out "ddf6vewg64f" "gtwthgdwthdwfteewhrtag6h4ffdhsd" # Esperado: df6ewg4
./a.out "nothing" "This sentence hides nothing" # Esperado: nothig
./a.out | cat -e  # Esperado: $
```

#### Por que usar array de 256?
- ASCII tem 256 valores possíveis (0-255)
- Acesso O(1) para marcar/verificar caractere
- Alternativa seria string auxiliar com busca O(n)

---

### 📝 is_power_of_2

**Arquivos esperados**: `is_power_of_2.c`  
**Funções permitidas**: Nenhuma

#### Descrição
Retorna 1 se o número é uma potência de 2, caso contrário retorna 0.

#### Conceitos-chave
- Manipulação de bits
- Propriedades de potências de 2
- Operador bit a bit AND

#### Abordagem

**Truque matemático**: Um número é potência de 2 se tem apenas um bit 1.

Exemplos em binário:
- 1 = `00000001` (2⁰)
- 2 = `00000010` (2¹)
- 4 = `00000100` (2²)
- 8 = `00001000` (2³)

**Propriedade chave**: Para potência de 2, `n & (n-1)` sempre é 0!

Exemplo com 8:
```
  8 = 00001000
  7 = 00000111
& ────────────
  0 = 00000000
```

Exemplo com 6 (não é potência de 2):
```
  6 = 00000110
  5 = 00000101
& ────────────
  4 = 00000100  (não é zero!)
```

#### Como testar
```bash
gcc -Wall -Wextra -Werror is_power_of_2.c main.c
# Testar: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 → 1
# Testar: 0, 3, 5, 6, 7, 9, 10, 15, 100 → 0
# Testar: números negativos → 0
```

---

### 📝 last_word

**Arquivos esperados**: `last_word.c`  
**Funções permitidas**: `write`

#### Descrição
Exibe a última palavra de uma string. Palavra é definida como sequência de caracteres não-espaço/tab.

#### Conceitos-chave
- Parsing de strings
- Identificação de palavras
- Navegação reversa

#### Abordagem
1. **Ir até o final da string**
2. **Voltar pulando espaços/tabs finais**
3. **Marcar fim da palavra**
4. **Voltar até encontrar espaço/tab ou início**
5. **Imprimir da posição atual até o fim marcado**

#### Como testar
```bash
gcc -Wall -Wextra -Werror last_word.c
./a.out "FOR PONY" | cat -e        # Esperado: PONY$
./a.out "this        ...       is sparta, then again, maybe    not" | cat -e
# Esperado: not$
./a.out "   " | cat -e              # Esperado: $
./a.out "a" "b" | cat -e            # Esperado: $
```

---

### 📝 max

**Arquivos esperados**: `max.c`  
**Funções permitidas**: Nenhuma

#### Descrição
Retorna o maior valor em um array de inteiros. Se array vazio, retorna 0.

#### Conceitos-chave
- Iteração em arrays
- Comparação de valores
- Tratamento de caso vazio

#### Abordagem
1. **Verificar se array vazio**: se len == 0, retornar 0
2. **Inicializar max**: com primeiro elemento
3. **Percorrer array**: comparar cada elemento com max
4. **Atualizar max**: se encontrar valor maior
5. **Retornar max**

#### Como testar
```bash
gcc -Wall -Wextra -Werror max.c main.c
# Testar: [1, 2, 3, 4, 5] → 5
# Testar: [5, 4, 3, 2, 1] → 5
# Testar: [-5, -2, -10, -1] → -1
# Testar: [42] → 42
# Testar: [] (len=0) → 0
```

---

### 📝 print_bits

**Arquivos esperados**: `print_bits.c`  
**Funções permitidas**: `write`

#### Descrição
Imprime a representação binária de um byte (8 bits), do bit mais significativo ao menos significativo.

#### Conceitos-chave
- Representação binária
- Operador shift (>>)
- Operador AND (&)
- Conversão bit para caractere

#### Abordagem

Para imprimir cada bit:
1. **Começar do bit 7** (mais significativo)
2. **Para cada posição i de 7 a 0**:
   - Deslocar byte i posições à direita: `byte >> i`
   - Isolar bit menos significativo: `& 1`
   - Converter para caractere: `+ '0'`
   - Imprimir

**Exemplo com 2 (00000010)**:
- Bit 7: `2 >> 7 = 0`, `0 & 1 = 0` → '0'
- Bit 6: `2 >> 6 = 0`, `0 & 1 = 0` → '0'
- ...
- Bit 1: `2 >> 1 = 1`, `1 & 1 = 1` → '1'
- Bit 0: `2 >> 0 = 2`, `2 & 1 = 0` → '0'
- Resultado: "00000010"

#### Como testar
```bash
gcc -Wall -Wextra -Werror print_bits.c main.c
# Testar: 0 → 00000000
# Testar: 1 → 00000001
# Testar: 2 → 00000010
# Testar: 255 → 11111111
# Testar: 128 → 10000000
```

---

### 📝 snake_to_camel

**Arquivos esperados**: `snake_to_camel.c`  
**Funções permitidas**: `malloc`, `free`, `write`

#### Descrição
Converte string em snake_case para camelCase. Remove underscores e capitaliza letra seguinte.

#### Conceitos-chave
- Detecção de underscore
- Conversão para maiúscula
- Skip de caracteres

#### Abordagem
1. Percorrer string
2. Se encontrar '_':
   - Pular o '_'
   - Converter próximo caractere para maiúscula (- 32)
   - Escrever
3. Caso contrário, escrever caractere normalmente

#### Como testar
```bash
gcc -Wall -Wextra -Werror snake_to_camel.c
./a.out "here_is_a_snake_case_word" # Esperado: hereIsASnakeCaseWord
./a.out "hello_world"                # Esperado: helloWorld
./a.out "camel_case"                 # Esperado: camelCase
```

---

### 📝 swap_bits

**Arquivos esperados**: `swap_bits.c`  
**Funções permitidas**: Nenhuma

#### Descrição
Troca os 4 bits mais significativos com os 4 bits menos significativos de um byte.

#### Conceitos-chave
- Nibbles (grupos de 4 bits)
- Operadores shift
- Operador OR

#### Abordagem

Um byte tem 8 bits = 2 nibbles de 4 bits cada.

**Exemplo**: 0b01000001 (65)
- Nibble alto: 0100 (bits 7-4)
- Nibble baixo: 0001 (bits 3-0)
- Após swap: 0b00010100 (20)

**Algoritmo**:
1. **Extrair nibble alto**: `(byte >> 4) & 0x0F`
   - Shift 4 posições à direita
   - AND com 0x0F (00001111) para garantir apenas 4 bits
2. **Extrair nibble baixo**: `(byte << 4) & 0xF0`
   - Shift 4 posições à esquerda
   - AND com 0xF0 (11110000) para garantir apenas 4 bits
3. **Combinar**: OR entre os dois

#### Como testar
```bash
gcc -Wall -Wextra -Werror swap_bits.c main.c
# Testar: 65 (01000001) → 20 (00010100)
# Testar: 0 → 0
# Testar: 255 (11111111) → 255
# Testar: 1 (00000001) → 16 (00010000)
```

---

### 📝 union

**Arquivos esperados**: `union.c`  
**Funções permitidas**: `write`

#### Descrição
Exibe caracteres que aparecem em qualquer uma das strings (união), sem duplicatas, na ordem de aparição.

#### Conceitos-chave
- Operações de conjunto
- Array de marcação
- Ordem de processamento

#### Abordagem
1. **Criar array de marcação**: `int seen[256] = {0}`
2. **Processar primeira string**:
   - Para cada caractere não visto: imprimir e marcar
3. **Processar segunda string**:
   - Para cada caractere não visto: imprimir e marcar

#### Como testar
```bash
gcc -Wall -Wextra -Werror union.c
./a.out "zpadinton" "paqefwtdjetyiytjneytjoeyjnejeyj" | cat -e
# Esperado: zpadintoqefwjy$
./a.out "ddf6vewg64f" "gtwthgdwthdwfteewhrtag6h4ffdhsd" | cat -e
# Esperado: df6vewg4thras$
./a.out "rien" "cette phrase ne cache rien" | cat -e
# Esperado: rienct phas$
```

#### Diferença entre inter e union
- **inter**: apenas caracteres em AMBAS (interseção: A ∩ B)
- **union**: caracteres em QUALQUER UMA (união: A ∪ B)

---

## Resumo de Complexidade

| Exercício | Tempo | Espaço | Notas |
|-----------|-------|--------|-------|
| alpha_mirror | O(n) | O(1) | n = tamanho da string |
| camel_to_snake | O(n) | O(1) | Apenas escrita |
| do_op | O(1) | O(1) | Operações aritméticas simples |
| ft_atoi | O(n) | O(1) | n = tamanho da string |
| ft_strcmp | O(min(n,m)) | O(1) | Para até primeiro caractere diferente |
| ft_strcspn | O(n*m) | O(1) | n e m = tamanhos das strings |
| ft_strdup | O(n) | O(n) | Aloca nova string |
| inter | O(n*m) | O(1) | Array fixo de 256 |
| is_power_of_2 | O(1) | O(1) | Operação bit a bit |
| last_word | O(n) | O(1) | n = tamanho da string |
| max | O(n) | O(1) | n = tamanho do array |
| print_bits | O(1) | O(1) | Sempre 8 bits |
| snake_to_camel | O(n) | O(1) | Apenas escrita |
| swap_bits | O(1) | O(1) | Operações bit a bit |
| union | O(n+m) | O(1) | Array fixo de 256 |

---

## Checklist de Preparação

Antes de considerar-se pronto para o Nível 1, certifique-se de que consegue:

- [ ] Explicar o que é um ponteiro e como usá-lo
- [ ] Usar malloc corretamente e verificar retorno
- [ ] Calcular tamanho necessário para alocar strings (+1 para '\0')
- [ ] Entender e usar operadores bit a bit (&, |, ^, ~, <<, >>)
- [ ] Converter string para número (implementar atoi)
- [ ] Comparar strings caractere por caractere
- [ ] Usar array de marcação para tracking de caracteres
- [ ] Identificar e tratar edge cases (NULL, vazio, etc.)
- [ ] Compilar com -Wall -Wextra -Werror sem warnings
- [ ] Desenhar diagramas de memória e bits no papel

---

## Recursos Adicionais para Estudo

### Tópicos para Aprofundar

1. **Ponteiros**:
   - Ponteiros para ponteiros
   - Ponteiros para funções
   - Diferença entre array e ponteiro

2. **Memória**:
   - Stack vs Heap
   - Memory leaks e como evitá-los
   - Valgrind para detecção de erros de memória

3. **Bits**:
   - Representação de números negativos (complemento de 2)
   - Máscaras de bits
   - Flags e bitfields

4. **Strings**:
   - String literals vs arrays de char
   - Funções da string.h
   - Manipulação eficiente de strings

### Prática Recomendada

1. Implemente cada exercício sem olhar a solução
2. Compare sua solução com a fornecida
3. Teste com edge cases que você mesmo criar
4. Refaça exercícios que achou difíceis
5. Tente otimizar suas soluções
6. Explique sua solução em voz alta (rubber duck debugging)

---

**Próximo passo**: Quando dominar o Nível 1, avance para o [Nível 2](../level-2/README.md) que introduz algoritmos matemáticos, listas encadeadas e parsing mais complexo.

**Voltar**: [Nível 0](../level-0/README.md) | [Índice Principal](../README.md)
