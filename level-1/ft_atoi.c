/* ************************************************************************** */
/*                                                                            */
/*   ft_atoi.c                                                                */
/*                                                                            */
/*   Converte uma string para um inteiro (int)                               */
/*   Funciona como a função padrão atoi()                                    */
/*                                                                            */
/* ************************************************************************** */

int	ft_atoi(const char *str)
{
	int	result;
	int	sign;

	result = 0;
	sign = 1;
	
	// Pula espaços em branco (espaço, tab, newline, etc.)
	while (*str == ' ' || (*str >= 9 && *str <= 13))
		str++;
	
	// Verifica o sinal (+ ou -)
	if (*str == '-' || *str == '+')
	{
		if (*str == '-')
			sign = -1;
		str++;
	}
	
	// Converte os dígitos para inteiro
	while (*str >= '0' && *str <= '9')
	{
		result = result * 10 + (*str - '0');
		str++;
	}
	
	return (result * sign);
}
