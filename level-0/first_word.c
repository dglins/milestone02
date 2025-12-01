/* ************************************************************************** */
/*                                                                            */
/*   first_word.c                                                             */
/*                                                                            */
/*   Descrição: Programa que imprime a primeira palavra de uma string        */
/*              Uma palavra é delimitada por espaços/tabs ou início/fim       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;

	// Verifica se há exatamente 1 argumento (além do nome do programa)
	if (argc == 2)
	{
		i = 0;
		
		// Pula espaços e tabs no início da string
		while (argv[1][i] == ' ' || argv[1][i] == '\t')
			i++;
		
		// Imprime caracteres até encontrar espaço, tab ou fim da string
		while (argv[1][i] != '\0' && argv[1][i] != ' ' && argv[1][i] != '\t')
		{
			write(1, &argv[1][i], 1);
			i++;
		}
	}
	
	// Sempre imprime newline no final (mesmo se não houver palavra)
	write(1, "\n", 1);
	return (0);
}
