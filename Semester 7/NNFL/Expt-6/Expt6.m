clc; clear all; close all;

p=[1 -1 1 -1; 1 1 -1 -1];
t=[-1 1 1 -1];

net=newff(minmax(p),[4 1]);
net.trainParam.lr=0.1;
net.trainParam.goal=0.0001;
net.trainParam.epochs=1000;
net.trainParam.show=1;
net1=train(net,p,t);
y=sim(net1,p);
round(y)

