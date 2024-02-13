#include <stdlib.h> 
#include <unistd.h> 
#include <stdio.h> 
void runit()
{
    printf("About to run ls\n");
    execlp("ls", "ls", "-aF", "/", (char *)0);
    perror("execlp"); 
    exit(1);
} 
int main()
{
    int pid; 
    switch (pid = fork())
    {
        case 0: 
            runit();
            break;
        default:      
            sleep(5); 
            printf("I'm still here!\n");
            break;
        case -1: 
            perror("fork");
            exit(1);
    }
    exit(0);
}
