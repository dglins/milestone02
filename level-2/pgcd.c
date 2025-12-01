/* ************************************************************************** */
/*                                                                            */
/*   pgcd.c                                                                   */
/*                                                                            */
/*   Descrição: Calcula o maior divisor comum (GCD/PGCD) de dois números     */
/*              usando o algoritmo de Euclides.                               */
/*                                                                            */
/*   Conceitos: Algoritmo de Euclides, recursão, divisão modular             */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

/* Algoritmo de Euclides para calcular o GCD (Greatest Common Divisor)
 * 
 * Princípio: GCD(a, b) = GCD(b, a % b)
 * Caso base: GCD(a, 0) = a
 * 
 * Exemplo: GCD(42, 10)
 *   GCD(42, 10) = GCD(10, 42 % 10) = GCD(10, 2)
 *   GCD(10, 2)  = GCD(2, 10 % 2)   = GCD(2, 0)
 *   GCD(2, 0)   = 2
 */
unsigned int	pgcd(unsigned int a, unsigned int b)
{
	/* Caso base: quando b é 0, o GCD é a */
	if (b == 0)
		return (a);
	/* Recursão: GCD(a, b) = GCD(b, a mod b) */
	return (pgcd(b, a % b));
}

int	main(int argc, char **argv)
{
	unsigned int	a;
	unsigned int	b;

	/* Verifica se há exatamente 2 argumentos */
	if (argc == 3)
	{
		/* Converte strings para inteiros */
		a = atoi(argv[1]);
		b = atoi(argv[2]);
		/* Calcula e imprime o PGCD */
		printf("%u\n", pgcd(a, b));
	}
	else
	{
		/* Caso de erro: imprime apenas newline */
		printf("\n");
	}
	return (0);
}
