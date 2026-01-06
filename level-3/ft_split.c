/* ************************************************************************** */
/*                                                                            */
/*   ft_split.c                                                               */
/*                                                                            */
/*   Descrição: Divide uma string em palavras e retorna array de strings     */
/*   terminado em NULL                                                        */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int is_space(char c)
{
  return (c == ' ' || c == '\t' || c == '\n');
}

int count_words(char *str)
{
  int count;

  count = 0;
  while (*str)
  {
    while (*str && is_space(*str))
      str++;
    if (*str)
    {
      count++;
      while (*str && !is_space(*str))
        str++;
    }
  }
  return (count);
}

int word_len(char *str)
{
  int len;

  len = 0;
  while (str[len] && !is_space(str[len]))
    len++;
  return (len);
}

char  *copy_word(char *str, int len)
{
  char *word;
  int i;

  word = (char *)malloc(sizeof(char) * (len + 1));
  if (!word)
    return (NULL);
  i = 0;
  while (i < len)
  {
    word[i] = str[i];
    i++;
  }
  word[i] = '\0';
  return (word);
}


char    **ft_split(char *str)
{
  char **result;
  int words;
  int len;
  int i;

  words = count_words(str);
  result = (char **)malloc(sizeof(char *) * (words + 1));
  if (!result)
    return (NULL);
  i = 0;
  while (*str)
  {
    if (!is_space(*str))
    {
      len = word_len(str);
      result[i] = copy_word(str, len);
      if (!result[i])
        return (NULL);
      str += len;
      i++;
    }
    else
      str++;
  }
  result[i] = NULL;
  return (result);
}
