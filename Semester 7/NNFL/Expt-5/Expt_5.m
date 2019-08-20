clc; clear; close all;

p=[1 1 -1 -1; 1 -1 1 -1]
t=[1 -1 -1 -1]
[n1, n2]=size(p);
w1=randi([0 1]);
w2=randi([0 1]);
b=0;
alpha=input('Enter the value of alpha');
theta=input('Enter the value of theta');

for i=1:n2
        yin=p(1,i)*w1+b + p(2,i)*w2+b;
        if(yin>theta)
            y=1;
        elseif(yin<-theta)
            y=-1;
        elseif(-theta<=yin<=theta)
            y=0;
        end
        if(y~=t(i))
            w1=w1+alpha*t(i)*p(1,i);
            w2=w2+alpha*t(i)*p(2,i);
        end
end    





