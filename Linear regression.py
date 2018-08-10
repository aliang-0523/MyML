from numpy import *;
import numpy as np
import math
x=np.matrix([[1,1],[1,2],[1,3]]);
y=np.matrix([[1],[2],[3]]);
theta=np.matrix([[0.1],[0.4]]);
temp=np.matrix([[0.0],[0.1]]);
'判断theta值是否收敛'
def compare(the,tem,slrange):
    countn = [0,0];
    delta=0;
    for i in range(0, len(the.A)):
        if(abs(the.A[i] - tem.A[i])>slrange):
            countn[i]+=1;
        if(countn[i]==1):
            delta+=1;
    if(delta==len(the.A)):
        return True;
    else:
        return False;
'线性回归算法'
def linear_regression(learning_rate,slrange):
    count = 0;
    times = 0;
    while(compare(theta,temp,slrange)):
        sum = [0.0,0.0];
        for a in x[:, 1]:
            b=a.A;
            'jtheta对theta(i)的偏导的和'
            for i in range(0, len(sum)):
                '模型改变之后hypothesis(theta)的计算方式也需要改变'
                sum[i]+=math.pow(b[0],i)*(theta.A[0]+b[0]*theta.A[1]-y.A[count]);
            count+=1;
        for i in range(0, len(sum)):
            sum[i]=sum[i]/y.A.size;
            temp.A[i] = theta.A[i];
            theta.A[i] = theta.A[i] - learning_rate * sum[i];
        count=0;
        times+=1;
    print(theta.A[0]);
    print(theta.A[1]);
    print(times);
if __name__ == '__main__':
    linear_regression(0.32,0.000000000001);