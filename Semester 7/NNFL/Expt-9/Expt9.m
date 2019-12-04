clc; clear all; close all;

x=0:0.25:4;
y=sin(pi*x)+cos(pi*x);

net=newrb(x,y);
view(net);

x1=0:0.2:4;
y1=sim(net,x1);

figure
hold on;
plot(x,y,'*r')
plot(x1,y1,'ob')
legend('Training','Testing')
xlabel('Inputs')
ylabel('Targets')