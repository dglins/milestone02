/* ************************************************************************** */
/*                                                                            */
/*   ft_strcmp.c                                                              */
/*                                                                            */
/*   Compara duas strings lexicograficamente                                 */
/*   Retorna: 0 se iguais, <0 se s1 < s2, >0 se s1 > s2                     */
/*                                                                            */
/* ************************************************************************** */

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	
	// Percorre as strings enquanto os caracteres forem iguais
	// e não chegarmos ao final de nenhuma delas
	while (s1[i] && s2[i] && s1[i] == s2[i])
		i++;
	
	// Retorna a diferença entre os caracteres
	// Se forem iguais até o fim, retorna 0
	// Caso contrário, retorna a diferença do primeiro caractere diferente
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}
