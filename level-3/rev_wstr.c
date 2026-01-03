/* ************************************************************************** */
/*                                                                            */
/*   rev_wstr.c                                                               */
/*                                                                            */
/*   Descrição: Programa que imprime as palavras de uma string em ordem      */
/*   reversa                                                                  */
/*                                                                            */
/* ************************************************************************** */

  	 #include <stdlib.h>
     #include <unistd.h>

     static int is_space(char c) {
       return (c == ' ' || (c >= 9 && c <= 13));
     }

     static int skip_spaces_left(const char *s, int i) 
{
       while (i >= 0 && is_space(s[i])) 
		   i--;
       return i;
     }

     static int skip_word_left(const char *s, int i) 
{
       while (i >= 0 && !is_space(s[i])) 
		   i--;
       return i;
     }

     static void write_word(const char *s, int start, int end) 
{
       while (start <= end) 
		   write(1, &s[start++], 1);
     }

     int main(int argc, char **argv) 
{
       if (argc == 2) {
         int i = 0;
         while (argv[1][i]) 
			 i++;
         while (i >= 0) 
		 {
           i = skip_spaces_left(argv[1], i);
           if (i < 0) 
			   break;
           int start = skip_word_left(argv[1], i) + 1;
           write_word(argv[1], start, i);
           i = skip_word_left(argv[1], i);
           i = skip_spaces_left(argv[1], i);
           if (i >= 0) 
			   write(1, " ", 1);
		   i--;
         }
       }
       write(1, "\n", 1);
       return 0;
     }

