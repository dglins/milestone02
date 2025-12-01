/* ************************************************************************** */
/*                                                                            */
/*   rotone.c                                                                 */
/*                                                                            */
/*   Descrição: Programa que rotaciona cada letra 1 posição no alfabeto      */
/*              (a->b, b->c, ..., z->a)                                      */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char **argv)
{
	int		i;
	char	c;

	// Verifica se há exatamente 1 argumento
	if (argc == 2)
	{
		i = 0;
		while (argv[1][i] != '\0')
		{
			c = argv[1][i];
			
			// Para letras minúsculas (a-z)
			if (c >= 'a' && c <= 'z')
			{
				// Se for 'z', volta para 'a'
				if (c == 'z')
					c = 'a';
				// Caso contrário, avança 1 letra
				else
					c = c + 1;
			}
			// Para letras maiúsculas (A-Z)
			else if (c >= 'A' && c <= 'Z')
			{
				// Se for 'Z', volta para 'A'
				if (c == 'Z')
					c = 'A';
				// Caso contrário, avança 1 letra
				else
					c = c + 1;
			}
			// Outros caracteres permanecem inalterados
			
			write(1, &c, 1);
			i++;
		}
	}
	
	// Sempre imprime newline no final
	write(1, "\n", 1);
	return (0);
}
