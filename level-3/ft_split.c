/* ************************************************************************** */
/*                                                                            */
/*   ft_split.c                                                               */
/*                                                                            */
/*   Descrição: Divide uma string em palavras e retorna array de strings     */
/*   terminado em NULL                                                        */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

/*
** Função auxiliar que verifica se um caractere é espaço em branco
** (espaço, tab ou newline)
*/
int	is_space(char c)
{
	return (c == ' ' || c == '\t' || c == '\n');
}

/*
** Função auxiliar que conta o número de palavras na string
*/
int	count_words(char *str)
{
	int	count;
	int	in_word;
	
	count = 0;
	in_word = 0;
	
	while (*str)
	{
		// Se não é espaço e não estamos em uma palavra, inicia nova palavra
		if (!is_space(*str) && !in_word)
		{
			in_word = 1;
			count++;
		}
		// Se é espaço, marca que não estamos em palavra
		else if (is_space(*str))
		{
			in_word = 0;
		}
		str++;
	}
	
	return (count);
}

/*
** Função auxiliar que calcula o tamanho de uma palavra
** (até encontrar espaço ou fim da string)
*/
int	word_len(char *str)
{
	int	len;
	
	len = 0;
	while (str[len] && !is_space(str[len]))
		len++;
	
	return (len);
}

/*
** Função auxiliar que aloca e copia uma palavra
*/
char	*copy_word(char *str, int len)
{
	char	*word;
	int		i;
	
	word = (char *)malloc(sizeof(char) * (len + 1));
	if (!word)
		return (NULL);
	
	i = 0;
	while (i < len)
	{
		word[i] = str[i];
		i++;
	}
	word[i] = '\0';
	
	return (word);
}

/*
** Função principal ft_split
** Divide a string em palavras e retorna array de strings
** Retorna: array de strings terminado em NULL
*/
char	**ft_split(char *str)
{
	char	**result;
	int		words;
	int		i;
	int		len;
	
	// Conta o número de palavras
	words = count_words(str);
	
	// Aloca array de ponteiros (words + 1 para o NULL final)
	result = (char **)malloc(sizeof(char *) * (words + 1));
	if (!result)
		return (NULL);
	
	i = 0;
	// Processa cada palavra
	while (*str)
	{
		// Pula espaços em branco
		while (*str && is_space(*str))
			str++;
		
		// Se encontrou uma palavra
		if (*str)
		{
			// Calcula tamanho da palavra
			len = word_len(str);
			
			// Copia a palavra
			result[i] = copy_word(str, len);
			if (!result[i])
				return (NULL);  // Em caso de erro, deveria liberar memória
			
			// Avança para próxima palavra
			str += len;
			i++;
		}
	}
	
	// Adiciona NULL no final do array
	result[i] = NULL;
	
	return (result);
}
