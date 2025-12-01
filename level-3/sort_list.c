/* ************************************************************************** */
/*                                                                            */
/*   sort_list.c                                                              */
/*                                                                            */
/*   Descrição: Função que ordena uma lista encadeada usando uma função      */
/*   de comparação fornecida como parâmetro                                   */
/*                                                                            */
/* ************************************************************************** */

#include "list.h"

/*
** Função sort_list
** Ordena uma lista encadeada usando bubble sort
** Parâmetros:
**   - lst: ponteiro para o início da lista
**   - cmp: função de comparação que retorna != 0 se a <= b (ordem correta)
** Retorna: ponteiro para o início da lista ordenada
*/
t_list	*sort_list(t_list *lst, int (*cmp)(int, int))
{
	t_list	*current;
	int		temp;
	int		swapped;
	
	// Se a lista está vazia ou tem apenas um elemento, já está ordenada
	if (!lst || !lst->next)
		return (lst);
	
	// Bubble sort: continua até não haver mais trocas
	swapped = 1;
	while (swapped)
	{
		swapped = 0;
		current = lst;
		
		// Percorre a lista comparando elementos adjacentes
		while (current->next)
		{
			// Se os elementos estão na ordem errada (cmp retorna 0)
			// troca os valores
			if (cmp(current->data, current->next->data) == 0)
			{
				// Troca os valores (não os nós)
				temp = current->data;
				current->data = current->next->data;
				current->next->data = temp;
				
				// Marca que houve uma troca
				swapped = 1;
			}
			
			// Avança para o próximo par
			current = current->next;
		}
	}
	
	return (lst);
}
