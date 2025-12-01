/* ************************************************************************** */
/*                                                                            */
/*   camel_to_snake.c                                                         */
/*                                                                            */
/*   Converte lowerCamelCase para snake_case                                 */
/*   Exemplo: "hereIsACamelCase" -> "here_is_a_camel_case"                  */
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
		
		// Se encontrar uma letra maiúscula
		if (c >= 'A' && c <= 'Z')
		{
			// Adiciona underscore antes da letra maiúscula
			write(1, "_", 1);
			
			// Converte para minúscula
			c = c + 32;
		}
		
		write(1, &c, 1);
		i++;
	}
	
	write(1, "\n", 1);
	return (0);
}
