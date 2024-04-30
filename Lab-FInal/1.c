#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define NUM_STUDENTS 10
#define NUM_SLICES_PER_PIZZA 8


sem_t pizza;        
sem_t deliver;      
int num_slices=0; 
pthread_mutex_t mutex; 


void *student_thread(void *arg) 
{
    int student_id=*((int *)arg);
    while (1) 
    {
        sem_wait(&pizza); 
        pthread_mutex_lock(&mutex);
        if(num_slices>0) 
        {
            --num_slices; 
            printf("Student %d is eating pizza. Slices left: %d\n",student_id,num_slices);
        } 
        else 
        {
            printf("Student %d found no pizza. Going to sleep.\n",student_id);
            sem_post(&deliver);
            pthread_mutex_unlock(&mutex);
            sem_wait(&pizza); 
            pthread_mutex_lock(&mutex);
            if(num_slices>0)
            {
                --num_slices; 
                printf("Student %d is eating pizza. Slices left: %d\n",student_id,num_slices);
            }           
        }
        pthread_mutex_unlock(&mutex);
        sleep(1);
    }
    return NULL;
}

void *delivery_thread(void *arg) 
{
    while(1) 
    {
        sem_wait(&deliver); 
        pthread_mutex_lock(&mutex);
        if (num_slices==0) 
        {
            num_slices+=NUM_SLICES_PER_PIZZA; 
            printf("Pizza delivered. Slices left: %d\n",num_slices);
            pthread_mutex_unlock(&mutex);
            for(int i=0;i<NUM_STUDENTS;++i)
            {
                sem_post(&pizza);
            }
        } 
        else 
        {
            pthread_mutex_unlock(&mutex);
        }
    }
    return NULL;
}

int main() {
    pthread_t students[NUM_STUDENTS];
    pthread_t delivery;
    int student_ids[NUM_STUDENTS];
    
    sem_init(&pizza,0,0);
    sem_init(&deliver,0,1);
    pthread_mutex_init(&mutex,NULL);
    

    for(int i=0;i<NUM_STUDENTS;++i) 
    {
        student_ids[i]=i+1;
        pthread_create(&students[i],NULL,student_thread,&student_ids[i]);
    }
    
    pthread_create(&delivery,NULL,delivery_thread,NULL);
    

    for(int i=0;i<NUM_STUDENTS;++i) 
    {
        pthread_join(students[i],NULL);
    }
    pthread_join(delivery,NULL);
    
    sem_destroy(&pizza);
    sem_destroy(&deliver);
    pthread_mutex_destroy(&mutex);
    
    return 0;
}
