/* ************************************************************************** */
/*                                                                            */
/*   ft_swap.c                                                                */
/*                                                                            */
/*   Descrição: Função que troca os valores de dois inteiros                 */
/*                                                                            */
/* ************************************************************************** */

/*
** Função que troca o conteúdo de dois inteiros
**
** Parâmetros:
**   a - ponteiro para o primeiro inteiro
**   b - ponteiro para o segundo inteiro
**
** Funcionamento:
**   Usa uma variável temporária para guardar um valor durante a troca
**   1. Guarda o valor de *a em temp
**   2. Copia o valor de *b para *a
**   3. Copia o valor de temp (antigo *a) para *b
*/
void	ft_swap(int *a, int *b)
{
	int	temp;

	// Guarda o valor apontado por 'a' temporariamente
	temp = *a;
	
	// Copia o valor de 'b' para 'a'
	*a = *b;
	
	// Copia o valor temporário (antigo 'a') para 'b'
	*b = temp;
}
