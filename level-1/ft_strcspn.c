/* ************************************************************************** */
/*                                                                            */
/*   ft_strcspn.c                                                             */
/*                                                                            */
/*   Calcula o comprimento do segmento inicial de s que não contém          */
/*   nenhum dos caracteres em reject                                         */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

size_t	ft_strcspn(const char *s, const char *reject)
{
	size_t	i;
	size_t	j;

	i = 0;
	
	// Percorre a string s
	while (s[i])
	{
		j = 0;
		// Para cada caractere de s, verifica se está em reject
		while (reject[j])
		{
			// Se encontrar um caractere de reject em s, retorna o índice
			if (s[i] == reject[j])
				return (i);
			j++;
		}
		i++;
	}
	
	// Se não encontrou nenhum caractere de reject, retorna o tamanho de s
	return (i);
}
