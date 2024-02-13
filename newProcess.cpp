#include <stdlib.h> 
#include <unistd.h> 
#include <stdio.h>  
int main()
{
    char *args[] = {"ls", "-aF", "/", 0};
    //char *env[] = {0};   
    printf("About to run /bin/ls\n");
    execve("/bin/ls", args, 0);

    perror("execve");
    exit(1);
}