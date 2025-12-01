/* ************************************************************************** */
/*                                                                            */
/*   ft_strdup.c                                                              */
/*                                                                            */
/*   Duplica uma string alocando memória dinamicamente                       */
/*   Retorna um ponteiro para a nova string ou NULL se falhar                */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

char	*ft_strdup(char *src)
{
	char	*dup;
	int		len;
	int		i;

	// Calcula o tamanho da string
	len = 0;
	while (src[len])
		len++;

	// Aloca memória para a nova string (tamanho + 1 para o '\0')
	dup = (char *)malloc(sizeof(char) * (len + 1));
	
	// Se a alocação falhar, retorna NULL
	if (!dup)
		return (NULL);

	// Copia os caracteres da string original
	i = 0;
	while (src[i])
	{
		dup[i] = src[i];
		i++;
	}
	
	// Adiciona o terminador nulo
	dup[i] = '\0';

	return (dup);
}
