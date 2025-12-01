/* ************************************************************************** */
/*                                                                            */
/*   union.c                                                                  */
/*                                                                            */
/*   Exibe caracteres que aparecem em qualquer uma das strings (união)      */
/*   Sem duplicatas, na ordem que aparecem                                   */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char **argv)
{
	int		i;
	int		seen[256] = {0};  // Array para marcar caracteres já impressos

	// Se não houver exatamente 2 argumentos, imprime apenas newline
	if (argc != 3)
	{
		write(1, "\n", 1);
		return (0);
	}

	// Processa a primeira string
	i = 0;
	while (argv[1][i])
	{
		// Se o caractere ainda não foi impresso
		if (!seen[(unsigned char)argv[1][i]])
		{
			write(1, &argv[1][i], 1);
			seen[(unsigned char)argv[1][i]] = 1;
		}
		i++;
	}

	// Processa a segunda string
	i = 0;
	while (argv[2][i])
	{
		// Se o caractere ainda não foi impresso
		if (!seen[(unsigned char)argv[2][i]])
		{
			write(1, &argv[2][i], 1);
			seen[(unsigned char)argv[2][i]] = 1;
		}
		i++;
	}

	write(1, "\n", 1);
	return (0);
}
