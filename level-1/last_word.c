/* ************************************************************************** */
/*                                                                            */
/*   last_word.c                                                              */
/*                                                                            */
/*   Exibe a última palavra de uma string                                    */
/*   Palavra = sequência de caracteres delimitada por espaços/tabs          */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;
	int	start;
	int	end;

	// Se não houver exatamente 1 argumento, imprime apenas newline
	if (argc != 2)
	{
		write(1, "\n", 1);
		return (0);
	}

	// Encontra o final da string
	i = 0;
	while (argv[1][i])
		i++;
	i--;

	// Pula espaços e tabs no final
	while (i >= 0 && (argv[1][i] == ' ' || argv[1][i] == '\t'))
		i--;

	end = i;

	// Encontra o início da última palavra
	while (i >= 0 && argv[1][i] != ' ' && argv[1][i] != '\t')
		i--;

	start = i + 1;

	// Imprime a última palavra
	while (start <= end)
	{
		write(1, &argv[1][start], 1);
		start++;
	}

	write(1, "\n", 1);
	return (0);
}
