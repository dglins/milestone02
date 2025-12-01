/* ************************************************************************** */
/*                                                                            */
/*   ft_list_size.c                                                           */
/*                                                                            */
/*   Descrição: Conta o número de elementos em uma lista encadeada           */
/*                                                                            */
/*   Conceitos: Listas encadeadas, traversal, contagem de nós                */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

/* Definição da estrutura de lista encadeada */
typedef struct s_list
{
	struct s_list	*next;
	void			*data;
}	t_list;

/* Conta o número de elementos em uma lista encadeada
 * 
 * Algoritmo (traversal):
 * 1. Começa com contador = 0
 * 2. Percorre a lista seguindo os ponteiros next
 * 3. Para cada nó, incrementa o contador
 * 4. Para quando next é NULL (fim da lista)
 * 
 * Complexidade: O(n) onde n é o número de elementos
 * 
 * Exemplo:
 *   Lista: [A] -> [B] -> [C] -> NULL
 *   Retorna: 3
 * 
 *   Lista vazia: NULL
 *   Retorna: 0
 */
int	ft_list_size(t_list *begin_list)
{
	int	count;

	count = 0;
	
	/* Percorre a lista até o final */
	while (begin_list)
	{
		count++;
		begin_list = begin_list->next;
	}
	
	return (count);
}
