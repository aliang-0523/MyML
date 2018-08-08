from numpy import *;
import numpy as np
x=np.matrix([[1,1],[1,2],[1,3]]);
y=np.matrix([[1],[2],[3]]);
theta=0.5;
temp=0;
h=mat([[1],[1],[1]])
sum=0;
count=0;
while(abs(theta-temp)>0.01):
    for a in x[:, 1]:
        b=a.A;
        sum+=b[0]*theta*b[0]-b[0]*y.A[count];
        count+=1;
    sum=sum/3;
    count=0;
    temp=theta;
    theta=theta-0.1*sum;
print(theta);
