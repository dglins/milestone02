/* ************************************************************************** */
/*                                                                            */
/*   rot_13.c                                                                 */
/*                                                                            */
/*   Descrição: Programa que aplica cifra ROT13 - rotaciona cada letra       */
/*              13 posições no alfabeto (a->n, b->o, ..., z->m)              */
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
				// Rotaciona 13 posições
				// Se passar de 'z', volta para o início do alfabeto
				c = c + 13;
				if (c > 'z')
					c = c - 26;
			}
			// Para letras maiúsculas (A-Z)
			else if (c >= 'A' && c <= 'Z')
			{
				// Rotaciona 13 posições
				// Se passar de 'Z', volta para o início do alfabeto
				c = c + 13;
				if (c > 'Z')
					c = c - 26;
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
