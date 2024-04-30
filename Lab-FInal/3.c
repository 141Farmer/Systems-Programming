#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<pthread.h>
#include<unistd.h>

void *thread_task() 
{
    while (1) 
    {
        printf("Thread task is running...\n");
        sleep(1);
    }
    return NULL;
}

void sigint_handler() 
{
    printf("\nSIGINT signal caught. Terminating program.\n");
    exit(0);
}

int main() 
{
    signal(SIGINT,sigint_handler);
    pthread_t tid;
    if (pthread_create(&tid,NULL,thread_task,NULL)!=0) 
    {
        perror("pthread_create");
        exit(1);
    }
    while(1) 
    {
        printf("Main program is running...\n");
        sleep(1);
    }
    return 0;
}
