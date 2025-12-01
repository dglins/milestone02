/* ************************************************************************** */
/*                                                                            */
/*   snake_to_camel.c                                                         */
/*                                                                            */
/*   Converte snake_case para lowerCamelCase                                 */
/*   Exemplo: "here_is_a_snake_case" -> "hereIsASnakeCase"                  */
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
		
		// Se encontrar um underscore
		if (c == '_')
		{
			// Pula o underscore
			i++;
			
			// Se o próximo caractere for uma letra minúscula, converte para maiúscula
			if (argv[1][i] >= 'a' && argv[1][i] <= 'z')
			{
				c = argv[1][i] - 32;
				write(1, &c, 1);
			}
		}
		else
		{
			write(1, &c, 1);
		}
		
		i++;
	}
	
	write(1, "\n", 1);
	return (0);
}
