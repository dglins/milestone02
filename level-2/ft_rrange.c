/* ************************************************************************** */
/*                                                                            */
/*   ft_rrange.c                                                              */
/*                                                                            */
/*   Descrição: Cria um array dinâmico com valores consecutivos de end       */
/*              até start (ordem reversa de ft_range).                        */
/*                                                                            */
/*   Conceitos: Alocação dinâmica, arrays, ordem reversa                     */
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

/* Cria um array com valores consecutivos de end até start (ordem reversa)
 * 
 * Similar ao ft_range, mas começa do end e vai até start
 * 
 * Algoritmo:
 * 1. Calcula o tamanho do array: |end - start| + 1
 * 2. Aloca memória para o array
 * 3. Preenche com valores consecutivos começando do end:
 *    - Se start < end: valores decrescentes (de end até start)
 *    - Se start > end: valores crescentes (de end até start)
 *    - Se start == end: array com um único elemento
 * 
 * Exemplos:
 *   ft_rrange(1, 3)   -> [3, 2, 1]
 *   ft_rrange(-1, 2)  -> [2, 1, 0, -1]
 *   ft_rrange(0, -3)  -> [-3, -2, -1, 0]
 *   ft_rrange(0, 0)   -> [0]
 */
int	*ft_rrange(int start, int end)
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
	
	/* Preenche o array com valores consecutivos começando do end */
	i = 0;
	while (i < size)
	{
		/* Se start < end, decrementa do end; se start > end, incrementa do end */
		if (start < end)
			array[i] = end - i;
		else
			array[i] = end + i;
		i++;
	}
	
	return (array);
}
