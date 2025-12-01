/* ************************************************************************** */
/*                                                                            */
/*   print_hex.c                                                              */
/*                                                                            */
/*   Descrição: Converte um número decimal para hexadecimal (minúsculas)     */
/*                                                                            */
/*   Conceitos: Conversão de bases, recursão, representação hexadecimal      */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

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

/* Imprime um número em hexadecimal (base 16)
 * 
 * Algoritmo recursivo:
 * 1. Se n >= 16, chama recursivamente com n/16 (dígitos mais significativos)
 * 2. Imprime o dígito atual (n % 16)
 * 
 * Exemplo: 255 em hex
 *   255 / 16 = 15 (f), 255 % 16 = 15 (f)
 *   Resultado: ff
 */
void	print_hex(int n)
{
	char	*hex_digits;

	hex_digits = "0123456789abcdef";
	
	/* Se o número tem mais de um dígito hex, processa recursivamente */
	if (n >= 16)
		print_hex(n / 16);
	
	/* Imprime o dígito hexadecimal correspondente */
	write(1, &hex_digits[n % 16], 1);
}

int	main(int argc, char **argv)
{
	int	n;

	/* Verifica se há exatamente 1 argumento */
	if (argc == 2)
	{
		n = ft_atoi(argv[1]);
		print_hex(n);
	}
	/* Sempre imprime newline no final */
	write(1, "\n", 1);
	return (0);
}
