/* ************************************************************************** */
/*                                                                            */
/*   flood_fill.c                                                             */
/*                                                                            */
/*   Descrição: Função que preenche uma zona de caracteres iguais com 'F'    */
/*   usando algoritmo de flood fill (preenchimento recursivo)                 */
/*                                                                            */
/* ************************************************************************** */

// Definição da estrutura t_point
typedef struct s_point
{
	int	x;
	int	y;
}	t_point;

/*
** Função auxiliar recursiva que realiza o flood fill
** Parâmetros:
**   - tab: array 2D de caracteres
**   - size: dimensões do array (largura e altura)
**   - cur: posição atual sendo processada
**   - target: caractere original que será substituído
*/
void	fill(char **tab, t_point size, t_point cur, char target)
{
	// Verifica se a posição atual está fora dos limites
	if (cur.x < 0 || cur.x >= size.x || cur.y < 0 || cur.y >= size.y)
		return;
	
	// Verifica se o caractere na posição atual é diferente do alvo
	// (já foi preenchido ou é um limite da zona)
	if (tab[cur.y][cur.x] != target)
		return;
	
	// Preenche a posição atual com 'F'
	tab[cur.y][cur.x] = 'F';
	
	// Chama recursivamente para as 4 direções (cima, baixo, esquerda, direita)
	// Não preenche diagonalmente
	
	// Direção: cima (y - 1)
	fill(tab, size, (t_point){cur.x, cur.y - 1}, target);
	
	// Direção: baixo (y + 1)
	fill(tab, size, (t_point){cur.x, cur.y + 1}, target);
	
	// Direção: esquerda (x - 1)
	fill(tab, size, (t_point){cur.x - 1, cur.y}, target);
	
	// Direção: direita (x + 1)
	fill(tab, size, (t_point){cur.x + 1, cur.y}, target);
}

/*
** Função principal flood_fill
** Inicia o processo de preenchimento a partir do ponto 'begin'
** Parâmetros:
**   - tab: array 2D de caracteres a ser preenchido
**   - size: dimensões do array
**   - begin: ponto inicial do preenchimento
*/
void	flood_fill(char **tab, t_point size, t_point begin)
{
	char	target;
	
	// Guarda o caractere original na posição inicial
	// Este é o caractere que será substituído em toda a zona
	target = tab[begin.y][begin.x];
	
	// Chama a função recursiva de preenchimento
	fill(tab, size, begin, target);
}
