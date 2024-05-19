#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <unistd.h>

#define MAX_READERS 3
#define NUM_READERS 3
#define NUM_WRITERS 3

pthread_mutex_t mutex;
sem_t readerSem;
sem_t writerSem;
int readers=0;
char resource[1024]="";

void* readerThread(void* arg) 
{
    int readerId=*(int*)arg;
    while(1) 
    {
        sem_wait(&readerSem);
        pthread_mutex_lock(&mutex);
        ++readers;
        if (readers>0) 
        {
            sem_wait(&writerSem);
        }
        pthread_mutex_unlock(&mutex);
        sem_post(&readerSem);
        printf("Reader %d is reading %s\n", readerId, resource);
        sleep(2);
        pthread_mutex_lock(&mutex);
        --readers;
        if (readers==0) 
        {
            sem_post(&writerSem);
        }
        pthread_mutex_unlock(&mutex);
        sleep(2);
    }
    return NULL;
}

void* writerThread(void* arg) 
{
    int writerId=*(int*)arg;
    char value[2]={(char)writerId+'a','\0'};
    while(1) 
    {
        sem_wait(&writerSem);
        printf("Writer %d is writing %s\n", writerId, value);
        strcat(resource,value);
        sem_post(&writerSem);
        sleep(2);
    }
    return NULL;
}

int main() 
{
    pthread_t readers[NUM_READERS];
    pthread_t writers[NUM_WRITERS];
    pthread_mutex_init(&mutex, NULL);
    sem_init(&readerSem, 0, MAX_READERS);
    sem_init(&writerSem, 0, 1);

    for (int i=0;i<NUM_READERS;++i) 
    {
        int* arg=malloc(sizeof(*arg));
        *arg=i+1;
        pthread_create(&readers[i],NULL,readerThread,arg);
    }

    for (int i=0;i<NUM_WRITERS;++i) 
    {
        int* arg=malloc(sizeof(*arg));
        *arg=i+1;
        pthread_create(&writers[i],NULL,writerThread,arg);
    }

    for (int i=0;i<NUM_READERS;++i) 
    {
        pthread_join(readers[i],NULL);
    }

    for (int i=0;i<NUM_WRITERS;++i) 
    {
        pthread_join(writers[i],NULL);
    }

    pthread_mutex_destroy(&mutex);
    sem_destroy(&readerSem);
    sem_destroy(&writerSem);
    return 0;
}
