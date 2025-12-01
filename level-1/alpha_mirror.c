/* ************************************************************************** */
/*                                                                            */
/*   alpha_mirror.c                                                           */
/*                                                                            */
/*   Espelha caracteres alfabéticos (a->z, b->y, c->x, etc.)                */
/*   Mantém maiúsculas/minúsculas e caracteres não alfabéticos              */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int argc, char **argv)
{
	int		i;
	char	c;

	// Se não houver exatamente 1 argumento, imprime apenas newline
	if (argc != 2)
	{
		write(1, "\n", 1);
		return (0);
	}

	i = 0;
	while (argv[1][i])
	{
		c = argv[1][i];
		
		// Se for letra minúscula, espelha: a(0) -> z(25), b(1) -> y(24), etc.
		// Fórmula: 'z' - (c - 'a') = 'z' + 'a' - c
		if (c >= 'a' && c <= 'z')
			c = 'z' + 'a' - c;
		
		// Se for letra maiúscula, espelha: A(0) -> Z(25), B(1) -> Y(24), etc.
		else if (c >= 'A' && c <= 'Z')
			c = 'Z' + 'A' - c;
		
		// Caracteres não alfabéticos permanecem inalterados
		
		write(1, &c, 1);
		i++;
	}
	
	write(1, "\n", 1);
	return (0);
}
