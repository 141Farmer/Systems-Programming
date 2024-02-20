#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
int main() 
{
    	int n;
    	scanf("%d",&n);
    	int pid=fork();
    	if(pid<0) 
    	{
        	perror("Fork\n");
        	exit(1);
    	} 
    	else if(pid==0) 
    	{	 
        	int odd_sum=0;
        	for (int i=1;i<=n;i+=2)     odd_sum+=i;
        	printf("Child process: Sum of odd numbers  %d\n",odd_sum);
    	} 
    	else 
    	{ 
        	int even_sum=0;
        	for(int i=2;i<=n;i+=2) 	    even_sum+=i;   
        	printf("Parent process: Sum of even numbers %d\n",even_sum);
    	}
    	exit(0);
}
