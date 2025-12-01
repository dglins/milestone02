/* ************************************************************************** */
/*                                                                            */
/*   fprime.c                                                                 */
/*                                                                            */
/*   Descrição: Programa que exibe os fatores primos de um número positivo   */
/*   em ordem crescente, separados por '*'                                    */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	int	number;
	int	divisor;
	int	first;

	// Verifica se há exatamente 1 argumento
	if (argc != 2)
	{
		printf("\n");
		return (0);
	}

	// Converte o argumento para inteiro
	number = atoi(argv[1]);
	
	// Caso especial: número 1
	if (number == 1)
	{
		printf("1");
	}
	
	// Inicia com o menor divisor primo (2)
	divisor = 2;
	first = 1;  // Flag para controlar a impressão do '*'
	
	// Enquanto o número for maior que 1, procura fatores primos
	while (number > 1)
	{
		// Se o divisor atual divide o número
		if (number % divisor == 0)
		{
			// Imprime o separador '*' se não for o primeiro fator
			if (first == 0)
				printf("*");
			
			// Imprime o fator primo
			printf("%d", divisor);
			
			// Divide o número pelo fator encontrado
			number = number / divisor;
			
			// Marca que já imprimimos o primeiro fator
			first = 0;
		}
		else
		{
			// Se não divide, tenta o próximo divisor
			divisor++;
		}
	}
	
	printf("\n");
	return (0);
}
