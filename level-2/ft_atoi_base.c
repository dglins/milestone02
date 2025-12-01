/* ************************************************************************** */
/*                                                                            */
/*   ft_atoi_base.c                                                           */
/*                                                                            */
/*   Descrição: Converte uma string em base N (N <= 16) para inteiro base 10 */
/*                                                                            */
/*   Conceitos: Conversão de bases, parsing, validação de caracteres         */
/*                                                                            */
/* ************************************************************************** */

/* Converte um caractere hexadecimal para seu valor numérico
 * 
 * Aceita: '0'-'9' (valor 0-9), 'a'-'f' (valor 10-15), 'A'-'F' (valor 10-15)
 * Retorna: -1 se o caractere não é válido
 */
int	get_digit_value(char c)
{
	/* Dígitos numéricos 0-9 */
	if (c >= '0' && c <= '9')
		return (c - '0');
	/* Letras minúsculas a-f (valores 10-15) */
	if (c >= 'a' && c <= 'f')
		return (c - 'a' + 10);
	/* Letras maiúsculas A-F (valores 10-15) */
	if (c >= 'A' && c <= 'F')
		return (c - 'A' + 10);
	/* Caractere inválido */
	return (-1);
}

/* Converte string em base str_base para inteiro em base 10
 * 
 * Algoritmo:
 * 1. Verifica sinal negativo
 * 2. Para cada dígito válido na base:
 *    - Multiplica resultado atual pela base
 *    - Adiciona o valor do dígito
 * 
 * Exemplo: "1a" em base 16
 *   '1' -> result = 0 * 16 + 1 = 1
 *   'a' -> result = 1 * 16 + 10 = 26
 */
int	ft_atoi_base(const char *str, int str_base)
{
	int	result;
	int	sign;
	int	digit;
	int	i;

	result = 0;
	sign = 1;
	i = 0;

	/* Verifica se há sinal negativo no início */
	if (str[i] == '-')
	{
		sign = -1;
		i++;
	}

	/* Processa cada caractere da string */
	while (str[i])
	{
		/* Obtém o valor numérico do caractere */
		digit = get_digit_value(str[i]);
		
		/* Se o dígito é inválido ou maior que a base, para */
		if (digit == -1 || digit >= str_base)
			break;
		
		/* Multiplica resultado pela base e adiciona o dígito */
		result = result * str_base + digit;
		i++;
	}

	return (result * sign);
}
