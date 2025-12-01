/* ************************************************************************** */
/*                                                                            */
/*   ft_range.c                                                               */
/*                                                                            */
/*   Descrição: Cria um array dinâmico com valores consecutivos de start     */
/*              até end (inclusive).                                          */
/*                                                                            */
/*   Conceitos: Alocação dinâmica, arrays, valores crescentes/decrescentes   */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

/* Calcula o valor absoluto de um número */
int	ft_abs(int n)
{
	if (n < 0)
		return (-n);
	return (n);
}

/* Cria um array com valores consecutivos de start até end
 * 
 * Algoritmo:
 * 1. Calcula o tamanho do array: |end - start| + 1
 * 2. Aloca memória para o array
 * 3. Preenche com valores consecutivos:
 *    - Se start < end: valores crescentes
 *    - Se start > end: valores decrescentes
 *    - Se start == end: array com um único elemento
 * 
 * Exemplos:
 *   ft_range(1, 3)   -> [1, 2, 3]
 *   ft_range(-1, 2)  -> [-1, 0, 1, 2]
 *   ft_range(0, -3)  -> [0, -1, -2, -3]
 *   ft_range(0, 0)   -> [0]
 */
int	*ft_range(int start, int end)
{
	int	*array;
	int	size;
	int	i;

	/* Calcula o tamanho do array (incluindo start e end) */
	size = ft_abs(end - start) + 1;
	
	/* Aloca memória para o array */
	array = (int *)malloc(sizeof(int) * size);
	if (!array)
		return (NULL);
	
	/* Preenche o array com valores consecutivos */
	i = 0;
	while (i < size)
	{
		/* Se start < end, incrementa; se start > end, decrementa */
		if (start < end)
			array[i] = start + i;
		else
			array[i] = start - i;
		i++;
	}
	
	return (array);
}
