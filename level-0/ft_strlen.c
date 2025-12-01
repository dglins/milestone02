/* ************************************************************************** */
/*                                                                            */
/*   ft_strlen.c                                                              */
/*                                                                            */
/*   Descrição: Função que retorna o comprimento de uma string               */
/*                                                                            */
/* ************************************************************************** */

/*
** Função que calcula o tamanho de uma string
**
** Parâmetros:
**   str - ponteiro para a string
**
** Retorno:
**   Número de caracteres na string (sem contar o '\0')
**
** Funcionamento:
**   Percorre a string contando caracteres até encontrar '\0'
*/
int	ft_strlen(char *str)
{
	int	len;

	len = 0;
	// Conta cada caractere até encontrar o terminador nulo
	while (str[len] != '\0')
		len++;
	
	return (len);
}
