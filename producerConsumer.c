#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <unistd.h>

#define MAX_NUM_ITEMS 5
#define MAX_NUM_CONSUMERS 8

pthread_mutex_t mutex;
sem_t empty;
sem_t full;
int num_items=0;

void* producer(void* arg) 
{
    while(1) 
    {
        sem_wait(&empty);
        pthread_mutex_lock(&mutex);
        ++num_items;
        printf("Produced item %d\n", num_items);
        pthread_mutex_unlock(&mutex);
        sem_post(&full);
        sleep(1);
    }
    return NULL;
}

void* consumer(void* arg) 
{
    int consumer_num=*(int*)arg;
    while(1) 
    {
        sem_wait(&full);
        pthread_mutex_lock(&mutex);
        printf("Consumer %d consumed item %d\n", consumer_num, num_items);
        --num_items;
        pthread_mutex_unlock(&mutex);
        sem_post(&empty);
        sleep(1);
    }
    return NULL;
}

int main() 
{
    pthread_t producers[MAX_NUM_ITEMS];
    pthread_t consumers[MAX_NUM_CONSUMERS];
    pthread_mutex_init(&mutex, NULL);
    sem_init(&empty,0,MAX_NUM_ITEMS);
    sem_init(&full,0,0);
    for int i=0;i<MAX_NUM_ITEMS;++i) 
    {
        pthread_create(&producers[i],NULL,producer,NULL);
    }
    for(int i=0;i<MAX_NUM_CONSUMERS;++i) 
    {
        int* arg=malloc(sizeof(*arg));
        *arg=i+1;
        pthread_create(&consumers[i],NULL,consumer,arg);
    }
    for(int i=0;i<MAX_NUM_ITEMS;++i) 
    {
        pthread_join(producers[i],NULL);
    }
    for(int i=0;i<MAX_NUM_CONSUMERS;++i) 
    {
        pthread_join(consumers[i],NULL);
    }
    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);
    return 0;
}
