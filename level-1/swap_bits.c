/* ************************************************************************** */
/*                                                                            */
/*   swap_bits.c                                                              */
/*                                                                            */
/*   Troca as metades de um byte (4 bits superiores com 4 bits inferiores)  */
/*   Exemplo: 0100 0001 -> 0001 0100                                         */
/*                                                                            */
/* ************************************************************************** */

unsigned char	swap_bits(unsigned char octet)
{
	// Desloca os 4 bits superiores para a direita (tornam-se os 4 bits inferiores)
	// Desloca os 4 bits inferiores para a esquerda (tornam-se os 4 bits superiores)
	// Combina os dois resultados com OR
	return ((octet >> 4) | (octet << 4));
}
