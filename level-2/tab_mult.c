/* ************************************************************************** */
/*                                                                            */
/*   tab_mult.c                                                               */
/*                                                                            */
/*   Descrição: Exibe a tabuada de multiplicação de um número (1 a 9)        */
/*                                                                            */
/*   Conceitos: Loops, formatação de output, conversão de strings            */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/* Função auxiliar para escrever um caractere */
void	ft_putchar(char c)
{
	write(1, &c, 1);
}

/* Função para escrever um número inteiro */
void	ft_putnbr(int n)
{
	if (n >= 10)
		ft_putnbr(n / 10);
	ft_putchar(n % 10 + '0');
}

/* Converte string para inteiro (atoi simplificado) */
int	ft_atoi(char *str)
{
	int	result;
	int	i;

	result = 0;
	i = 0;
	
	/* Ignora espaços em branco */
	while (str[i] == ' ' || str[i] == '\t')
		i++;
	
	/* Converte dígitos para número */
	while (str[i] >= '0' && str[i] <= '9')
	{
		result = result * 10 + (str[i] - '0');
		i++;
	}
	
	return (result);
}

/* Exibe a tabuada de multiplicação de n (de 1 a 9)
 * 
 * Formato: "i x n = resultado"
 * 
 * Exemplo para n=9:
 *   1 x 9 = 9
 *   2 x 9 = 18
 *   ...
 *   9 x 9 = 81
 */
void	tab_mult(int n)
{
	int	i;

	i = 1;
	while (i <= 9)
	{
		/* Imprime: "i x n = resultado\n" */
		ft_putnbr(i);
		write(1, " x ", 3);
		ft_putnbr(n);
		write(1, " = ", 3);
		ft_putnbr(i * n);
		ft_putchar('\n');
		i++;
	}
}

int	main(int argc, char **argv)
{
	int	n;

	/* Verifica se há exatamente 1 argumento */
	if (argc == 2)
	{
		n = ft_atoi(argv[1]);
		tab_mult(n);
	}
	else
	{
		/* Caso de erro: imprime apenas newline */
		ft_putchar('\n');
	}
	
	return (0);
}
