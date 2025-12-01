/* ************************************************************************** */
/*                                                                            */
/*   hidenp.c                                                                 */
/*                                                                            */
/*   Descrição: Verifica se a primeira string está "escondida" na segunda    */
/*              (todos os caracteres aparecem na mesma ordem).                */
/*                                                                            */
/*   Conceitos: Subsequência, two pointers, busca em string                  */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/* Verifica se s1 é uma subsequência de s2
 * 
 * Algoritmo (two pointers):
 * 1. Usa dois índices: i para s1, j para s2
 * 2. Para cada caractere de s2:
 *    - Se corresponde ao caractere atual de s1, avança i
 *    - Sempre avança j
 * 3. Se i chegou ao fim de s1, todos os caracteres foram encontrados
 * 
 * Exemplo: s1="abc", s2="aXbXc"
 *   'a' encontrado -> i=1
 *   'X' ignorado
 *   'b' encontrado -> i=2
 *   'X' ignorado
 *   'c' encontrado -> i=3 (fim de s1) -> retorna 1
 */
int	hidenp(char *s1, char *s2)
{
	int	i;
	int	j;

	i = 0;
	j = 0;

	/* Percorre s2 procurando caracteres de s1 em ordem */
	while (s2[j])
	{
		/* Se encontrou o próximo caractere de s1 */
		if (s1[i] && s1[i] == s2[j])
			i++;
		j++;
	}

	/* Se chegou ao fim de s1, todos os caracteres foram encontrados */
	return (s1[i] == '\0');
}

int	main(int argc, char **argv)
{
	/* Verifica se há exatamente 2 argumentos */
	if (argc == 3)
	{
		/* Imprime 1 se s1 está escondida em s2, 0 caso contrário */
		if (hidenp(argv[1], argv[2]))
			write(1, "1", 1);
		else
			write(1, "0", 1);
	}
	
	/* Sempre imprime newline */
	write(1, "\n", 1);
	return (0);
}
