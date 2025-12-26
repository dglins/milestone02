/* ************************************************************************** */
/*                                                                            */
/*   rev_wstr.c                                                               */
/*                                                                            */
/*   Descrição: Programa que imprime as palavras de uma string em ordem      */
/*   reversa                                                                  */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/*
** Função principal
** Imprime as palavras da string em ordem reversa
*/
int	main(int argc, char **argv)
{
	char	*str;
	int		i;
	int		start;
	int		end;
	
	// Verifica se há exatamente 1 argumento
	if (argc != 2)
	{
		write(1, "\n", 1);
		return (0);
	}
	
	str = argv[1];
	
	// Encontra o final da string
	i = 0;
	while (str[i])
		i++;
	
	// Processa a string de trás para frente
	while (i >= 0)
	{
		// Pula espaços e tabs no final
		while (i >= 0 && (str[i] == ' ' || str[i] == '\t' || str[i] == '\0'))
			i--;
		
		// Marca o fim da palavra
		end = i;
		
		// Encontra o início da palavra
		while (i >= 0 && str[i] != ' ' && str[i] != '\t')
			i--;
		
		// Marca o início da palavra
		start = i + 1;
		
		// Se encontrou uma palavra válida, imprime
		if (start <= end)
		{
			// Imprime a palavra caractere por caractere
			int j = start;
			while (j <= end)
			{
				write(1, &str[j], 1);
				j++;
			}
			
			// Se não é a última palavra (ainda há mais caracteres antes)
			// imprime um espaço
			if (i > 0)
				write(1, " ", 1);
		}
	}
	
	write(1, "\n", 1);
	return (0);
}
