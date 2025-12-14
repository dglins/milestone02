/* ************************************************************************** */
/*                                                                            */
/*   rostring.c                                                               */
/*                                                                            */
/*   Descrição: Programa que rotaciona uma string movendo a primeira         */
/*   palavra para o final                                                     */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

static int is_space(char c)
{
	return (c == ' ' || c == '\t');
}

/* print a word given a pointer to its start and length */
static void write_word(const char *start, int len)
{
	if (len > 0)
		write(1, start, len);
}

int	main(int argc, char **argv)
{
	const char	*str;
	const char	*p;
	int			first_start = -1;
	int			first_len = 0;
	int			printed_any = 0;

	if (argc < 2)
	{
		write(1, "\n", 1);
		return (0);
	}

	str = argv[1];
	p = str;

	/* skip leading spaces */
	while (*p && is_space(*p))
		p++;

	/* record first word start and length */
	if (*p)
	{
		first_start = p - str;
		while (p[first_len] && !is_space(p[first_len]))
			first_len++;
	}

	/* start printing words after the first word */
	p = str;
	/* move p to just after the first word */
	if (first_start >= 0)
		p += first_start + first_len;
	else
		p = str;

	/* iterate through remaining words and print them separated by single spaces */
	while (*p)
	{
		/* skip spaces */
		while (*p && is_space(*p))
			p++;

		if (!*p)
			break;

		/* find word length */
		const char *word_start = p;
		int wlen = 0;
		while (p[wlen] && !is_space(p[wlen]))
			wlen++;

		/* print a space before subsequent words (not before the first printed one) */
		if (printed_any)
			write(1, " ", 1);

		write_word(word_start, wlen);
		printed_any = 1;

		/* advance p */
		p = word_start + wlen;
	}

	/* if we printed some words and there is a first word, separate with a space */
	if (first_len > 0)
	{
		if (printed_any)
			write(1, " ", 1);
		/* print the first word */
		write_word(str + first_start, first_len);
	}

	write(1, "\n", 1);
	return (0);
}
