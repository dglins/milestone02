/* ************************************************************************** */
/*                                                                            */
/*   rev_print.c                                                              */
/*                                                                            */
/*   Descrição: Programa que imprime uma string em ordem reversa             */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/*
** Função auxiliar que calcula o comprimento de uma string
*/
int	ft_strlen(char *str)
{
	int	len;

	len = 0;
	while (str[len] != '\0')
		len++;
	return (len);
}

int	main(int argc, char **argv)
{
	int	len;

	// Verifica se há exatamente 1 argumento
	if (argc == 2)
	{
		// Calcula o comprimento da string
		len = ft_strlen(argv[1]);
		
		// Imprime a string de trás para frente
		// Começa no último caractere (len - 1) e vai até o primeiro (0)
		while (len > 0)
		{
			len--;
			write(1, &argv[1][len], 1);
		}
	}
	
	// Sempre imprime newline no final
	write(1, "\n", 1);
	return (0);
}
