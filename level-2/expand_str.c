/* ************************************************************************** */
/*                                                                            */
/*   expand_str.c                                                             */
/*                                                                            */
/*   Descrição: Coloca exatamente 3 espaços entre palavras, sem espaços      */
/*              no início ou fim.                                             */
/*                                                                            */
/*   Conceitos: Parsing de strings, separadores customizados                 */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/* Verifica se um caractere é espaço ou tab */
int	is_space(char c)
{
	return (c == ' ' || c == '\t');
}

/* Expande espaços entre palavras para exatamente 3 espaços
 * 
 * Similar ao epur_str, mas coloca 3 espaços entre palavras
 */
void	expand_str(char *str)
{
	int	i;
	int	first_word;

	i = 0;
	first_word = 1;

	/* Pula espaços iniciais */
	while (is_space(str[i]))
		i++;

	while (str[i])
	{
		/* Se não é a primeira palavra, adiciona 3 espaços separadores */
		if (!first_word && !is_space(str[i]))
			write(1, "   ", 3);
		
		/* Imprime todos os caracteres da palavra atual */
		while (str[i] && !is_space(str[i]))
		{
			write(1, &str[i], 1);
			i++;
		}
		
		/* Marca que já processamos pelo menos uma palavra */
		if (str[i] || !first_word)
			first_word = 0;
		
		/* Pula espaços entre palavras */
		while (is_space(str[i]))
			i++;
	}
}

int	main(int argc, char **argv)
{
	/* Verifica se há exatamente 1 argumento */
	if (argc == 2)
		expand_str(argv[1]);
	
	/* Sempre imprime newline */
	write(1, "\n", 1);
	return (0);
}
