/* ************************************************************************** */
/*                                                                            */
/*   lcm.c                                                                    */
/*                                                                            */
/*   Descrição: Calcula o menor múltiplo comum (LCM) de dois números usando  */
/*              a relação LCM(a,b) = |a * b| / GCD(a,b)                       */
/*                                                                            */
/*   Conceitos: LCM, GCD, algoritmo de Euclides, relação matemática          */
/*                                                                            */
/* ************************************************************************** */

#include <limits.h> /* INT_MAX, UINT_MAX */
#include <stdint.h> /* uint64_t */

/* Algoritmo de Euclides para calcular o GCD (Greatest Common Divisor) */
unsigned int	gcd(unsigned int a, unsigned int b)
{
	if (b == 0)
		return (a);
	return (gcd(b, a % b));
}


unsigned int	lcm(unsigned int a, unsigned int b)
{
	unsigned int	g;
	uint64_t		tmp;

	/* Se algum é 0, LCM é 0 */
	if (a == 0 || b == 0)
		return (0);

	/* Detecta valores que provavelmente vieram de inteiros negativos */
	if (a > (unsigned int)INT_MAX || b > (unsigned int)INT_MAX)
		return (0);

	g = gcd(a, b);

	/* Usa 64 bits temporários para evitar overflow durante a multiplicação */
	tmp = (uint64_t)(a / g) * (uint64_t)b;
	return ((unsigned int)tmp);
}
