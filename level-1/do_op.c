/* ************************************************************************** */
/*                                                                            */
/*   do_op.c                                                                  */
/*                                                                            */
/*   Programa que realiza operações aritméticas básicas                      */
/*   Uso: ./do_op "num1" "operador" "num2"                                   */
/*   Operadores suportados: + - * / %                                        */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	main(int argc, char **argv)
{
	int	num1;
	int	num2;
	int	result = 0;

	// Verifica se foram passados exatamente 3 argumentos
	if (argc != 4)
	{
		printf("\n");
		return (0);
	}

	// Converte os argumentos para inteiros
	num1 = atoi(argv[1]);
	num2 = atoi(argv[3]);

	// Realiza a operação baseada no operador
	if (argv[2][0] == '+')
		result = num1 + num2;
	else if (argv[2][0] == '-')
		result = num1 - num2;
	else if (argv[2][0] == '*')
		result = num1 * num2;
	else if (argv[2][0] == '/')
		result = num1 / num2;
	else if (argv[2][0] == '%')
		result = num1 % num2;

	// Imprime o resultado
	printf("%d\n", result);

	return (0);
}
