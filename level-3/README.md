# Nível 3 - Expert

## Visão Geral

O Nível 3 representa o ápice de dificuldade do Exam 02. Estes exercícios exigem domínio completo de todos os conceitos anteriores, além de habilidades avançadas em recursão, algoritmos complexos, manipulação sofisticada de strings e estruturas de dados. Este nível testa sua capacidade de resolver problemas que requerem pensamento algorítmico profundo e implementação cuidadosa.

**Tempo estimado de estudo**: 20-30 horas  
**Número de exercícios**: 7  
**Pré-requisitos**: Domínio completo dos níveis 0, 1 e 2  
**Dificuldade**: Expert - requer experiência sólida em C

## Conceitos Principais

### 1. **Recursão Avançada**

A recursão é uma técnica fundamental onde uma função chama a si mesma para resolver subproblemas menores. No Nível 3, você encontrará recursão em sua forma mais sofisticada.

#### **Anatomia de uma Função Recursiva**

Toda função recursiva bem construída possui:

1. **Caso Base**: Condição que para a recursão
2. **Caso Recursivo**: Chamada da função com problema menor
3. **Progresso**: Cada chamada deve aproximar-se do caso base

```c
void recursiva(int n)
{
    // Caso base: para a recursão
    if (n <= 0)
        return;
    
    // Caso recursivo: problema menor
    recursiva(n - 1);
    
    // Processamento
    printf("%d\n", n);
}
```


#### **Recursão vs Iteração**

| Aspecto | Recursão | Iteração |
|---------|----------|----------|
| **Legibilidade** | Mais natural para problemas recursivos | Mais direta para loops simples |
| **Memória** | Usa call stack (pode causar stack overflow) | Usa memória constante |
| **Performance** | Overhead de chamadas de função | Geralmente mais rápida |
| **Casos de uso** | Árvores, grafos, divisão e conquista | Arrays, listas, contadores |

#### **Padrões Recursivos Comuns**

**1. Recursão Linear** (uma chamada recursiva):
```c
int factorial(int n)
{
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

**2. Recursão Múltipla** (várias chamadas recursivas):
```c
void flood_fill(char **tab, t_point size, t_point cur, char target)
{
    // Caso base
    if (fora_dos_limites || diferente_do_alvo)
        return;
    
    // Processar
    tab[cur.y][cur.x] = 'F';
    
    // 4 chamadas recursivas (cima, baixo, esquerda, direita)
    flood_fill(tab, size, (t_point){cur.x, cur.y - 1}, target);
    flood_fill(tab, size, (t_point){cur.x, cur.y + 1}, target);
    flood_fill(tab, size, (t_point){cur.x - 1, cur.y}, target);
    flood_fill(tab, size, (t_point){cur.x + 1, cur.y}, target);
}
```


**3. Tail Recursion** (chamada recursiva é a última operação):
```c
int sum_tail(int n, int acc)
{
    if (n == 0) return acc;
    return sum_tail(n - 1, acc + n);  // Tail call
}
```

#### **Aplicações no Nível 3**
- **flood_fill**: Recursão múltipla para explorar 4 direções
- **fprime**: Recursão para fatoração prima
- Conversão de números (ft_itoa pode usar recursão)

**Por que é importante**: Recursão é essencial para trabalhar com estruturas hierárquicas (árvores, grafos) e implementar algoritmos de divisão e conquista. Muitos problemas complexos têm soluções recursivas elegantes.

### 2. **Algoritmos de Grafos e Busca**

#### **Flood Fill (Preenchimento por Inundação)**

Algoritmo clássico usado em:
- Paint bucket tools (Photoshop, Paint)
- Detecção de regiões conectadas
- Resolução de labirintos
- Análise de imagens

**Conceito**: A partir de um ponto inicial, preencher todos os pontos conectados que têm o mesmo valor.

**Algoritmo**:
1. Verificar se ponto atual é válido
2. Verificar se tem o valor alvo
3. Marcar ponto atual como visitado
4. Recursivamente processar vizinhos (4 direções)


**Visualização**:
```
Antes:          Depois (começando em X):
. . . . .       F F F F .
. X X . .  -->  F F F F .
. X X . .       F F F F .
. . . . .       . . . . .
```

**Complexidade**: O(n × m) onde n e m são dimensões da matriz - cada célula é visitada no máximo uma vez.

**Cuidados**:
- Verificar limites antes de acessar array
- Evitar recursão infinita (marcar células visitadas)
- Stack overflow em matrizes muito grandes

### 3. **Fatoração Prima**

#### **Conceito**
Todo número inteiro > 1 pode ser expresso como produto de números primos.

**Exemplos**:
- 12 = 2 × 2 × 3
- 42 = 2 × 3 × 7
- 100 = 2 × 2 × 5 × 5

#### **Algoritmo de Fatoração**
1. Começar com divisor = 2
2. Enquanto n > 1:
   - Se n é divisível por divisor:
     - Imprimir divisor
     - Dividir n por divisor
   - Senão:
     - Incrementar divisor
3. Otimização: só precisa testar até √n


**Por que funciona**:
- Se n tem fator > √n, também tem fator < √n
- Ao dividir por fatores pequenos primeiro, eliminamos fatores grandes
- O que sobra no final (se > 1) é primo

**Exemplo com 60**:
```
60 ÷ 2 = 30  → imprime "2"
30 ÷ 2 = 15  → imprime "2"
15 ÷ 3 = 5   → imprime "3"
5 é primo    → imprime "5"
Resultado: 2*2*3*5
```

**Complexidade**: O(√n) no pior caso (número primo)

### 4. **Conversão Numérica Avançada (itoa)**

#### **Desafios da Conversão Int → String**

1. **Calcular número de dígitos**: Quantos caracteres alocar?
2. **Lidar com negativos**: Adicionar '-' e trabalhar com valor absoluto
3. **Ordem dos dígitos**: Extrair dígitos de trás para frente
4. **Caso especial**: INT_MIN (-2147483648) não pode ser negado em int

#### **Técnicas de Implementação**

**Método 1: Recursão**
```c
void print_number(int n)
{
    if (n < 0)
    {
        write(1, "-", 1);
        n = -n;
    }
    if (n >= 10)
        print_number(n / 10);
    char c = (n % 10) + '0';
    write(1, &c, 1);
}
```


**Método 2: Array e Preenchimento Reverso**
```c
char *ft_itoa(int n)
{
    // 1. Calcular tamanho
    int len = get_num_len(n);
    
    // 2. Alocar string
    char *str = malloc(len + 1);
    
    // 3. Preencher de trás para frente
    str[len] = '\0';
    len--;
    while (n > 0)
    {
        str[len--] = (n % 10) + '0';
        n /= 10;
    }
    
    return str;
}
```

**Truque para INT_MIN**: Use `long` para evitar overflow ao negar.

### 5. **Parsing e Split de Strings**

#### **ft_split: O Desafio Definitivo**

Split é um dos exercícios mais complexos porque combina:
- Alocação dinâmica de memória (array de strings)
- Parsing de delimitadores
- Contagem de palavras
- Gerenciamento de múltiplos mallocs

#### **Estrutura de Dados**
```c
char **result;  // Array de ponteiros para strings
// result[0] → "primeira"
// result[1] → "segunda"
// result[2] → "terceira"
// result[3] → NULL
```


#### **Algoritmo em Etapas**

1. **Contar palavras**: Percorrer string identificando transições
2. **Alocar array principal**: `malloc(sizeof(char*) * (words + 1))`
3. **Para cada palavra**:
   - Calcular tamanho da palavra
   - Alocar string individual
   - Copiar caracteres
   - Adicionar '\0'
4. **Adicionar NULL final**: `result[words] = NULL`

**Complexidade**: O(n) onde n é o tamanho da string (assumindo número constante de palavras)

**Armadilhas**:
- Memory leaks se malloc falhar no meio
- Esquecer NULL no final do array
- Off-by-one ao calcular tamanhos
- Não tratar múltiplos espaços consecutivos

### 6. **Manipulação Avançada de Palavras**

#### **Rotação de Palavras**

Exercícios como `rostring` e `rev_wstr` exigem:
- Identificar palavras em uma string
- Reorganizar ordem das palavras
- Manter formatação correta

**Padrões Comuns**:
- Pular espaços iniciais
- Identificar início e fim de cada palavra
- Imprimir com espaçamento correto

#### **Reversão de Palavras**

**rev_wstr**: Imprime palavras em ordem reversa
```
"hello world foo" → "foo world hello"
```

**Abordagem**:
1. Encontrar última palavra
2. Imprimir
3. Encontrar penúltima palavra
4. Repetir


#### **Rotação de Palavras**

**rostring**: Move primeira palavra para o final
```
"hello world foo" → "world foo hello"
```

**Abordagem**:
1. Guardar primeira palavra
2. Imprimir resto das palavras
3. Imprimir primeira palavra no final

### 7. **Ordenação de Listas Encadeadas**

#### **Desafios Únicos**

Ordenar listas encadeadas é diferente de ordenar arrays:
- Não há acesso direto por índice
- Swap de valores é mais fácil que swap de nós
- Algoritmos in-place são mais complexos

#### **Bubble Sort para Listas**

Algoritmo mais simples para listas:
1. Percorrer lista comparando pares adjacentes
2. Se estão fora de ordem, trocar valores
3. Repetir até não haver mais trocas

**Complexidade**: O(n²) - não é eficiente, mas é simples e funciona

**Por que Bubble Sort?**
- Fácil de implementar em listas
- Não requer memória extra
- Suficiente para o exame


**Alternativas mais eficientes** (não necessárias no exame):
- Merge Sort: O(n log n) mas requer mais código
- Quick Sort: O(n log n) médio, complexo para listas

## Dicas de Estudo

### 🎯 Estratégias de Resolução de Problemas Complexos

#### **1. Decomposição em Funções Auxiliares**

Problemas complexos ficam mais gerenciáveis quando divididos:

```c
// Ruim: tudo em uma função gigante
char **ft_split(char *str) { /* 100 linhas */ }

// Bom: dividido em funções auxiliares
int is_space(char c);
int count_words(char *str);
int word_len(char *str);
char *copy_word(char *str, int len);
char **ft_split(char *str);
```

**Benefícios**:
- Cada função é testável isoladamente
- Código mais legível e manutenível
- Mais fácil de debugar
- Reutilização de código

#### **2. Teste Incremental**

Não escreva todo o código de uma vez!

**Processo recomendado**:
1. Escreva função auxiliar simples
2. Teste com printf
3. Escreva próxima função
4. Teste integração
5. Repita até completar


**Exemplo para ft_split**:
```c
// Passo 1: Testar is_space
printf("is_space(' ') = %d\n", is_space(' '));  // Deve ser 1

// Passo 2: Testar count_words
printf("count_words(\"hello world\") = %d\n", count_words("hello world"));  // Deve ser 2

// Passo 3: Testar word_len
printf("word_len(\"hello\") = %d\n", word_len("hello"));  // Deve ser 5

// Passo 4: Testar copy_word
char *word = copy_word("hello", 5);
printf("copy_word = %s\n", word);  // Deve ser "hello"

// Passo 5: Testar ft_split completo
```

#### **3. Desenhe Antes de Codificar**

Para problemas visuais ou com estruturas de dados:

**Flood Fill**: Desenhe a matriz no papel
```
Passo 0:    Passo 1:    Passo 2:    Passo 3:
. . . .     F . . .     F F . .     F F F .
X X . .     F X . .     F F . .     F F F .
X X . .     F X . .     F F . .     F F F .
. . . .     . . . .     . . . .     . . . .
```

**Listas Encadeadas**: Desenhe os nós e ponteiros
```
[3] -> [1] -> [4] -> [2] -> NULL

Após ordenação:
[1] -> [2] -> [3] -> [4] -> NULL
```


#### **4. Pense em Edge Cases Extremos**

Nível 3 requer atenção especial a casos extremos:

**Para ft_split**:
- String vazia: `""`
- Apenas espaços: `"   "`
- Uma palavra: `"hello"`
- Múltiplos espaços: `"hello    world"`
- Espaços no início/fim: `"  hello world  "`

**Para flood_fill**:
- Matriz 1×1
- Ponto inicial na borda
- Toda matriz com mesmo caractere
- Matriz vazia

**Para ft_itoa**:
- 0
- Números negativos
- INT_MIN (-2147483648)
- INT_MAX (2147483647)

**Para sort_list**:
- Lista vazia (NULL)
- Lista com um elemento
- Lista já ordenada
- Lista em ordem reversa

### ⚠️ Armadilhas Comuns no Nível 3

#### **1. Stack Overflow em Recursão**

**Problema**: Recursão muito profunda esgota a stack
```c
// Perigoso para n muito grande
void recursiva(int n)
{
    if (n == 0) return;
    recursiva(n - 1);
}
```


**Solução**: 
- Verificar limites antes de recursão
- Considerar solução iterativa se possível
- Para flood_fill: limites da matriz previnem recursão infinita

#### **2. Memory Leaks em Múltiplos Mallocs**

**Problema**: ft_split aloca múltiplas strings
```c
char **result = malloc(sizeof(char*) * (words + 1));
result[0] = malloc(10);  // OK
result[1] = malloc(10);  // Falha!
// result[0] nunca é liberado → leak
```

**Solução**: Função de limpeza
```c
void free_split(char **split, int count)
{
    int i = 0;
    while (i < count)
        free(split[i++]);
    free(split);
}
```

**No exame**: Geralmente não é necessário liberar, mas é boa prática.

#### **3. INT_MIN em ft_itoa**

**Problema**: `-INT_MIN` causa overflow
```c
int n = -2147483648;
n = -n;  // Overflow! Resultado indefinido
```

**Solução**: Use `long`
```c
long n = nbr;
if (n < 0)
{
    str[0] = '-';
    n = -n;  // Agora é seguro
}
```


#### **4. Esquecer NULL no Final de Arrays**

**Problema**: ft_split deve terminar com NULL
```c
char **result = malloc(sizeof(char*) * (words + 1));
// ... preencher palavras ...
// Esqueceu: result[words] = NULL;
```

**Consequência**: Ao iterar, não sabe onde parar → segfault

**Solução**: Sempre adicione NULL
```c
result[i] = NULL;  // Último elemento
```

#### **5. Não Verificar Limites em Flood Fill**

**Problema**: Acessar fora da matriz
```c
void fill(char **tab, t_point size, t_point cur, char target)
{
    tab[cur.y][cur.x] = 'F';  // Pode estar fora dos limites!
    // ...
}
```

**Solução**: Verificar ANTES de acessar
```c
if (cur.x < 0 || cur.x >= size.x || cur.y < 0 || cur.y >= size.y)
    return;
```

### 🔧 Técnicas de Debugging Avançadas

#### **1. Printf Debugging Estratégico**

Para recursão, indente output para visualizar profundidade:
```c
void debug_fill(int depth, t_point cur)
{
    for (int i = 0; i < depth; i++)
        printf("  ");
    printf("fill(%d, %d)\n", cur.x, cur.y);
}
```


Output:
```
fill(1, 1)
  fill(1, 0)
    fill(2, 0)
  fill(1, 2)
```

#### **2. Visualizar Estruturas de Dados**

Para ft_split, imprima o resultado:
```c
void print_split(char **split)
{
    int i = 0;
    while (split[i])
    {
        printf("[%d]: \"%s\"\n", i, split[i]);
        i++;
    }
    printf("[%d]: NULL\n", i);
}
```

#### **3. Valgrind para Memory Issues**

```bash
gcc -g ft_split.c main.c -o test
valgrind --leak-check=full --track-origins=yes ./test
```

Procure por:
- "definitely lost" → memory leak
- "Invalid read/write" → acesso fora dos limites
- "Conditional jump depends on uninitialised value" → variável não inicializada

#### **4. GDB para Debugging Interativo**

```bash
gcc -g programa.c -o programa
gdb ./programa

(gdb) break ft_split      # Breakpoint na função
(gdb) run "hello world"   # Executar com argumentos
(gdb) print str           # Ver valor de variável
(gdb) next                # Próxima linha
(gdb) step                # Entrar em função
(gdb) continue            # Continuar execução
```


## Análise Completa de Complexidade

### Complexidade de Tempo

| Exercício | Melhor Caso | Caso Médio | Pior Caso | Notas |
|-----------|-------------|------------|-----------|-------|
| **flood_fill** | O(1) | O(n×m) | O(n×m) | Visita cada célula uma vez |
| **fprime** | O(√n) | O(√n) | O(√n) | Testa divisores até √n |
| **ft_itoa** | O(log n) | O(log n) | O(log n) | Número de dígitos |
| **ft_split** | O(n) | O(n) | O(n) | n = tamanho da string |
| **rev_wstr** | O(n) | O(n) | O(n) | Percorre string 2 vezes |
| **rostring** | O(n) | O(n) | O(n) | Um passe pela string |
| **sort_list** | O(n) | O(n²) | O(n²) | Bubble sort |

### Complexidade de Espaço

| Exercício | Espaço | Detalhes |
|-----------|--------|----------|
| **flood_fill** | O(n×m) | Call stack na recursão |
| **fprime** | O(1) | Apenas variáveis locais |
| **ft_itoa** | O(log n) | String com número de dígitos |
| **ft_split** | O(n) | Array de strings + strings individuais |
| **rev_wstr** | O(1) | Apenas escrita, sem alocação |
| **rostring** | O(1) | Apenas escrita, sem alocação |
| **sort_list** | O(1) | Ordenação in-place |

### Análise Detalhada por Exercício

#### **flood_fill: O(n × m) tempo, O(n × m) espaço**

**Tempo**: Cada célula é visitada exatamente uma vez
- Melhor caso: Ponto inicial já é 'F' → O(1)
- Pior caso: Toda matriz tem mesmo caractere → O(n×m)


**Espaço**: Call stack da recursão
- Profundidade máxima = n×m (pior caso: caminho em espiral)
- Na prática, geralmente muito menor

**Trade-off**: Versão iterativa com queue usa O(n×m) espaço explícito mas evita stack overflow.

#### **fprime: O(√n) tempo, O(1) espaço**

**Tempo**: Testa divisores de 2 até √n
- Se n é primo: testa todos até √n
- Se n tem fatores pequenos: termina mais rápido

**Otimização**: Após testar 2, só testa ímpares → 2× mais rápido

**Espaço**: Apenas variáveis locais (divisor, n)

#### **ft_itoa: O(log₁₀ n) tempo e espaço**

**Tempo**: Proporcional ao número de dígitos
- 10 tem 2 dígitos → 2 operações
- 100 tem 3 dígitos → 3 operações
- 1000 tem 4 dígitos → 4 operações

**Espaço**: String com tamanho = número de dígitos + 1 (para '\0') + 1 (para sinal se negativo)

#### **ft_split: O(n) tempo, O(n) espaço**

**Tempo**: 
- Contar palavras: O(n)
- Copiar cada palavra: O(n) total
- Total: O(n)

**Espaço**:
- Array de ponteiros: O(w) onde w = número de palavras
- Strings individuais: O(n) total
- Total: O(n)


#### **sort_list: O(n²) tempo, O(1) espaço**

**Tempo**: Bubble sort clássico
- Melhor caso (já ordenada): O(n) com flag de otimização
- Pior caso (ordem reversa): O(n²)

**Espaço**: Ordenação in-place, apenas variáveis temporárias

**Alternativas**:
- Merge sort: O(n log n) mas O(n) espaço
- Quick sort: O(n log n) médio mas complexo para listas

## Trade-offs e Otimizações

### 1. Recursão vs Iteração

#### **Quando usar Recursão**:
✅ Problema naturalmente recursivo (árvores, grafos)  
✅ Código mais limpo e legível  
✅ Profundidade limitada e conhecida  

#### **Quando usar Iteração**:
✅ Performance crítica  
✅ Profundidade muito grande (risco de stack overflow)  
✅ Memória limitada  

**Exemplo**: flood_fill
- Recursivo: Mais elegante, mas pode causar stack overflow
- Iterativo com queue: Mais robusto, mas mais código

### 2. Bubble Sort vs Algoritmos Mais Eficientes

#### **Bubble Sort (O(n²))**:
✅ Simples de implementar  
✅ Funciona bem para listas pequenas  
✅ Ordenação in-place (O(1) espaço)  
❌ Lento para listas grandes  


#### **Merge Sort (O(n log n))**:
✅ Muito mais rápido para listas grandes  
✅ Performance consistente  
❌ Mais complexo de implementar  
❌ Requer O(n) espaço extra  

**No exame**: Bubble sort é suficiente e mais rápido de implementar.

### 3. Alocação de Memória: Tudo de Uma Vez vs Incremental

#### **ft_split: Duas Abordagens**

**Abordagem 1: Contar primeiro, alocar depois**
```c
int words = count_words(str);
char **result = malloc(sizeof(char*) * (words + 1));
// Preencher result
```
✅ Aloca tamanho exato  
✅ Mais eficiente em memória  
❌ Dois passes pela string  

**Abordagem 2: Realloc dinâmico**
```c
char **result = NULL;
int capacity = 0;
// Para cada palavra: realloc se necessário
```
✅ Um passe pela string  
❌ Múltiplos reallocs (mais lento)  
❌ Pode desperdiçar memória  

**Recomendação**: Abordagem 1 é melhor para o exame.

### 4. Otimizações Específicas

#### **fprime: Pular Números Pares**
```c
// Básico
for (int i = 2; i <= n; i++)

// Otimizado
if (n % 2 == 0) { /* processar 2 */ }
for (int i = 3; i <= n; i += 2)  // Só ímpares
```
**Ganho**: ~2× mais rápido


#### **ft_itoa: Calcular Tamanho vs Realloc**
```c
// Eficiente: calcular tamanho primeiro
int len = get_num_len(n);
char *str = malloc(len + 1);

// Ineficiente: realloc conforme necessário
char *str = malloc(1);
// ... realloc a cada dígito
```
**Ganho**: Evita múltiplos reallocs

#### **sort_list: Early Exit**
```c
int swapped = 1;
while (swapped)
{
    swapped = 0;
    // ... se fizer swap, swapped = 1
}
```
**Ganho**: Para quando lista já está ordenada

## Exercícios do Nível 3

### 📝 flood_fill

**Arquivos esperados**: `flood_fill.c`  
**Funções permitidas**: Nenhuma  
**Estrutura fornecida**: `t_point`

#### Descrição
Implementa o algoritmo de flood fill (preenchimento por inundação). A partir de um ponto inicial, preenche com 'F' todos os pontos conectados que têm o mesmo caractere.

#### Conceitos-chave
- Recursão múltipla (4 direções)
- Verificação de limites
- Algoritmo de busca em grafos
- Estruturas (t_point)


#### Abordagem
1. Guardar caractere alvo na posição inicial
2. Criar função recursiva auxiliar que:
   - Verifica se posição é válida (dentro dos limites)
   - Verifica se caractere é igual ao alvo
   - Marca posição atual como 'F'
   - Chama recursivamente para 4 direções (cima, baixo, esquerda, direita)

#### Diagrama
```
Entrada (begin = {1,1}):     Saída:
. . . . .                    F F F F .
. X X . .                    F F F F .
. X X . .                    F F F F .
. . . . .                    . . . . .

Ordem de preenchimento:
1. (1,1) → F
2. (1,0) → F  (cima)
3. (2,0) → F  (direita de 1,0)
4. (2,1) → F  (baixo de 2,0)
5. (2,2) → F  (baixo de 2,1)
6. (1,2) → F  (esquerda de 2,2)
7. (0,2) → F  (esquerda de 1,2)
8. (0,1) → F  (cima de 0,2)
9. (0,0) → F  (cima de 0,1)
10. (3,0) → F (direita de 2,0)
```

#### Como testar
```c
// Criar matriz de teste
char **make_area(char **zone, t_point size)
{
    char **new = malloc(sizeof(char*) * size.y);
    for (int i = 0; i < size.y; i++)
    {
        new[i] = malloc(size.x + 1);
        for (int j = 0; j < size.x; j++)
            new[i][j] = zone[i][j];
        new[i][size.x] = '\0';
    }
    return new;
}


// Testar
char *zone[] = {
    ".....",
    ".XXX.",
    ".XXX.",
    "....."
};
t_point size = {5, 4};
t_point begin = {1, 1};
char **area = make_area(zone, size);
flood_fill(area, size, begin);
// Imprimir resultado
```

#### Complexidade
- **Tempo**: O(n × m) - cada célula visitada uma vez
- **Espaço**: O(n × m) - call stack da recursão

#### Dicas
- Sempre verifique limites ANTES de acessar array
- Não esqueça de verificar se caractere é igual ao alvo
- Recursão para automaticamente quando não há mais células válidas

---

### 📝 fprime

**Arquivos esperados**: `fprime.c`  
**Funções permitidas**: `printf`, `atoi`

#### Descrição
Imprime a fatoração prima de um número. Fatores devem ser impressos em ordem crescente, separados por '*'.

#### Conceitos-chave
- Fatoração prima
- Divisão sucessiva
- Otimização até √n
- Formatação de output


#### Abordagem
1. Validar entrada (argc == 2, número > 1)
2. Converter string para número
3. Para cada divisor começando em 2:
   - Enquanto n é divisível por divisor:
     - Imprimir divisor (com '*' se não for o primeiro)
     - Dividir n por divisor
   - Incrementar divisor
4. Se n > 1 no final, imprimir n (é primo)

#### Exemplos
```bash
./fprime 225225
# Saída: 3*3*5*5*7*11*13

./fprime 8333325
# Saída: 3*3*5*5*7*11*13*37

./fprime 9539
# Saída: 9539 (número primo)

./fprime 1
# Saída: (newline)
```

#### Otimização
```c
// Básico: testa todos os números
for (int i = 2; i <= n; i++)

// Otimizado: só precisa testar até √n
// Porque se n tem fator > √n, também tem fator < √n
for (int i = 2; i * i <= n; i++)
```

#### Complexidade
- **Tempo**: O(√n) no pior caso (número primo)
- **Espaço**: O(1)

#### Dicas
- Imprima '*' entre fatores, não antes do primeiro
- Após o loop, se n > 1, ele é um fator primo
- Não precisa verificar se divisor é primo (divisores compostos já foram eliminados)

---


### 📝 ft_itoa

**Arquivos esperados**: `ft_itoa.c`  
**Funções permitidas**: `malloc`

#### Descrição
Converte um inteiro em string alocada dinamicamente. Deve lidar com números negativos e INT_MIN.

#### Conceitos-chave
- Conversão numérica
- Alocação dinâmica
- Cálculo de tamanho
- Caso especial: INT_MIN

#### Abordagem
1. **Calcular tamanho necessário**:
   - Contar dígitos
   - Adicionar 1 se negativo (para '-')
   - Adicionar 1 para '\0'
2. **Alocar memória**: `malloc(tamanho + 1)`
3. **Tratar sinal**: Se negativo, adicionar '-' e trabalhar com valor absoluto
4. **Preencher string de trás para frente**:
   - Extrair último dígito: `n % 10`
   - Converter para char: `+ '0'`
   - Remover último dígito: `n / 10`

#### Exemplo de Execução
```
ft_itoa(-1234):
1. Calcular tamanho: 4 dígitos + 1 sinal = 5 + 1 ('\0') = 6
2. Alocar: str[6]
3. str[5] = '\0'
4. str[0] = '-'
5. n = 1234 (valor absoluto)
6. str[4] = '4', n = 123
7. str[3] = '3', n = 12
8. str[2] = '2', n = 1
9. str[1] = '1', n = 0
10. Retornar "-1234"
```


#### Caso Especial: INT_MIN

**Problema**: INT_MIN = -2147483648
- Negar causa overflow: `-(-2147483648)` não cabe em int

**Solução**: Use `long`
```c
long n = nbr;
if (n < 0)
{
    str[0] = '-';
    n = -n;  // Seguro porque n é long
}
```

#### Como testar
```c
char *s;

s = ft_itoa(0);
printf("%s\n", s);  // "0"
free(s);

s = ft_itoa(-1234);
printf("%s\n", s);  // "-1234"
free(s);

s = ft_itoa(2147483647);  // INT_MAX
printf("%s\n", s);  // "2147483647"
free(s);

s = ft_itoa(-2147483648);  // INT_MIN
printf("%s\n", s);  // "-2147483648"
free(s);
```

#### Complexidade
- **Tempo**: O(log₁₀ n) - número de dígitos
- **Espaço**: O(log₁₀ n) - tamanho da string

#### Dicas
- Use `long` para evitar overflow com INT_MIN
- Preencha de trás para frente (mais fácil)
- Não esqueça o '\0'
- Caso especial: 0 tem 1 dígito

---


### 📝 ft_split

**Arquivos esperados**: `ft_split.c`  
**Funções permitidas**: `malloc`

#### Descrição
Divide uma string em palavras (separadas por espaços, tabs, newlines) e retorna array de strings terminado em NULL.

#### Conceitos-chave
- Alocação dinâmica múltipla
- Parsing de delimitadores
- Array de ponteiros
- Gerenciamento de memória complexo

#### Abordagem

**Passo 1: Funções Auxiliares**
```c
int is_space(char c);           // Verifica se é whitespace
int count_words(char *str);     // Conta palavras
int word_len(char *str);        // Tamanho da palavra atual
char *copy_word(char *str, int len);  // Copia palavra
```

**Passo 2: Algoritmo Principal**
1. Contar número de palavras
2. Alocar array de ponteiros: `malloc(sizeof(char*) * (words + 1))`
3. Para cada palavra:
   - Pular espaços
   - Calcular tamanho da palavra
   - Alocar e copiar palavra
   - Adicionar ao array
4. Adicionar NULL no final

#### Diagrama de Memória
```
Input: "hello world foo"

result → [ptr0] → "hello\0"
         [ptr1] → "world\0"
         [ptr2] → "foo\0"
         [NULL]
```


#### Exemplo de Execução
```
Input: "  hello   world  "

1. count_words: 2
2. Alocar result[3] (2 palavras + NULL)
3. Pular espaços iniciais → "hello   world  "
4. word_len("hello...") = 5
5. copy_word("hello", 5) → result[0] = "hello"
6. Avançar 5 caracteres → "   world  "
7. Pular espaços → "world  "
8. word_len("world...") = 5
9. copy_word("world", 5) → result[1] = "world"
10. result[2] = NULL
```

#### Como testar
```c
char **result = ft_split("  hello   world  ");
int i = 0;
while (result[i])
{
    printf("[%d]: \"%s\"\n", i, result[i]);
    i++;
}
// Saída:
// [0]: "hello"
// [1]: "world"

// Liberar memória
i = 0;
while (result[i])
    free(result[i++]);
free(result);
```

#### Edge Cases
- String vazia: `""` → array com apenas NULL
- Apenas espaços: `"   "` → array com apenas NULL
- Uma palavra: `"hello"` → array com 1 palavra + NULL
- Múltiplos espaços: `"a    b"` → array com 2 palavras

#### Complexidade
- **Tempo**: O(n) onde n = tamanho da string
- **Espaço**: O(n) para armazenar todas as palavras


#### Dicas
- Divida em funções auxiliares pequenas
- Teste cada função isoladamente
- Sempre adicione NULL no final do array
- Verifique retorno de malloc
- Whitespace = espaço, tab, newline

---

### 📝 rev_wstr

**Arquivos esperados**: `rev_wstr.c`  
**Funções permitidas**: `write`, `malloc`

#### Descrição
Imprime palavras de uma string em ordem reversa, separadas por um espaço.

#### Conceitos-chave
- Parsing de palavras
- Ordem reversa
- Formatação de output

#### Abordagem

**Método 1: Encontrar e Imprimir de Trás para Frente**
1. Ir até o final da string
2. Voltar pulando espaços finais
3. Marcar fim da palavra
4. Voltar até início da palavra
5. Imprimir palavra
6. Repetir até início da string

**Método 2: Usar ft_split**
1. Dividir string em palavras
2. Imprimir array de trás para frente

#### Exemplo
```bash
./rev_wstr "hello world foo bar"
# Saída: bar foo world hello

./rev_wstr "   hello   world  "
# Saída: world hello

./rev_wstr "a"
# Saída: a
```


#### Diagrama
```
Input: "hello world foo"
       ^           ^
       start       end

Passo 1: Encontrar última palavra
"hello world foo"
             ^^^
             
Passo 2: Imprimir "foo"

Passo 3: Encontrar penúltima palavra
"hello world foo"
       ^^^^^
       
Passo 4: Imprimir " world"

Passo 5: Encontrar primeira palavra
"hello world foo"
 ^^^^^
 
Passo 6: Imprimir " hello"

Resultado: "foo world hello"
```

#### Complexidade
- **Tempo**: O(n) - percorre string 2 vezes
- **Espaço**: O(1) - apenas escrita, sem alocação

#### Dicas
- Não imprima espaço antes da primeira palavra (última na ordem original)
- Imprima espaço antes das demais palavras
- Sempre termine com newline

---

### 📝 rostring

**Arquivos esperados**: `rostring.c`  
**Funções permitidas**: `write`, `malloc`

#### Descrição
Move a primeira palavra para o final, mantendo as demais na ordem original. Palavras separadas por exatamente um espaço.


#### Conceitos-chave
- Parsing de palavras
- Rotação de elementos
- Formatação de output

#### Abordagem
1. Pular espaços iniciais
2. Guardar início e fim da primeira palavra
3. Pular espaços após primeira palavra
4. Imprimir resto das palavras (com espaços entre elas)
5. Imprimir espaço + primeira palavra no final

#### Exemplo
```bash
./rostring "hello world foo bar"
# Saída: world foo bar hello

./rostring "   hello   world  "
# Saída: world hello

./rostring "a b c"
# Saída: b c a

./rostring "a"
# Saída: a
```

#### Diagrama
```
Input: "hello world foo"
        ^^^^^           primeira palavra
              ^^^^^^^^^^  resto

Output: "world foo hello"
        ^^^^^^^^^^  resto (impresso primeiro)
                   ^^^^^  primeira palavra (impresso no final)
```

#### Casos Especiais
- Uma palavra: imprimir normalmente
- String vazia: imprimir newline
- Apenas espaços: imprimir newline

#### Complexidade
- **Tempo**: O(n)
- **Espaço**: O(1) se não usar malloc, O(n) se guardar primeira palavra


#### Dicas
- Guarde ponteiros para início e fim da primeira palavra
- Imprima espaço entre palavras, não no início ou fim
- Trate caso de uma única palavra

---

### 📝 sort_list

**Arquivos esperados**: `sort_list.c`, `list.h`  
**Funções permitidas**: Nenhuma  
**Estrutura fornecida**: `t_list`

#### Descrição
Ordena uma lista encadeada usando uma função de comparação fornecida. A função de comparação retorna valor diferente de 0 se os elementos estão na ordem correta.

#### Conceitos-chave
- Listas encadeadas
- Algoritmos de ordenação
- Ponteiros para funções
- Bubble sort

#### Estrutura
```c
typedef struct s_list
{
    int           data;
    struct s_list *next;
} t_list;
```

#### Abordagem (Bubble Sort)
1. Se lista vazia ou um elemento, retornar (já ordenada)
2. Repetir até não haver trocas:
   - Percorrer lista comparando pares adjacentes
   - Se `cmp(a, b) == 0` (ordem errada), trocar valores
   - Marcar que houve troca
3. Retornar lista


#### Exemplo de Execução
```
Lista inicial: 3 → 1 → 4 → 2 → NULL

Passagem 1:
3 vs 1: cmp(3,1)=0 → trocar → 1 → 3 → 4 → 2
3 vs 4: cmp(3,4)≠0 → OK     → 1 → 3 → 4 → 2
4 vs 2: cmp(4,2)=0 → trocar → 1 → 3 → 2 → 4

Passagem 2:
1 vs 3: cmp(1,3)≠0 → OK     → 1 → 3 → 2 → 4
3 vs 2: cmp(3,2)=0 → trocar → 1 → 2 → 3 → 4
3 vs 4: cmp(3,4)≠0 → OK     → 1 → 2 → 3 → 4

Passagem 3:
Nenhuma troca → lista ordenada!
```

#### Função de Comparação
```c
// Ordem crescente
int ascending(int a, int b)
{
    return (a <= b);  // Retorna != 0 se ordem correta
}

// Ordem decrescente
int descending(int a, int b)
{
    return (a >= b);
}
```

#### Como testar
```c
// Criar lista: 3 → 1 → 4 → 2
t_list *list = malloc(sizeof(t_list));
list->data = 3;
list->next = malloc(sizeof(t_list));
list->next->data = 1;
// ... continuar

// Ordenar
list = sort_list(list, ascending);

// Imprimir
t_list *tmp = list;
while (tmp)
{
    printf("%d ", tmp->data);
    tmp = tmp->next;
}
// Saída: 1 2 3 4
```


#### Complexidade
- **Tempo**: O(n²) pior caso, O(n) melhor caso (já ordenada)
- **Espaço**: O(1) - ordenação in-place

#### Dicas
- Troque valores (data), não nós (mais simples)
- Use flag para detectar quando lista está ordenada
- Retorne o ponteiro original da lista
- Trate lista vazia e lista com um elemento

---

## Resumo de Preparação

### Checklist de Conceitos para Dominar

Antes de considerar-se pronto para o Nível 3, certifique-se de que consegue:

- [ ] Implementar recursão com múltiplas chamadas
- [ ] Entender e evitar stack overflow
- [ ] Implementar flood fill em matriz 2D
- [ ] Calcular fatoração prima eficientemente
- [ ] Converter inteiro para string (incluindo INT_MIN)
- [ ] Implementar ft_split com múltiplos mallocs
- [ ] Manipular palavras em strings (reverter, rotacionar)
- [ ] Ordenar lista encadeada com bubble sort
- [ ] Usar ponteiros para funções
- [ ] Gerenciar memória complexa sem leaks
- [ ] Debugar com printf, valgrind e gdb
- [ ] Analisar complexidade de algoritmos
- [ ] Identificar e otimizar gargalos


### Ordem Sugerida de Estudo

1. **Primeiro** (mais acessíveis):
   - ft_itoa: Conversão numérica fundamental
   - fprime: Algoritmo matemático clássico

2. **Segundo** (recursão):
   - flood_fill: Introdução a recursão múltipla
   - Pratique desenhar a execução no papel

3. **Terceiro** (strings avançadas):
   - rev_wstr: Manipulação de palavras
   - rostring: Rotação de palavras

4. **Quarto** (estruturas de dados):
   - sort_list: Ordenação de listas

5. **Por último** (mais complexo):
   - ft_split: Combina tudo (malloc, parsing, arrays)

### Tempo de Prática Recomendado

- **Primeira implementação**: 1-2 horas por exercício
- **Revisão e otimização**: 30-45 minutos por exercício
- **Prática antes do exame**: 15-20 minutos por exercício
- **Total para dominar o nível**: 20-30 horas

### Estratégia para o Exame

1. **Leia o subject completamente** antes de começar
2. **Identifique o tipo de problema** (recursão, parsing, etc.)
3. **Desenhe exemplos** no papel
4. **Escreva funções auxiliares** primeiro
5. **Teste incrementalmente** com printf
6. **Verifique edge cases** antes de submeter


## Recursos Adicionais para Estudo

### Conceitos para Aprofundar

1. **Algoritmos de Grafos**:
   - BFS (Breadth-First Search)
   - DFS (Depth-First Search)
   - Flood fill iterativo com queue

2. **Algoritmos de Ordenação**:
   - Merge sort para listas
   - Quick sort
   - Análise de complexidade

3. **Recursão Avançada**:
   - Tail recursion optimization
   - Memoization
   - Backtracking

4. **Estruturas de Dados**:
   - Listas duplamente encadeadas
   - Árvores binárias
   - Hash tables

### Recursos Online Recomendados

- **Visualização de Algoritmos**: VisuAlgo.net
- **Prática de Recursão**: LeetCode (problemas de recursão)
- **Debugging**: Tutorial de GDB e Valgrind
- **Complexidade**: Big-O Cheat Sheet

### Livros Úteis

- "The C Programming Language" - Kernighan & Ritchie
- "Introduction to Algorithms" - CLRS
- "Data Structures and Algorithm Analysis in C" - Mark Allen Weiss


## Tabela Comparativa de Exercícios

| Exercício | Dificuldade | Conceito Principal | Tempo Estimado | Armadilhas Principais |
|-----------|-------------|-------------------|----------------|----------------------|
| **ft_itoa** | ⭐⭐⭐ | Conversão numérica | 30-45 min | INT_MIN overflow |
| **fprime** | ⭐⭐⭐ | Fatoração prima | 20-30 min | Formatação do output |
| **flood_fill** | ⭐⭐⭐⭐ | Recursão múltipla | 45-60 min | Stack overflow, limites |
| **rev_wstr** | ⭐⭐⭐ | Parsing reverso | 30-40 min | Espaçamento correto |
| **rostring** | ⭐⭐⭐ | Rotação de palavras | 30-40 min | Casos especiais |
| **sort_list** | ⭐⭐⭐⭐ | Ordenação de listas | 40-50 min | Lógica de comparação |
| **ft_split** | ⭐⭐⭐⭐⭐ | Parsing + malloc | 60-90 min | Memory leaks, NULL final |

### Legenda de Dificuldade
- ⭐⭐⭐: Desafiador mas direto
- ⭐⭐⭐⭐: Complexo, requer planejamento
- ⭐⭐⭐⭐⭐: Muito complexo, múltiplos conceitos

## Mensagem Final

O Nível 3 representa o ponto culminante do Exam 02. Dominar estes exercícios significa que você desenvolveu habilidades sólidas em:

✅ Pensamento algorítmico avançado  
✅ Recursão e suas aplicações  
✅ Gerenciamento complexo de memória  
✅ Estruturas de dados fundamentais  
✅ Debugging e otimização  

Estas habilidades são fundamentais não apenas para passar no exame, mas para se tornar um programador competente em C e além.

**Lembre-se**:
- A prática leva à perfeição
- Entenda o "porquê", não apenas o "como"
- Desenhe antes de codificar
- Teste incrementalmente
- Não desista quando encontrar dificuldades

Boa sorte nos seus estudos e no exame! 🚀

---

**Voltar**: [Nível 2](../level-2/README.md) | [Índice Principal](../README.md)

