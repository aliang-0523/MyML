from numpy import *;
import numpy as np
x=np.matrix([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[1,13],[1,14],[1,15],[1,16]]);
y=np.matrix([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16]]);
theta=np.matrix([[0.5]]);
temp=np.matrix([[0.0]]);
'判断theta值是否收敛'
def compare(the,tem,slrange):
    countn = 0;
    for i in the.A:
        if(abs(i-tem.A[np.where(the.A==i)])>slrange):
            countn+=1;
    if(countn==the.A.size):
        return True;
    else:
        return False;
'线性回归算法'
def linear_regression(learning_rate,slrange):
    count = 0;
    times = 0;
    while(compare(theta,temp,slrange)):
        sum = 0.0;
        for a in x[:, 1]:
            b=a.A;
            'jtheta对theta(i)的偏导的和'
            sum+=b[0]*theta.A[0]*b[0]-b[0]*y.A[count];
            count+=1;
        sum=sum/y.A.size;
        count=0;
        temp.A[0]=theta.A[0];
        theta.A[0]=theta.A[0]-learning_rate*sum;
        times+=1;
    print(theta.A[0]);
    print(times);
if __name__ == '__main__':
    linear_regression(0.005,0.000000001);