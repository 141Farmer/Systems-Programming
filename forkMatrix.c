#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
void multiply(int n,int row,int col,int mat1[n][n],int mat2[n][n],int result[n][n]) 
{
	int sum=0;
        for(int k=0;k<n;++k) 
        {
        	    sum+=mat1[row][k]*mat2[k][col];
        }
        result[row][col]=sum;
    	
}
int main() 
{
	freopen("fork5Input.txt","r",stdin);
	int n;
	scanf("%d",&n);
	int mat1[n][n],mat2[n][n],result[n][n];
	for(int i=0;i<n;++i)
	{
		for(int j=0;j<n;++j)
		{
			scanf("%d",&mat1[i][j]);
		}
	}
	for(int i=0;i<n;++i)
	{
		for(int j=0;j<n;++j)
		{
			scanf("%d",&mat2[i][j]);
		}
	}
    	int pid;
    	printf("Multiplied matrix\n");
    	for(int i=0;i<n;++i) 
    	{
    		for(int j=0;j<n;++j)
    		{
			
			pid=fork();
        		if(pid<0) 
        		{
            			perror("Fork\n");
            			exit(1);
        		} 
        		else if(pid==0) 
        		{ 
            			multiply(n,i,j,mat1,mat2,result);
            			printf("result[%d][%d]=%d\n",i+1,j+1,result[i][j]);
            			exit(0);
        		}
        	}
    	}
    	exit(0);
}
