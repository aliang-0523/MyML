from numpy import *;
import numpy as np
x=np.matrix([[1,1],[1,2],[1,3]]);
y=np.matrix([[1],[2],[3]]);
theta=np.matrix([[0.5]]);
temp=np.matrix([[0.0]]);
sum=0;
h=mat([[1],[1],[1]])
count=0;
times=0;
while(abs(theta.A[0]-temp.A[0])>0.000000001):
    for a in x[:, 1]:
        b=a.A;
        sum+=b[0]*theta.A[0]*b[0]-b[0]*y.A[count];
        count+=1;
    sum=sum/y.A.size;
    count=0;
    temp.A[0]=theta.A[0];
    theta.A[0]=theta.A[0]-0.1*sum;
    times+=1;
print(theta.A[0]);
print(times);
