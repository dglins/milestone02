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

int	main(int argc, char *argv[])
{
	if (argc == 2)
	{
		int	num = atoi(argv[1]);
		int	i = 2;

		if (num == 1)
			printf("1");
		while (i <= num)
		{
			if (num % i == 0)
			{
				printf("%d", i);
				if (num == i)
					break;
				printf("*");
				num /= i;
			}
			else
				i++;
		}
	}
	printf("\n");
}
