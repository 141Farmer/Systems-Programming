from threading import Thread,current_thread
from os import getpid

def multiply(n,row,col,mat1,mat2,result):
    for k in range(n):
        result[row][col]+=(mat1[row][k]*mat2[k][col])   

def main():
    with open('fork5Input.txt','r') as f:
        n=int(f.readline())
        mat1=[]
        for _ in range(n):
            mat1.append(list(map(int,f.readline().split())))
        mat2=[]
        for _ in range(n):
            mat2.append(list(map(int,f.readline().split())))
    result=[[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            Thread(target=multiply,args=(n,i,j,mat1,mat2,result)).start()
            print(f'Thread identifier: {current_thread().ident} Result[{i+1}][{j+1}]={result[i][j]}')
    
    '''for row in result:
        print(*row)'''

if __name__=='__main__':
    main()