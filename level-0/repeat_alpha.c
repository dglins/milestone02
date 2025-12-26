/* ************************************************************************** */
/*                                                                            */
/*   repeat_alpha.c                                                           */
/*                                                                            */
/*   Descrição: Programa que repete cada letra alfabética de acordo com      */
/*              sua posição no alfabeto (a=1x, b=2x, c=3x, etc.)             */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int argc, char **argv)
{
  int i;
  char c;
  int times;

  if (argc == 2)
  {
    i = 0;
    while (argv[1][i])
    {
      c = argv[1][i];
      times = 1;
      if (c >= 'a' && c <= 'z')
        times = c - 'a' + 1;
      else if (c >= 'A' && c <= 'Z')
        times = c - 'A' + 1;
      while (times > 0)
      {
        write(1, &c, 1);
        times--;
      }
      i++;
    }
  }
  write(1, "\n", 1);
  return (0);
}
