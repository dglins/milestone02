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

/* Algoritmo de Euclides para calcular o GCD (Greatest Common Divisor)
 * 
 * O GCD é necessário para calcular o LCM de forma eficiente
 * usando a fórmula: LCM(a, b) = (a * b) / GCD(a, b)
 */
unsigned int	gcd(unsigned int a, unsigned int b)
{
	/* Caso base: quando b é 0, o GCD é a */
	if (b == 0)
		return (a);
	/* Recursão: GCD(a, b) = GCD(b, a mod b) */
	return (gcd(b, a % b));
}

/* Calcula o Menor Múltiplo Comum (Lowest Common Multiple)
 * 
 * LCM é o menor número positivo que é divisível por ambos a e b
 * 
 * Fórmula: LCM(a, b) = |a * b| / GCD(a, b)
 * 
 * Casos especiais:
 * - Se a ou b é 0, LCM é 0
 * - Se a e b são coprimos (GCD = 1), LCM = a * b
 * 
 * Exemplo: LCM(12, 18)
 *   GCD(12, 18) = 6
 *   LCM(12, 18) = (12 * 18) / 6 = 216 / 6 = 36
 */
unsigned int	lcm(unsigned int a, unsigned int b)
{
	unsigned int	result;

	/* Se algum número é 0, o LCM é 0 */
	if (a == 0 || b == 0)
		return (0);
	
	/* Calcula LCM usando a fórmula: LCM = (a * b) / GCD(a, b)
	 * Dividimos primeiro para evitar overflow em números grandes
	 */
	result = (a / gcd(a, b)) * b;
	
	return (result);
}
