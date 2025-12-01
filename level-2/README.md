# Nível 2 - Avançado

## Visão Geral

O Nível 2 representa um salto significativo em complexidade em relação aos níveis anteriores. Aqui você encontrará exercícios que exigem conhecimento sólido de algoritmos matemáticos, estruturas de dados como listas encadeadas, parsing complexo e manipulação avançada de strings. Este nível testa sua capacidade de implementar algoritmos clássicos e resolver problemas que requerem pensamento algorítmico mais sofisticado.

**Tempo estimado de estudo**: 15-20 horas  
**Número de exercícios**: 15  
**Pré-requisitos**: Domínio completo dos níveis 0 e 1

## Conceitos Principais

### 1. Algoritmos Matemáticos

Os exercícios deste nível introduzem algoritmos matemáticos clássicos que todo programador deve conhecer:

#### **Números Primos**
- **Definição**: Um número primo é divisível apenas por 1 e por ele mesmo
- **Teste de primalidade**: Verificar divisibilidade até √n (otimização importante)
- **Aplicações**: `add_prime_sum`
- **Complexidade**: O(√n) para teste, O(n√n) para soma de primos

#### **Algoritmo de Euclides (GCD/PGCD)**
- **Princípio**: GCD(a, b) = GCD(b, a mod b)
- **Caso base**: GCD(a, 0) = a
- **Por que funciona**: Baseado na propriedade de que o GCD não muda ao subtrair múltiplos
- **Aplicações**: `pgcd`, `lcm`
- **Complexidade**: O(log min(a, b))

#### **Mínimo Múltiplo Comum (LCM)**
- **Fórmula**: LCM(a, b) = (a × b) / GCD(a, b)
- **Relação com GCD**: Sempre calcule o GCD primeiro
- **Cuidado**: Multiplicar antes de dividir pode causar overflow
- **Aplicações**: `lcm`

### 2. Conversão de Bases Numéricas

#### **Sistema Posicional**
- Cada posição representa uma potência da base
- Exemplo em base 16: "1A" = 1×16¹ + 10×16⁰ = 26
- Algoritmo: `result = result * base + digit`

#### **Validação de Dígitos**
- Base 10: '0'-'9'
- Base 16: '0'-'9', 'a'-'f', 'A'-'F'
- Sempre validar se o dígito é menor que a base

#### **Aplicações**
- `ft_atoi_base`: Conversão de qualquer base ≤ 16 para decimal
- `print_hex`: Conversão de decimal para hexadecimal

### 3. Listas Encadeadas

#### **Estrutura Básica**
```c
typedef struct s_list
{
    struct s_list *next;  // Ponteiro para próximo nó
    void          *data;  // Dados do nó
} t_list;
```

#### **Operações Fundamentais**
- **Traversal (Percorrer)**: Seguir ponteiros `next` até NULL
- **Contagem**: Incrementar contador a cada nó
- **Busca**: Comparar dados até encontrar ou chegar ao fim

#### **Padrões Comuns**
```c
// Percorrer lista
while (list)
{
    // processar list->data
    list = list->next;
}
```

#### **Complexidade**
- Acesso: O(n)
- Busca: O(n)
- Inserção no início: O(1)
- Inserção no fim: O(n) sem tail pointer

#### **Aplicações**
- `ft_list_size`: Contagem de elementos

### 4. Alocação Dinâmica de Arrays

#### **Padrão de Alocação**
```c
int *array = (int *)malloc(sizeof(int) * size);
if (!array)
    return (NULL);  // Sempre verificar!
```

#### **Preenchimento de Arrays**
- Usar loops para inicializar valores
- Cuidado com ordem (crescente vs decrescente)
- Lembrar de retornar o ponteiro

#### **Aplicações**
- `ft_range`: Array crescente de min a max
- `ft_rrange`: Array decrescente de max a min

### 5. Manipulação Avançada de Strings

#### **Normalização de Espaços**
- Remover espaços extras no início/fim
- Reduzir múltiplos espaços para um único
- Padrão: detectar transições palavra↔espaço

#### **Capitalização Condicional**
- Identificar início de palavras
- Alternar entre maiúsculas e minúsculas
- Manter controle de estado (dentro/fora de palavra)

#### **Busca de Subsequências**
- Verificar se string A está "escondida" em B
- Não precisa ser contígua
- Algoritmo: avançar em B até encontrar cada char de A

#### **Aplicações**
- `epur_str`, `expand_str`: Normalização de espaços
- `str_capitalizer`, `rstr_capitalizer`: Capitalização
- `hidenp`: Busca de subsequências

### 6. Parsing e Validação de Entrada

#### **Conversão Robusta**
- Ignorar whitespace inicial
- Detectar e processar sinais (+/-)
- Validar cada caractere
- Parar em caractere inválido

#### **Validação de Argumentos**
- Verificar `argc` antes de acessar `argv`
- Validar formato e range de valores
- Retornar valores padrão em caso de erro

## Dicas de Estudo

### Estratégias de Resolução

1. **Entenda o Algoritmo Primeiro**
   - Não comece a codificar imediatamente
   - Escreva o algoritmo em pseudocódigo
   - Teste mentalmente com exemplos simples
   - Identifique casos especiais

2. **Decomponha o Problema**
   - Divida em funções auxiliares menores
   - Cada função deve ter uma responsabilidade clara
   - Teste cada função isoladamente

3. **Pense em Edge Cases**
   - Entrada vazia ou NULL
   - Valores mínimos (0, 1)
   - Valores máximos (INT_MAX)
   - Casos especiais do domínio (ex: 2 é o único primo par)

4. **Otimize Quando Necessário**
   - Primeiro faça funcionar, depois otimize
   - Conheça as complexidades comuns
   - Evite loops desnecessários

### Armadilhas Comuns

#### **1. Overflow em Multiplicações**
```c
// ERRADO: pode causar overflow
int lcm = (a * b) / gcd(a, b);

// CORRETO: divide primeiro
int lcm = a / gcd(a, b) * b;
```

#### **2. Esquecer de Validar Malloc**
```c
// SEMPRE faça isso
int *arr = malloc(sizeof(int) * n);
if (!arr)
    return (NULL);
```

#### **3. Off-by-One em Loops**
```c
// Cuidado com <= vs <
for (i = min; i <= max; i++)  // Inclui max
for (i = 0; i < size; i++)    // Exclui size
```

#### **4. Não Considerar Números Negativos**
```c
// Lembre-se de tratar sinais
if (*str == '-')
{
    sign = -1;
    str++;
}
```

#### **5. Esquecer o Null Terminator**
```c
// Strings em C sempre terminam com '\0'
str[i] = '\0';
```

### Técnicas de Debugging

1. **Printf Debugging**
   ```c
   printf("Debug: i=%d, result=%d\n", i, result);
   ```

2. **Teste com Valores Conhecidos**
   - GCD(12, 8) = 4
   - Primos até 10: 2, 3, 5, 7 (soma = 17)
   - "1A" em base 16 = 26

3. **Valgrind para Memory Leaks**
   ```bash
   valgrind --leak-check=full ./program
   ```

4. **Compilar com Flags de Debug**
   ```bash
   gcc -g -Wall -Wextra -Werror file.c
   ```

## Análise de Complexidade

### Por que Complexidade Importa?

A análise de complexidade ajuda a:
- Prever performance com entradas grandes
- Comparar diferentes algoritmos
- Identificar gargalos
- Passar em testes com time limits

### Notação Big-O Comum

| Complexidade | Nome | Exemplo |
|--------------|------|---------|
| O(1) | Constante | Acesso a array por índice |
| O(log n) | Logarítmica | Busca binária, GCD |
| O(n) | Linear | Percorrer array/lista |
| O(n log n) | Linearítmica | Merge sort, quick sort |
| O(n²) | Quadrática | Bubble sort, nested loops |
| O(2ⁿ) | Exponencial | Fibonacci recursivo ingênuo |

### Análise por Exercício

#### **Algoritmos Matemáticos**
- `is_prime(n)`: O(√n) - só verifica até raiz quadrada
- `add_prime_sum(n)`: O(n√n) - testa n números
- `pgcd(a, b)`: O(log min(a,b)) - algoritmo de Euclides
- `lcm(a, b)`: O(log min(a,b)) - usa GCD

#### **Conversão e Parsing**
- `ft_atoi_base(str, base)`: O(n) onde n = len(str)
- `print_hex(n)`: O(log₁₆ n) - número de dígitos hex

#### **Listas Encadeadas**
- `ft_list_size(list)`: O(n) - percorre toda lista

#### **Arrays Dinâmicos**
- `ft_range(min, max)`: O(n) onde n = max - min + 1
- `ft_rrange(min, max)`: O(n)

#### **Strings**
- `epur_str(str)`: O(n) - um passe pela string
- `expand_str(str)`: O(n)
- `str_capitalizer(str)`: O(n)
- `hidenp(s1, s2)`: O(n + m) - percorre ambas strings

### Otimizações Importantes

#### **1. Teste de Primalidade**
```c
// Ingênuo: O(n)
for (i = 2; i < n; i++)
    if (n % i == 0) return 0;

// Otimizado: O(√n)
for (i = 2; i * i <= n; i++)
    if (n % i == 0) return 0;
```

#### **2. Pular Números Pares**
```c
// Depois de verificar 2, só teste ímpares
if (n % 2 == 0) return 0;
for (i = 3; i * i <= n; i += 2)  // i += 2 !
    if (n % i == 0) return 0;
```

#### **3. Evitar Recálculos**
```c
// RUIM: calcula i*i a cada iteração
while (i * i <= n)

// BOM: calcula uma vez
int limit = sqrt(n);
while (i <= limit)
```

## Exercícios do Nível 2

### Categoria: Algoritmos Matemáticos

#### 1. **add_prime_sum**
- **Descrição**: Soma todos os números primos ≤ n
- **Conceitos**: Números primos, teste de primalidade, otimização
- **Complexidade**: O(n√n)
- **Dica**: Otimize o teste de primalidade para √n

#### 2. **pgcd**
- **Descrição**: Calcula o maior divisor comum (GCD)
- **Conceitos**: Algoritmo de Euclides, recursão, módulo
- **Complexidade**: O(log min(a,b))
- **Dica**: Use a fórmula recursiva GCD(a,b) = GCD(b, a%b)

#### 3. **lcm**
- **Descrição**: Calcula o mínimo múltiplo comum
- **Conceitos**: LCM, GCD, overflow prevention
- **Complexidade**: O(log min(a,b))
- **Dica**: LCM(a,b) = a / GCD(a,b) * b (evita overflow)

### Categoria: Conversão de Bases

#### 4. **ft_atoi_base**
- **Descrição**: Converte string em base N para decimal
- **Conceitos**: Conversão de bases, validação de dígitos
- **Complexidade**: O(n) onde n = comprimento da string
- **Dica**: Valide se cada dígito é < base

#### 5. **print_hex**
- **Descrição**: Imprime número em hexadecimal
- **Conceitos**: Conversão para base 16, recursão
- **Complexidade**: O(log₁₆ n)
- **Dica**: Use recursão ou array para inverter dígitos

### Categoria: Listas Encadeadas

#### 6. **ft_list_size**
- **Descrição**: Conta elementos em lista encadeada
- **Conceitos**: Listas, traversal, ponteiros
- **Complexidade**: O(n)
- **Dica**: Percorra até next == NULL

### Categoria: Arrays Dinâmicos

#### 7. **ft_range**
- **Descrição**: Cria array de min a max (crescente)
- **Conceitos**: Malloc, preenchimento de arrays
- **Complexidade**: O(n) onde n = max - min + 1
- **Dica**: Tamanho = max - min + 1

#### 8. **ft_rrange**
- **Descrição**: Cria array de max a min (decrescente)
- **Conceitos**: Malloc, ordem reversa
- **Complexidade**: O(n)
- **Dica**: Similar a ft_range, mas ordem inversa

### Categoria: Manipulação Avançada de Strings

#### 9. **epur_str**
- **Descrição**: Remove espaços extras, deixa apenas um entre palavras
- **Conceitos**: Normalização, estado (dentro/fora de palavra)
- **Complexidade**: O(n)
- **Dica**: Use flag para rastrear se está em palavra

#### 10. **expand_str**
- **Descrição**: Coloca exatamente 3 espaços entre palavras
- **Conceitos**: Parsing, formatação
- **Complexidade**: O(n)
- **Dica**: Similar a epur_str, mas imprime 3 espaços

#### 11. **str_capitalizer**
- **Descrição**: Primeira letra de cada palavra maiúscula, resto minúscula
- **Conceitos**: Capitalização, detecção de palavras
- **Complexidade**: O(n)
- **Dica**: Palavra começa após espaço/tab

#### 12. **rstr_capitalizer**
- **Descrição**: Última letra de cada palavra maiúscula, resto minúscula
- **Conceitos**: Capitalização reversa, lookahead
- **Complexidade**: O(n)
- **Dica**: Letra é última se próximo char é espaço/tab/null

#### 13. **hidenp**
- **Descrição**: Verifica se s1 está "escondida" em s2
- **Conceitos**: Subsequências, busca
- **Complexidade**: O(n + m)
- **Dica**: Avance em s2 até encontrar cada char de s1

### Categoria: Parsing e Contagem

#### 14. **paramsum**
- **Descrição**: Conta número de argumentos (exceto programa)
- **Conceitos**: argc/argv, contagem simples
- **Complexidade**: O(1)
- **Dica**: Retorne argc - 1

#### 15. **tab_mult**
- **Descrição**: Imprime tabela de multiplicação de 1 a 9
- **Conceitos**: Loops, formatação de output
- **Complexidade**: O(1) - sempre 9 iterações
- **Dica**: Use printf com formato específico

## Como Testar

### Compilação Básica
```bash
gcc -Wall -Wextra -Werror arquivo.c -o programa
./programa [argumentos]
```

### Exemplos de Teste por Exercício

#### add_prime_sum
```bash
./add_prime_sum 10    # Esperado: 17 (2+3+5+7)
./add_prime_sum 5     # Esperado: 10 (2+3+5)
./add_prime_sum 1     # Esperado: 0
```

#### pgcd
```bash
./pgcd 42 10          # Esperado: 2
./pgcd 12 8           # Esperado: 4
./pgcd 17 3           # Esperado: 1
```

#### ft_atoi_base (requer main)
```c
printf("%d\n", ft_atoi_base("1A", 16));  // 26
printf("%d\n", ft_atoi_base("101", 2));  // 5
printf("%d\n", ft_atoi_base("-12", 10)); // -12
```

#### hidenp
```bash
./hidenp "fgex" "tyf34gdgf;'ektufjhgdgex;.p"  # 1
./hidenp "abc" "2altrb53c"                     # 1
./hidenp "abc" "btarc"                         # 0
```

### Testes com Valgrind (para exercícios com malloc)
```bash
gcc -g arquivo.c -o programa
valgrind --leak-check=full ./programa [args]
```

Verifique:
- "All heap blocks were freed" (sem leaks)
- "ERROR SUMMARY: 0 errors" (sem erros)

## Progressão para o Nível 3

Após dominar o Nível 2, você estará pronto para:
- **Algoritmos recursivos complexos** (flood_fill, fprime)
- **Parsing avançado** (ft_split com múltiplos delimitadores)
- **Manipulação de strings expert** (rev_wstr, rostring)
- **Estruturas de dados avançadas** (sort_list)

### Checklist de Preparação

Antes de avançar, certifique-se de que você:
- [ ] Entende e consegue implementar o algoritmo de Euclides
- [ ] Sabe testar se um número é primo eficientemente
- [ ] Consegue converter entre bases numéricas
- [ ] Domina operações básicas com listas encadeadas
- [ ] Sabe alocar e preencher arrays dinâmicos
- [ ] Consegue normalizar e manipular strings complexas
- [ ] Entende análise de complexidade básica
- [ ] Sempre valida malloc e trata erros
- [ ] Testa seus programas com edge cases

## Recursos Adicionais

### Conceitos para Aprofundar
- Crivo de Eratóstenes (algoritmo mais eficiente para múltiplos primos)
- Algoritmo de Euclides estendido
- Conversão entre bases arbitrárias
- Estruturas de dados: listas duplamente encadeadas
- Algoritmos de string matching (KMP, Boyer-Moore)

### Prática Recomendada
1. Implemente cada exercício sem olhar a solução
2. Compare sua solução com a fornecida
3. Analise a complexidade da sua implementação
4. Refatore para melhorar clareza ou eficiência
5. Teste com casos extremos

### Tempo de Estudo Sugerido
- **Primeira passagem**: 2-3 dias (entender todos os exercícios)
- **Prática intensiva**: 1 semana (implementar múltiplas vezes)
- **Revisão**: 2-3 dias antes do exame

Boa sorte nos seus estudos! 🚀
