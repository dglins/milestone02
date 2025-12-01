/* ************************************************************************** */
/*                                                                            */
/*   str_capitalizer.c                                                        */
/*                                                                            */
/*   Descrição: Capitaliza a primeira letra de cada palavra e coloca o       */
/*              resto em minúsculas.                                          */
/*                                                                            */
/*   Conceitos: Manipulação de case, detecção de início de palavra           */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/* Verifica se um caractere é espaço ou tab */
int	is_space(char c)
{
	return (c == ' ' || c == '\t');
}

/* Verifica se um caractere é uma letra */
int	is_alpha(char c)
{
	return ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'));
}

/* Converte para maiúscula se for letra minúscula */
char	to_upper(char c)
{
	if (c >= 'a' && c <= 'z')
		return (c - 32);
	return (c);
}

/* Converte para minúscula se for letra maiúscula */
char	to_lower(char c)
{
	if (c >= 'A' && c <= 'Z')
		return (c + 32);
	return (c);
}

/* Capitaliza primeira letra de cada palavra
 * 
 * Algoritmo:
 * 1. Marca início de palavra após espaços/tabs ou no início
 * 2. Se é início de palavra e é letra, capitaliza
 * 3. Caso contrário, coloca em minúscula
 */
void	str_capitalizer(char *str)
{
	int		i;
	int		new_word;
	char	c;

	i = 0;
	new_word = 1;

	while (str[i])
	{
		/* Se é início de palavra e é letra, capitaliza */
		if (new_word && is_alpha(str[i]))
		{
			c = to_upper(str[i]);
			new_word = 0;
		}
		/* Se não é início de palavra e é letra, minúscula */
		else if (is_alpha(str[i]))
		{
			c = to_lower(str[i]);
		}
		/* Se não é letra, mantém o caractere */
		else
		{
			c = str[i];
		}
		
		/* Marca início de nova palavra após espaço/tab */
		if (is_space(str[i]))
			new_word = 1;
		
		write(1, &c, 1);
		i++;
	}
}

int	main(int argc, char **argv)
{
	int	i;

	/* Se não há argumentos, imprime apenas newline */
	if (argc < 2)
	{
		write(1, "\n", 1);
		return (0);
	}

	/* Processa cada argumento */
	i = 1;
	while (i < argc)
	{
		str_capitalizer(argv[i]);
		write(1, "\n", 1);
		i++;
	}
	
	return (0);
}
