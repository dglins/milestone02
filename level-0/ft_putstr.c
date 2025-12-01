/* ************************************************************************** */
/*                                                                            */
/*   ft_putstr.c                                                              */
/*                                                                            */
/*   Descrição: Função que imprime uma string na saída padrão                */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/*
** Função que imprime uma string caractere por caractere
** 
** Parâmetros:
**   str - ponteiro para a string a ser impressa
**
** Funcionamento:
**   1. Percorre a string até encontrar o caractere nulo '\0'
**   2. Para cada caractere, usa write() para imprimir na saída padrão
*/
void	ft_putstr(char *str)
{
	int	i;

	i = 0;
	// Percorre a string até o final (caractere nulo)
	while (str[i] != '\0')
	{
		// Escreve um caractere por vez na saída padrão
		write(1, &str[i], 1);
		i++;
	}
}
