/* ************************************************************************** */
/*                                                                            */
/*   rstr_capitalizer.c                                                       */
/*                                                                            */
/*   Descrição: Capitaliza a ÚLTIMA letra de cada palavra e coloca o resto   */
/*              em minúsculas.                                                */
/*                                                                            */
/*   Conceitos: Lookahead, detecção de fim de palavra                        */
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

/* Verifica se é a última letra da palavra
 * Olha à frente para ver se o próximo caractere é espaço/tab/fim
 */
int	is_last_letter(char *str, int i)
{
	int	j;

	j = i + 1;
	/* Pula caracteres não-letra até encontrar espaço/fim ou outra letra */
	while (str[j] && !is_space(str[j]) && !is_alpha(str[j]))
		j++;
	
	/* Se encontrou espaço ou fim, esta é a última letra */
	return (!str[j] || is_space(str[j]));
}

/* Capitaliza última letra de cada palavra
 * 
 * Algoritmo:
 * 1. Para cada caractere:
 *    - Se é letra e é a última da palavra, capitaliza
 *    - Se é letra mas não é a última, minúscula
 *    - Caso contrário, mantém o caractere
 */
void	rstr_capitalizer(char *str)
{
	int		i;
	char	c;

	i = 0;
	while (str[i])
	{
		/* Se é letra, verifica se é a última da palavra */
		if (is_alpha(str[i]))
		{
			if (is_last_letter(str, i))
				c = to_upper(str[i]);
			else
				c = to_lower(str[i]);
		}
		else
		{
			c = str[i];
		}
		
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
		rstr_capitalizer(argv[i]);
		write(1, "\n", 1);
		i++;
	}
	
	return (0);
}
