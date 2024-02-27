#include <stdlib.h> 
#include <unistd.h> 
#include <stdio.h>  
int main()
{
    char *args[] = {"ls", "-aF", "/", 0};
    printf("About to run ls\n");
    execvp("ls", args);
    perror("execvp");
    exit(1);
}