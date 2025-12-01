/* ************************************************************************** */
/*                                                                            */
/*   is_power_of_2.c                                                          */
/*                                                                            */
/*   Verifica se um número é uma potência de 2                               */
/*   Retorna 1 se for potência de 2, 0 caso contrário                        */
/*                                                                            */
/* ************************************************************************** */

int	is_power_of_2(unsigned int n)
{
	// Um número é potência de 2 se:
	// 1. É maior que 0
	// 2. Tem apenas um bit 1 em sua representação binária
	//
	// Truque: n & (n - 1) zera o bit 1 mais à direita
	// Se n é potência de 2, tem apenas um bit 1, então n & (n - 1) == 0
	//
	// Exemplos:
	// 8 (1000) & 7 (0111) = 0 -> é potência de 2
	// 6 (0110) & 5 (0101) = 4 (0100) != 0 -> não é potência de 2
	
	if (n == 0)
		return (0);
	
	return ((n & (n - 1)) == 0);
}
