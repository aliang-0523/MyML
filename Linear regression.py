from numpy import *;
import numpy as np
import math
x=np.matrix([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8]]);
y=np.matrix([[1],[2],[3],[4],[5],[6],[7],[8]]);
theta=np.matrix([[0.1],[0.4]]);
'判断Jtheta值是否收敛'
def compare(Jtheta,temp,slrange):
    if(abs(Jtheta-temp)>slrange):
        return True;
    else:
        return False;
'线性回归算法'
def linear_regression(learning_rate,slrange):
    count = 0;
    times = 0;
    temp = 0;
    Jtheta = 1;
    while(compare(Jtheta,temp,slrange)):
        sum = [0.0,0.0];
        for a in x[:, 1]:
            b=a.A;
            'jtheta对theta(i)的偏导的和'
            for i in range(0, len(sum)):
                '模型改变之后hypothesis(theta)的计算方式也需要改变'
                'sum[i]+=math.pow(b[0],i)*(theta.A[0]+b[0]*theta.A[1]-y.A[count]);'
                sum[i] += math.pow(b[0], i) * hypothesis(theta,b[0],y.A[count]);
            count+=1;
        temp = Jtheta;
        Jtheta = jtheta(x[:, 1].A, y.A, theta);
        for i in range(0, len(sum)):
            sum[i]=sum[i]/y.A.size;
            theta.A[i] = theta.A[i] - learning_rate * sum[i];
        count=0;
        times+=1;
    print(theta.A[0]);
    print(theta.A[1]);
    print(times);
def hypothesis(theta,x,y):
    return theta.A[0]+x*theta.A[1]-y;
def jtheta(x,y,theta):
    sum=0;
    for i in range(0, len(y)):
        sum+=math.pow(theta.A[0]+theta.A[1]*x[i]-y[i],2);
    return sum;
if __name__ == '__main__':
    linear_regression(0.075,0.00000001);