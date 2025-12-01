/* ************************************************************************** */
/*                                                                            */
/*   ft_itoa.c                                                                */
/*                                                                            */
/*   Descrição: Converte um inteiro em uma string alocada dinamicamente      */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

/*
** Função auxiliar que calcula o número de dígitos necessários
** para representar o número (incluindo o sinal negativo se houver)
*/
int	get_num_len(int n)
{
	int	len;
	
	len = 0;
	
	// Se o número for 0, precisa de 1 dígito
	if (n == 0)
		return (1);
	
	// Se for negativo, adiciona 1 para o sinal '-'
	if (n < 0)
		len++;
	
	// Conta os dígitos
	while (n != 0)
	{
		n = n / 10;
		len++;
	}
	
	return (len);
}

/*
** Função principal ft_itoa
** Converte um inteiro em string
** Retorna: ponteiro para a string alocada ou NULL se falhar
*/
char	*ft_itoa(int nbr)
{
	char	*str;
	int		len;
	long	n;
	
	// Usa long para lidar com INT_MIN (-2147483648)
	n = nbr;
	
	// Calcula o tamanho necessário para a string
	len = get_num_len(n);
	
	// Aloca memória (len + 1 para o '\0')
	str = (char *)malloc(sizeof(char) * (len + 1));
	if (!str)
		return (NULL);
	
	// Adiciona o terminador nulo
	str[len] = '\0';
	
	// Caso especial: número 0
	if (n == 0)
	{
		str[0] = '0';
		return (str);
	}
	
	// Se o número for negativo, adiciona o sinal e trabalha com valor positivo
	if (n < 0)
	{
		str[0] = '-';
		n = -n;
	}
	
	// Preenche a string de trás para frente com os dígitos
	len--;  // Ajusta para o último índice válido
	while (n > 0)
	{
		str[len] = (n % 10) + '0';  // Converte dígito para caractere
		n = n / 10;
		len--;
	}
	
	return (str);
}
