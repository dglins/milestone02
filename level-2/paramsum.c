/* ************************************************************************** */
/*                                                                            */
/*   paramsum.c                                                               */
/*                                                                            */
/*   Descrição: Conta e exibe o número de argumentos passados ao programa    */
/*                                                                            */
/*   Conceitos: argc, contagem de parâmetros, conversão de números           */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/* Função auxiliar para escrever um caractere */
void	ft_putchar(char c)
{
	write(1, &c, 1);
}

/* Função para escrever um número inteiro
 * 
 * Usa recursão para imprimir dígitos da esquerda para direita
 */
void	ft_putnbr(int n)
{
	/* Se o número tem mais de um dígito, imprime recursivamente */
	if (n >= 10)
		ft_putnbr(n / 10);
	
	/* Imprime o dígito atual */
	ft_putchar(n % 10 + '0');
}

/* Conta e exibe o número de argumentos
 * 
 * argc - 1 porque argc inclui o nome do programa
 * 
 * Exemplos:
 *   ./paramsum 1 2 3    -> argc = 4, imprime 3
 *   ./paramsum          -> argc = 1, imprime 0
 */
int	main(int argc, char **argv)
{
	(void)argv;  /* Evita warning de variável não usada */
	
	/* Imprime o número de argumentos (excluindo o nome do programa) */
	ft_putnbr(argc - 1);
	ft_putchar('\n');
	
	return (0);
}
