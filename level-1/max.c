/* ************************************************************************** */
/*                                                                            */
/*   max.c                                                                    */
/*                                                                            */
/*   Encontra o maior número em um array de inteiros                         */
/*   Retorna 0 se o array estiver vazio                                      */
/*                                                                            */
/* ************************************************************************** */

int	max(int *tab, unsigned int len)
{
	unsigned int	i;
	int				max_value;

	// Se o array estiver vazio, retorna 0
	if (len == 0)
		return (0);

	// Inicializa max_value com o primeiro elemento
	max_value = tab[0];
	
	// Percorre o array procurando o maior valor
	i = 1;
	while (i < len)
	{
		if (tab[i] > max_value)
			max_value = tab[i];
		i++;
	}

	return (max_value);
}
