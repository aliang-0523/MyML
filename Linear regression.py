from numpy import *;
import numpy as np
x=np.matrix([[1,1],[1,2],[1,3]]);
y=np.matrix([[1],[2],[3]]);
theta=np.matrix([[0.5]]);
temp=np.matrix([[0.0]]);
h=mat([[1],[1],[1]])
'判断theta值是否收敛'
def compare(the,tem):
    countn = 0;
    for i in the.A:
        if(abs(i-tem.A[np.where(the.A==i)])>0.000000001):
            countn+=1;
    if(countn==the.A.size):
        return True;
    else:
        return False;
'线性回归算法'
def linear_regression():
    sum = 0;
    count = 0;
    times = 0;
    while(compare(theta,temp)):
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
if __name__ == '__main__':
    linear_regression();