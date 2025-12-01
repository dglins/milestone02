# Guia de Estudos - Exam 02 da 42 School

## 📚 Sobre este Guia

Este é um guia completo de estudos para o Exam 02 da 42 School, contendo soluções comentadas e explicações didáticas para todos os 49 exercícios organizados por nível de dificuldade (0 a 3).

**O que você encontrará neste guia:**
- ✅ Soluções completas e funcionais para todos os 49 exercícios
- ✅ Código comentado linha por linha
- ✅ Explicações detalhadas dos algoritmos
- ✅ Conceitos-chave por nível de dificuldade
- ✅ Exemplos de compilação e teste
- ✅ Dicas de preparação para o exame
- ✅ Análise de complexidade
- ✅ Armadilhas comuns e como evitá-las

## 📖 Tabela de Conteúdos

- [Como Usar Este Guia](#-como-usar-este-guia)
- [Estrutura por Níveis](#-estrutura-por-níveis)
  - [Level 0 - Básico (12 exercícios)](#level-0---básico-12-exercícios)
  - [Level 1 - Intermediário (15 exercícios)](#level-1---intermediário-15-exercícios)
  - [Level 2 - Avançado (15 exercícios)](#level-2---avançado-15-exercícios)
  - [Level 3 - Expert (7 exercícios)](#level-3---expert-7-exercícios)
- [Índice Completo de Exercícios](#-índice-completo-de-exercícios)
- [Compilação e Testes](#-compilação-e-testes)
- [Dicas Gerais de Preparação](#-dicas-gerais-de-preparação)
- [Normas da 42](#-normas-da-42)
- [Resumo de Conceitos por Nível](#-resumo-de-conceitos-por-nível)

## 🎯 Como Usar Este Guia

### Para Iniciantes
1. **Comece pelo Level 0** - não pule etapas!
2. **Leia o README do nível** antes de ver as soluções
3. **Tente resolver sozinho** primeiro (pelo menos 15-20 minutos)
4. **Compare sua solução** com a fornecida
5. **Estude os comentários** no código para entender a lógica
6. **Compile e teste** as soluções para ver como funcionam

### Para Estudantes Intermediários
1. **Revise conceitos** que você tem dificuldade
2. **Foque nos níveis 1 e 2** para consolidar conhecimento
3. **Pratique variações** dos exercícios
4. **Analise a complexidade** das soluções
5. **Tente otimizar** suas próprias implementações

### Para Preparação Final do Exame
1. **Faça simulações** cronometradas
2. **Revise os exercícios** que você achou mais difíceis
3. **Memorize padrões** comuns (não o código completo!)
4. **Pratique compilação** com as flags corretas
5. **Revise edge cases** importantes

### Progressão Recomendada
```
Level 0 (2-3 dias) → Level 1 (1 semana) → Level 2 (1 semana) → Level 3 (1-2 semanas)
```

## 📊 Estrutura por Níveis

### Level 0 - Básico (12 exercícios)
**Conceitos**: Loops básicos, condicionais, manipulação de strings, I/O básico

- first_word
- fizzbuzz
- ft_putstr
- ft_strcpy
- ft_strlen
- ft_swap
- repeat_alpha
- rev_print
- rot_13
- rotone
- search_and_replace
- ulstr

### Level 1 - Intermediário (15 exercícios)
**Conceitos**: Ponteiros, alocação de memória, manipulação de bits, conversões

- alpha_mirror
- camel_to_snake
- do_op
- ft_atoi
- ft_strcmp
- ft_strcspn
- ft_strdup
- inter
- is_power_of_2
- last_word
- max
- print_bits
- snake_to_camel
- swap_bits
- union

### Level 2 - Avançado (15 exercícios)
**Conceitos**: Algoritmos matemáticos, listas encadeadas, parsing complexo

- add_prime_sum
- epur_str
- expand_str
- ft_atoi_base
- ft_list_size
- ft_range
- ft_rrange
- hidenp
- lcm
- paramsum
- pgcd
- print_hex
- rstr_capitalizer
- str_capitalizer
- tab_mult

### Level 3 - Expert (7 exercícios)
**Conceitos**: Recursão, algoritmos avançados, estruturas de dados complexas

- flood_fill
- fprime
- ft_itoa
- ft_split
- rev_wstr
- rostring
- sort_list

## 🔧 Compilação e Testes

Todas as soluções devem ser compiladas com as flags obrigatórias da 42:

```bash
gcc -Wall -Wextra -Werror arquivo.c
./a.out [argumentos]
```

### Exemplos Práticos de Compilação e Teste

#### Exemplo 1: Programa sem argumentos (fizzbuzz)
```bash
cd level-0
gcc -Wall -Wextra -Werror fizzbuzz.c
./a.out
# Saída: 1, 2, fizz, 4, buzz, fizz, 7, ...
```

#### Exemplo 2: Programa com argumentos (first_word)
```bash
cd level-0
gcc -Wall -Wextra -Werror first_word.c
./a.out "hello world"        # Saída: hello
./a.out "   hello world"     # Saída: hello
./a.out ""                   # Saída: (newline)
./a.out                      # Saída: (newline)
```

#### Exemplo 3: Função com main de teste (ft_strlen)
```bash
cd level-0
# Criar arquivo main.c para testar
cat > main.c << 'EOF'
#include <stdio.h>

int ft_strlen(char *str);

int main(void)
{
    printf("%d\n", ft_strlen("Hello"));      // Deve imprimir: 5
    printf("%d\n", ft_strlen(""));           // Deve imprimir: 0
    printf("%d\n", ft_strlen("42 School")); // Deve imprimir: 9
    return (0);
}
EOF

gcc -Wall -Wextra -Werror ft_strlen.c main.c
./a.out
```

#### Exemplo 4: Testando com diferentes entradas (ulstr)
```bash
cd level-0
gcc -Wall -Wextra -Werror ulstr.c
./a.out "Hello World"        # Saída: hELLO wORLD
./a.out "aBc123"             # Saída: AbC123
./a.out "HELLO"              # Saída: hello
```

### Dicas de Teste

- **Sempre teste edge cases**: strings vazias, NULL, valores extremos
- **Verifique warnings**: Compile sempre com `-Wall -Wextra -Werror`
- **Use valgrind** (quando aplicável): `valgrind ./a.out` para detectar memory leaks
- **Compare com funções originais**: Use `man` para ver comportamento esperado

## 💡 Dicas Gerais de Preparação

1. **Pratique regularmente**: Resolva pelo menos 2-3 exercícios por dia
2. **Entenda, não decore**: Foque em compreender a lógica, não em memorizar código
3. **Gerencie seu tempo**: No exame real, você tem tempo limitado
4. **Teste edge cases**: Sempre teste com entradas vazias, NULL, etc.
5. **Leia o subject com atenção**: Cada detalhe importa
6. **Compile frequentemente**: Não deixe para compilar só no final

## 📖 Índice de Exercícios

### Level 0 - Exercícios Básicos

📘 **[Guia Completo do Level 0](level-0/README.md)** - Leia primeiro para entender os conceitos fundamentais!

#### Exercícios de Output Simples
1. **[fizzbuzz](level-0/fizzbuzz.c)** - Imprime números de 1 a 100 com substituições
   - Conceitos: loops, condicionais, módulo, conversão de números
   - Dificuldade: ⭐⭐
   
2. **[ft_putstr](level-0/ft_putstr.c)** - Imprime uma string
   - Conceitos: iteração, write, ponteiros
   - Dificuldade: ⭐

3. **[first_word](level-0/first_word.c)** - Imprime a primeira palavra
   - Conceitos: argc/argv, whitespace, validação
   - Dificuldade: ⭐⭐

#### Exercícios de Manipulação de Strings
4. **[ft_strcpy](level-0/ft_strcpy.c)** - Copia uma string
   - Conceitos: ponteiros, cópia, terminador nulo
   - Dificuldade: ⭐

5. **[ft_strlen](level-0/ft_strlen.c)** - Retorna comprimento de string
   - Conceitos: iteração, contador, terminador nulo
   - Dificuldade: ⭐

6. **[rev_print](level-0/rev_print.c)** - Imprime string em ordem reversa
   - Conceitos: iteração reversa, cálculo de comprimento
   - Dificuldade: ⭐⭐

7. **[ulstr](level-0/ulstr.c)** - Inverte maiúsculas/minúsculas
   - Conceitos: ASCII, conversão de case
   - Dificuldade: ⭐

#### Exercícios de Transformação de Caracteres
8. **[repeat_alpha](level-0/repeat_alpha.c)** - Repete letras por posição no alfabeto
   - Conceitos: ASCII, cálculo de posição, loops aninhados
   - Dificuldade: ⭐⭐

9. **[rot_13](level-0/rot_13.c)** - Aplica cifra ROT13
   - Conceitos: cifra, aritmética modular, ASCII
   - Dificuldade: ⭐⭐⭐

10. **[rotone](level-0/rotone.c)** - Rotaciona letras em 1 posição
    - Conceitos: rotação, casos especiais
    - Dificuldade: ⭐⭐

11. **[search_and_replace](level-0/search_and_replace.c)** - Substitui caractere
    - Conceitos: substituição, validação de argumentos
    - Dificuldade: ⭐⭐

#### Exercícios com Ponteiros
12. **[ft_swap](level-0/ft_swap.c)** - Troca valores de dois inteiros
    - Conceitos: ponteiros, passagem por referência
    - Dificuldade: ⭐

### Level 1 - Exercícios Intermediários

📘 **[Guia Completo do Level 1](level-1/README.md)** - Ponteiros, malloc, bits e conversões!

#### Conversão e Comparação
13. **[ft_atoi](level-1/ft_atoi.c)** - Converte string para inteiro
    - Conceitos: parsing, sinais, whitespace
    - Dificuldade: ⭐⭐
    
14. **[ft_strcmp](level-1/ft_strcmp.c)** - Compara duas strings
    - Conceitos: comparação lexicográfica, ponteiros
    - Dificuldade: ⭐
    
15. **[ft_strcspn](level-1/ft_strcspn.c)** - Busca caractere em conjunto
    - Conceitos: busca, nested loops
    - Dificuldade: ⭐⭐
    
16. **[do_op](level-1/do_op.c)** - Calculadora simples
    - Conceitos: operadores aritméticos, argc/argv
    - Dificuldade: ⭐⭐

#### Alocação de Memória
17. **[ft_strdup](level-1/ft_strdup.c)** - Duplica string com malloc
    - Conceitos: malloc, cópia de memória
    - Dificuldade: ⭐⭐

#### Manipulação de Bits
18. **[print_bits](level-1/print_bits.c)** - Imprime byte em binário
    - Conceitos: shift, AND, conversão binária
    - Dificuldade: ⭐⭐⭐
    
19. **[swap_bits](level-1/swap_bits.c)** - Troca nibbles de um byte
    - Conceitos: shift, OR, máscaras de bits
    - Dificuldade: ⭐⭐⭐
    
20. **[is_power_of_2](level-1/is_power_of_2.c)** - Verifica potência de 2
    - Conceitos: propriedades de bits, truque matemático
    - Dificuldade: ⭐⭐

#### Transformação de Strings
21. **[alpha_mirror](level-1/alpha_mirror.c)** - Espelha letras do alfabeto
    - Conceitos: aritmética ASCII, espelhamento
    - Dificuldade: ⭐⭐
    
22. **[camel_to_snake](level-1/camel_to_snake.c)** - camelCase → snake_case
    - Conceitos: detecção de maiúsculas, conversão
    - Dificuldade: ⭐⭐
    
23. **[snake_to_camel](level-1/snake_to_camel.c)** - snake_case → camelCase
    - Conceitos: detecção de underscore, capitalização
    - Dificuldade: ⭐⭐

#### Operações de Conjunto
24. **[inter](level-1/inter.c)** - Interseção de strings
    - Conceitos: array de marcação, conjuntos
    - Dificuldade: ⭐⭐⭐
    
25. **[union](level-1/union.c)** - União de strings
    - Conceitos: array de marcação, ordem de processamento
    - Dificuldade: ⭐⭐⭐

#### Auxiliares
26. **[last_word](level-1/last_word.c)** - Extrai última palavra
    - Conceitos: parsing reverso, identificação de palavras
    - Dificuldade: ⭐⭐
    
27. **[max](level-1/max.c)** - Maior valor em array
    - Conceitos: iteração, comparação
    - Dificuldade: ⭐

### Level 2 - Exercícios Avançados

📘 **[Guia Completo do Level 2](level-2/README.md)** - Algoritmos matemáticos, listas e parsing complexo!

#### Algoritmos Matemáticos
28. **[add_prime_sum](level-2/add_prime_sum.c)** - Soma de números primos
    - Conceitos: teste de primalidade, otimização √n
    - Dificuldade: ⭐⭐⭐
    
29. **[pgcd](level-2/pgcd.c)** - Maior divisor comum (GCD)
    - Conceitos: algoritmo de Euclides, recursão
    - Dificuldade: ⭐⭐⭐
    
30. **[lcm](level-2/lcm.c)** - Mínimo múltiplo comum
    - Conceitos: LCM, GCD, prevenção de overflow
    - Dificuldade: ⭐⭐⭐

#### Conversão de Bases
31. **[ft_atoi_base](level-2/ft_atoi_base.c)** - Converte base N para decimal
    - Conceitos: conversão de bases, validação
    - Dificuldade: ⭐⭐⭐⭐
    
32. **[print_hex](level-2/print_hex.c)** - Imprime em hexadecimal
    - Conceitos: conversão para base 16, recursão
    - Dificuldade: ⭐⭐⭐

#### Listas Encadeadas
33. **[ft_list_size](level-2/ft_list_size.c)** - Conta elementos em lista
    - Conceitos: traversal de lista, ponteiros
    - Dificuldade: ⭐⭐

#### Arrays Dinâmicos
34. **[ft_range](level-2/ft_range.c)** - Array crescente de min a max
    - Conceitos: malloc, preenchimento de arrays
    - Dificuldade: ⭐⭐
    
35. **[ft_rrange](level-2/ft_rrange.c)** - Array decrescente de max a min
    - Conceitos: malloc, ordem reversa
    - Dificuldade: ⭐⭐

#### Manipulação Avançada de Strings
36. **[epur_str](level-2/epur_str.c)** - Remove espaços extras
    - Conceitos: normalização, estado de palavra
    - Dificuldade: ⭐⭐⭐
    
37. **[expand_str](level-2/expand_str.c)** - 3 espaços entre palavras
    - Conceitos: parsing, formatação
    - Dificuldade: ⭐⭐⭐
    
38. **[str_capitalizer](level-2/str_capitalizer.c)** - Capitaliza primeira letra
    - Conceitos: detecção de palavras, conversão de case
    - Dificuldade: ⭐⭐⭐
    
39. **[rstr_capitalizer](level-2/rstr_capitalizer.c)** - Capitaliza última letra
    - Conceitos: lookahead, capitalização reversa
    - Dificuldade: ⭐⭐⭐
    
40. **[hidenp](level-2/hidenp.c)** - Verifica subsequência escondida
    - Conceitos: busca de subsequências, two pointers
    - Dificuldade: ⭐⭐⭐

#### Parsing e Contagem
41. **[paramsum](level-2/paramsum.c)** - Conta argumentos
    - Conceitos: argc, contagem simples
    - Dificuldade: ⭐
    
42. **[tab_mult](level-2/tab_mult.c)** - Tabela de multiplicação
    - Conceitos: loops, formatação de output
    - Dificuldade: ⭐⭐

### Level 3 - Exercícios Expert

📘 **[Guia Completo do Level 3](level-3/README.md)** - Recursão avançada, algoritmos complexos e estruturas de dados!

#### Algoritmos Recursivos e de Grafos
43. **[flood_fill](level-3/flood_fill.c)** - Preenchimento por inundação
    - Conceitos: recursão múltipla, 4 direções, verificação de limites
    - Dificuldade: ⭐⭐⭐⭐
    - Tempo estimado: 45-60 min
    
44. **[fprime](level-3/fprime.c)** - Fatoração prima
    - Conceitos: divisão sucessiva, otimização √n
    - Dificuldade: ⭐⭐⭐
    - Tempo estimado: 20-30 min

#### Conversão Numérica Avançada
45. **[ft_itoa](level-3/ft_itoa.c)** - Inteiro para string
    - Conceitos: conversão, malloc, INT_MIN
    - Dificuldade: ⭐⭐⭐
    - Tempo estimado: 30-45 min

#### Parsing e Split Complexo
46. **[ft_split](level-3/ft_split.c)** - Divide string em palavras
    - Conceitos: múltiplos mallocs, parsing, array de strings
    - Dificuldade: ⭐⭐⭐⭐⭐
    - Tempo estimado: 60-90 min

#### Manipulação Expert de Strings
47. **[rev_wstr](level-3/rev_wstr.c)** - Palavras em ordem reversa
    - Conceitos: parsing reverso, formatação
    - Dificuldade: ⭐⭐⭐
    - Tempo estimado: 30-40 min
    
48. **[rostring](level-3/rostring.c)** - Rotaciona primeira palavra para o fim
    - Conceitos: rotação, parsing de palavras
    - Dificuldade: ⭐⭐⭐
    - Tempo estimado: 30-40 min

#### Estruturas de Dados Avançadas
49. **[sort_list](level-3/sort_list.c)** - Ordena lista encadeada
    - Conceitos: bubble sort, ponteiros para funções
    - Dificuldade: ⭐⭐⭐⭐
    - Tempo estimado: 40-50 min

## 📝 Normas da 42

### Regras Essenciais

Durante o exame, você DEVE seguir as normas da 42:

#### Estrutura de Código
- ✅ **Máximo 25 linhas por função** (excluindo chaves)
- ✅ **Máximo 5 funções por arquivo**
- ✅ **Máximo 80 colunas por linha**
- ✅ **Sem variáveis globais**
- ✅ **Declarações no início do bloco** (C89 style)

#### Funções Permitidas
- ⚠️ **Use APENAS as funções listadas no subject**
- ⚠️ **Funções comuns permitidas**: `write`, `malloc`, `free`
- ⚠️ **Algumas permitem**: `printf`, `atoi`, etc. (verifique o subject!)
- ❌ **Nunca use funções não autorizadas** (resulta em 0)

#### Boas Práticas
- ✅ **Nomes de variáveis descritivos** (não `i`, `j` para tudo)
- ✅ **Comentários quando necessário** (mas não excessivos)
- ✅ **Indentação consistente** (tabs ou espaços, não misture)
- ✅ **Sem código morto** (código comentado ou não usado)

#### Compilação
```bash
# Sempre compile com estas flags:
gcc -Wall -Wextra -Werror arquivo.c

# Sem warnings = código limpo!
```

### Checklist Antes de Submeter

- [ ] Código compila sem warnings com `-Wall -Wextra -Werror`
- [ ] Nenhuma função tem mais de 25 linhas
- [ ] Não há mais de 5 funções por arquivo
- [ ] Apenas funções permitidas foram usadas
- [ ] Testei com casos normais e edge cases
- [ ] Não há memory leaks (se aplicável)
- [ ] Nomes de arquivos estão corretos (case-sensitive!)

## 📊 Resumo de Conceitos por Nível

### Level 0 - Fundamentos (12 exercícios)
**Tempo de estudo**: 2-3 dias  
**Conceitos principais**:
- ✅ Loops básicos (`while`, `for`)
- ✅ Condicionais (`if`, `else`)
- ✅ Manipulação básica de strings
- ✅ I/O com `write`
- ✅ Iteração e contadores
- ✅ Conversão de caracteres (ASCII)
- ✅ Argumentos de linha de comando (`argc`, `argv`)

**Quando você domina o Level 0**:
- Consegue iterar sobre strings
- Entende terminador nulo (`\0`)
- Sabe usar `write` para output
- Compreende valores ASCII
- Consegue validar argumentos

### Level 1 - Intermediário (15 exercícios)
**Tempo de estudo**: 1 semana  
**Conceitos principais**:
- ✅ Ponteiros e aritmética de ponteiros
- ✅ Alocação dinâmica (`malloc`, `free`)
- ✅ Manipulação de bits (shift, AND, OR, XOR)
- ✅ Conversão string ↔ número (`atoi`)
- ✅ Comparação e busca em strings
- ✅ Operações de conjunto (interseção, união)
- ✅ Array de marcação (seen array)

**Quando você domina o Level 1**:
- Usa ponteiros com confiança
- Aloca memória corretamente
- Entende operações bit a bit
- Implementa conversões numéricas
- Trabalha com arrays de 256 posições

### Level 2 - Avançado (15 exercícios)
**Tempo de estudo**: 1 semana  
**Conceitos principais**:
- ✅ Algoritmos matemáticos (primos, GCD, LCM)
- ✅ Conversão entre bases numéricas
- ✅ Listas encadeadas (traversal, contagem)
- ✅ Arrays dinâmicos
- ✅ Normalização de strings
- ✅ Capitalização condicional
- ✅ Busca de subsequências
- ✅ Análise de complexidade

**Quando você domina o Level 2**:
- Implementa algoritmo de Euclides
- Testa primalidade eficientemente
- Trabalha com listas encadeadas
- Converte entre bases
- Analisa complexidade O(n), O(n²), O(log n)

### Level 3 - Expert (7 exercícios)
**Tempo de estudo**: 1-2 semanas  
**Conceitos principais**:
- ✅ Recursão avançada (múltiplas chamadas)
- ✅ Algoritmos de grafos (flood fill)
- ✅ Fatoração prima
- ✅ Conversão numérica complexa (INT_MIN)
- ✅ Parsing e split com múltiplos mallocs
- ✅ Manipulação expert de palavras
- ✅ Ordenação de estruturas de dados
- ✅ Ponteiros para funções

**Quando você domina o Level 3**:
- Implementa recursão sem medo
- Gerencia memória complexa sem leaks
- Resolve problemas algorítmicos avançados
- Debuga eficientemente
- Está pronto para o exame! 🎉

## 🎯 Estratégia de Preparação para o Exame

### 4 Semanas Antes
- [ ] Complete todos os exercícios do Level 0
- [ ] Complete todos os exercícios do Level 1
- [ ] Leia os READMEs de cada nível
- [ ] Entenda os conceitos fundamentais

### 2 Semanas Antes
- [ ] Complete todos os exercícios do Level 2
- [ ] Comece os exercícios do Level 3
- [ ] Refaça exercícios que achou difíceis
- [ ] Pratique sem olhar as soluções

### 1 Semana Antes
- [ ] Complete todos os exercícios do Level 3
- [ ] Faça simulações cronometradas (2-3 horas)
- [ ] Revise conceitos-chave de cada nível
- [ ] Pratique compilação e teste rápido

### 1 Dia Antes
- [ ] Revise exercícios mais difíceis
- [ ] Releia dicas de cada nível
- [ ] Descanse bem!
- [ ] Confie na sua preparação

### Durante o Exame
1. **Leia o subject completamente** antes de começar
2. **Identifique o nível** do exercício
3. **Desenhe exemplos** se necessário
4. **Escreva código limpo** desde o início
5. **Teste com edge cases** antes de submeter
6. **Gerencie seu tempo** (não fique preso em um exercício)

## 🔗 Links Rápidos

### Guias Completos por Nível
- 📘 [Level 0 - Guia Completo](level-0/README.md) - Fundamentos essenciais
- 📘 [Level 1 - Guia Completo](level-1/README.md) - Ponteiros e malloc
- 📘 [Level 2 - Guia Completo](level-2/README.md) - Algoritmos avançados
- 📘 [Level 3 - Guia Completo](level-3/README.md) - Recursão e estruturas

### Diretórios de Código
- 📁 [level-0/](level-0/) - 12 exercícios básicos
- 📁 [level-1/](level-1/) - 15 exercícios intermediários
- 📁 [level-2/](level-2/) - 15 exercícios avançados
- 📁 [level-3/](level-3/) - 7 exercícios expert

## 📈 Estatísticas do Guia

| Métrica | Valor |
|---------|-------|
| **Total de exercícios** | 49 |
| **Linhas de código** | ~2.500+ |
| **Linhas de documentação** | ~5.000+ |
| **Conceitos cobertos** | 30+ |
| **Exemplos de teste** | 100+ |
| **Tempo de estudo estimado** | 4-6 semanas |

## 🚀 Boa Sorte!

Este guia foi criado com dedicação para ajudar você a se preparar da melhor forma possível para o Exam 02. Cada exercício foi cuidadosamente documentado com:

- ✅ Código funcional e testado
- ✅ Comentários explicativos
- ✅ Conceitos teóricos
- ✅ Exemplos práticos
- ✅ Dicas e armadilhas

**Lembre-se**: O sucesso no exame vem da prática consistente e compreensão profunda dos conceitos, não da memorização de código.

**Estude com dedicação, pratique regularmente, e você terá sucesso!** 💪

---

## 📞 Contribuições e Feedback

Este guia é um projeto em constante evolução. Se você encontrar erros, tiver sugestões de melhorias, ou quiser contribuir com explicações adicionais, sinta-se à vontade para:

- Reportar issues
- Sugerir melhorias
- Compartilhar com outros estudantes

**Bons estudos e boa sorte no exame!** 🎓

---

*Última atualização: 2025*  
*Criado com ❤️ para a comunidade 42*
# milestone02
