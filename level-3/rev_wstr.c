/* ************************************************************************** */
/*                                                                            */
/*   rev_wstr.c                                                               */
/*                                                                            */
/*   Descrição: Programa que imprime as palavras de uma string em ordem      */
/*   reversa                                                                  */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char **argv)
{
	int i;
	int end;

	if (argc != 2)
	{
		write(1, "\n", 1);
		return (0);
	}

	i = 0;
	while (argv[1][i])
		i++;
	end = i;

	while (i >= 0)
	{
		if (i == 0 || argv[1][i - 1] == ' ')
		{
			write(1, &argv[1][i], end - i);
			if (i > 0)
				write(1, " ", 1);
			end = i - 1;
		}
		i--;
	}
	write(1, "\n", 1);
	return (0);
}

