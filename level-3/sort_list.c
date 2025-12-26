/* ************************************************************************** */
/*                                                                            */
/*   sort_list.c                                                              */
/*                                                                            */
/*   Descrição: Função que ordena uma lista encadeada usando uma função      */
/*   de comparação fornecida como parâmetro                                   */
/*                                                                            */
/* ************************************************************************** */

#include "list.h"

t_list	*sort_list(t_list* lst, int (*cmp)(int, int))
{
	int	temp;
	t_list *head;

	head = lst;
	while (lst && lst->next)
	{
		if (cmp(lst->data, lst->next->data) == 0)
		{
			temp = lst->data;
			lst->data = lst->next->data;
			lst->next->data = temp;
			lst = head;
		}
		else

			lst = lst->next;
	}
	return (head);
}
