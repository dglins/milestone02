/* ************************************************************************** */
/*                                                                            */
/*   ft_strcpy.c                                                              */
/*                                                                            */
/*   Descrição: Reproduz o comportamento da função strcpy                    */
/*              Copia a string s2 para s1, incluindo o '\0' final            */
/*                                                                            */
/* ************************************************************************** */

/*
** Função que copia uma string de origem para destino
**
** Parâmetros:
**   s1 - ponteiro para string de destino (deve ter espaço suficiente)
**   s2 - ponteiro para string de origem
**
** Retorno:
**   Retorna o ponteiro para a string de destino (s1)
**
** Funcionamento:
**   1. Percorre s2 copiando cada caractere para s1
**   2. Copia também o caractere nulo '\0' que marca o fim da string
**   3. Retorna o ponteiro original de s1
*/
char	*ft_strcpy(char *s1, char *s2)
{
	int	i;

	i = 0;
	// Copia cada caractere de s2 para s1, incluindo o '\0'
	while (s2[i] != '\0')
	{
		s1[i] = s2[i];
		i++;
	}
	// Adiciona o terminador nulo no final
	s1[i] = '\0';
	
	// Retorna o ponteiro para o início da string de destino
	return (s1);
}
