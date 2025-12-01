/* ************************************************************************** */
/*                                                                            */
/*   repeat_alpha.c                                                           */
/*                                                                            */
/*   Descrição: Programa que repete cada letra alfabética de acordo com      */
/*              sua posição no alfabeto (a=1x, b=2x, c=3x, etc.)             */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/*
** Função que calcula quantas vezes uma letra deve ser repetida
** baseado em sua posição no alfabeto
**
** Retorno:
**   Para 'a' ou 'A': 1
**   Para 'b' ou 'B': 2
**   Para 'z' ou 'Z': 26
*/
int	get_repeat_count(char c)
{
	// Se for minúscula, retorna posição no alfabeto (a=1, b=2, etc.)
	if (c >= 'a' && c <= 'z')
		return (c - 'a' + 1);
	
	// Se for maiúscula, retorna posição no alfabeto (A=1, B=2, etc.)
	if (c >= 'A' && c <= 'Z')
		return (c - 'A' + 1);
	
	// Se não for letra, repete apenas 1 vez
	return (1);
}

int	main(int argc, char **argv)
{
	int	i;
	int	repeat;
	int	j;

	// Verifica se há exatamente 1 argumento
	if (argc == 2)
	{
		i = 0;
		while (argv[1][i] != '\0')
		{
			// Calcula quantas vezes o caractere deve ser repetido
			repeat = get_repeat_count(argv[1][i]);
			
			// Imprime o caractere 'repeat' vezes
			j = 0;
			while (j < repeat)
			{
				write(1, &argv[1][i], 1);
				j++;
			}
			i++;
		}
	}
	
	// Sempre imprime newline no final
	write(1, "\n", 1);
	return (0);
}
