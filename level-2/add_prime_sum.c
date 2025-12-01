/* ************************************************************************** */
/*                                                                            */
/*   add_prime_sum.c                                                          */
/*                                                                            */
/*   Descrição: Calcula a soma de todos os números primos menores ou iguais  */
/*              ao número fornecido como argumento.                           */
/*                                                                            */
/*   Conceitos: Números primos, validação de entrada, conversão de strings   */
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

/* Verifica se um número é primo
 * Um número é primo se é divisível apenas por 1 e por ele mesmo
 * Otimização: só precisa verificar até a raiz quadrada do número
 */
int	is_prime(int n)
{
	int	i;

	/* Números menores que 2 não são primos */
	if (n <= 1)
		return (0);
	/* 2 é o único número primo par */
	if (n == 2)
		return (1);
	/* Números pares não são primos */
	if (n % 2 == 0)
		return (0);
	/* Verifica divisibilidade por números ímpares até sqrt(n) */
	i = 3;
	while (i * i <= n)
	{
		if (n % i == 0)
			return (0);
		i += 2;
	}
	return (1);
}

/* Calcula a soma de todos os primos <= n */
int	sum_primes(int n)
{
	int	sum;
	int	i;

	sum = 0;
	i = 2;
	/* Itera de 2 até n, somando todos os primos encontrados */
	while (i <= n)
	{
		if (is_prime(i))
			sum += i;
		i++;
	}
	return (sum);
}

int	main(int argc, char **argv)
{
	int	n;

	/* Verifica se há exatamente 1 argumento */
	if (argc == 2)
	{
		n = ft_atoi(argv[1]);
		/* Verifica se o número é positivo */
		if (n > 0)
		{
			ft_putnbr(sum_primes(n));
			ft_putchar('\n');
			return (0);
		}
	}
	/* Caso de erro: imprime 0 */
	ft_putchar('0');
	ft_putchar('\n');
	return (0);
}
