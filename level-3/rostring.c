/* ************************************************************************** */
/*                                                                            */
/*   rostring.c                                                               */
/*                                                                            */
/*   Descrição: Programa que rotaciona uma string movendo a primeira         */
/*   palavra para o final                                                     */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/*
** Função auxiliar que verifica se um caractere é espaço em branco
*/
int	is_space(char c)
{
	return (c == ' ' || c == '\t');
}

/*
** Função auxiliar que imprime uma palavra
** Retorna o índice após a palavra (pulando espaços)
*/
int	print_word(char *str, int i)
{
	int	start;
	
	start = i;
	
	// Encontra o fim da palavra
	while (str[i] && !is_space(str[i]))
		i++;
	
	// Imprime a palavra
	write(1, &str[start], i - start);
	
	return (i);
}

/*
** Função principal
** Rotaciona a string movendo a primeira palavra para o final
*/
int	main(int argc, char **argv)
{
	char	*str;
	int		i;
	int		first_word_start;
	int		first_word_end;
	
	// Verifica se há exatamente 1 argumento
	if (argc < 2)
	{
		write(1, "\n", 1);
		return (0);
	}
	
	str = argv[1];
	i = 0;
	
	// Pula espaços iniciais
	while (str[i] && is_space(str[i]))
		i++;
	
	// Guarda o início da primeira palavra
	first_word_start = i;
	
	// Encontra o fim da primeira palavra
	while (str[i] && !is_space(str[i]))
		i++;
	
	first_word_end = i;
	
	// Pula espaços após a primeira palavra
	while (str[i] && is_space(str[i]))
		i++;
	
	// Imprime todas as palavras exceto a primeira
	while (str[i])
	{
		// Pula espaços
		while (str[i] && is_space(str[i]))
			i++;
		
		// Se encontrou uma palavra
		if (str[i])
		{
			// Imprime a palavra
			i = print_word(str, i);
			
			// Pula espaços após a palavra
			while (str[i] && is_space(str[i]))
				i++;
			
			// Se ainda há mais palavras ou se vamos imprimir a primeira palavra
			// adiciona um espaço
			if (str[i] || first_word_start < first_word_end)
				write(1, " ", 1);
		}
	}
	
	// Imprime a primeira palavra no final (se ela existir)
	if (first_word_start < first_word_end)
	{
		write(1, &str[first_word_start], first_word_end - first_word_start);
	}
	
	write(1, "\n", 1);
	return (0);
}
