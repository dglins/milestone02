/* ************************************************************************** */
/*                                                                            */
/*   print_bits.c                                                             */
/*                                                                            */
/*   Imprime um byte em formato binário (8 bits)                             */
/*   Exemplo: 2 -> "00000010"                                                */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	print_bits(unsigned char octet)
{
	int				i;
	unsigned char	bit;

	// Começa do bit mais significativo (bit 7) até o menos significativo (bit 0)
	i = 7;
	while (i >= 0)
	{
		// Desloca o bit desejado para a posição menos significativa
		// e faz AND com 1 para isolar apenas esse bit
		bit = (octet >> i) & 1;
		
		// Converte o bit (0 ou 1) para caractere ASCII ('0' ou '1')
		bit = bit + '0';
		
		// Imprime o caractere
		write(1, &bit, 1);
		
		i--;
	}
}
