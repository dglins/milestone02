/* ************************************************************************** */
/*                                                                            */
/*   inter.c                                                                  */
/*                                                                            */
/*   Exibe caracteres que aparecem em ambas as strings (interseção)         */
/*   Sem duplicatas, na ordem da primeira string                             */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char **argv)
{
	int		i;
	int		j;
	int		seen[256] = {0};  // Array para marcar caracteres já impressos

	// Se não houver exatamente 2 argumentos, imprime apenas newline
	if (argc != 3)
	{
		write(1, "\n", 1);
		return (0);
	}

	i = 0;
	while (argv[1][i])
	{
		// Se o caractere ainda não foi impresso
		if (!seen[(unsigned char)argv[1][i]])
		{
			j = 0;
			// Verifica se o caractere existe na segunda string
			while (argv[2][j])
			{
				if (argv[1][i] == argv[2][j])
				{
					// Imprime o caractere e marca como visto
					write(1, &argv[1][i], 1);
					seen[(unsigned char)argv[1][i]] = 1;
					break;
				}
				j++;
			}
		}
		i++;
	}

	write(1, "\n", 1);
	return (0);
}
