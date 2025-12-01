/* ************************************************************************** */
/*                                                                            */
/*   fizzbuzz.c                                                               */
/*                                                                            */
/*   Descrição: Imprime números de 1 a 100, substituindo múltiplos de 3      */
/*              por "fizz", múltiplos de 5 por "buzz", e múltiplos de        */
/*              ambos por "fizzbuzz"                                          */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/*
** Função auxiliar para escrever um caractere na saída padrão
*/
void	ft_putchar(char c)
{
	write(1, &c, 1);
}

/*
** Função auxiliar para escrever um número na saída padrão
** Usa recursão para imprimir cada dígito do número
*/
void	ft_putnbr(int n)
{
	if (n > 9)
		ft_putnbr(n / 10);
	ft_putchar(n % 10 + '0');
}

int	main(void)
{
	int	i;

	i = 1;
	while (i <= 100)
	{
		// Verifica se é múltiplo de 3 E 5 (deve vir primeiro)
		if (i % 3 == 0 && i % 5 == 0)
			write(1, "fizzbuzz", 8);
		// Verifica se é múltiplo apenas de 3
		else if (i % 3 == 0)
			write(1, "fizz", 4);
		// Verifica se é múltiplo apenas de 5
		else if (i % 5 == 0)
			write(1, "buzz", 4);
		// Caso contrário, imprime o número
		else
			ft_putnbr(i);
		
		// Imprime newline após cada saída
		write(1, "\n", 1);
		i++;
	}
	return (0);
}
