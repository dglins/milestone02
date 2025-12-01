/* ************************************************************************** */
/*                                                                            */
/*   ulstr.c                                                                  */
/*                                                                            */
/*   Descrição: Programa que inverte maiúsculas/minúsculas de uma string     */
/*              Maiúsculas viram minúsculas e vice-versa                     */
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
			
			// Se for letra minúscula (a-z), converte para maiúscula
			// Subtrai 32 na tabela ASCII para converter minúscula em maiúscula
			if (c >= 'a' && c <= 'z')
				c = c - 32;
			
			// Se for letra maiúscula (A-Z), converte para minúscula
			// Adiciona 32 na tabela ASCII para converter maiúscula em minúscula
			else if (c >= 'A' && c <= 'Z')
				c = c + 32;
			
			// Outros caracteres permanecem inalterados
			write(1, &c, 1);
			i++;
		}
	}
	
	// Sempre imprime newline no final
	write(1, "\n", 1);
	return (0);
}
