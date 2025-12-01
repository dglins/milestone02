/* ************************************************************************** */
/*                                                                            */
/*   search_and_replace.c                                                     */
/*                                                                            */
/*   Descrição: Programa que busca e substitui um caractere por outro        */
/*              em uma string                                                 */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/*
** Função auxiliar para calcular o comprimento de uma string
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
	int	i;

	// Verifica se há exatamente 3 argumentos
	// E se o 2º e 3º argumentos têm exatamente 1 caractere cada
	if (argc == 4 && ft_strlen(argv[2]) == 1 && ft_strlen(argv[3]) == 1)
	{
		i = 0;
		while (argv[1][i] != '\0')
		{
			// Se o caractere atual for igual ao caractere a ser substituído
			if (argv[1][i] == argv[2][0])
			{
				// Escreve o caractere de substituição
				write(1, &argv[3][0], 1);
			}
			else
			{
				// Caso contrário, escreve o caractere original
				write(1, &argv[1][i], 1);
			}
			i++;
		}
	}
	
	// Sempre imprime newline no final
	write(1, "\n", 1);
	return (0);
}
