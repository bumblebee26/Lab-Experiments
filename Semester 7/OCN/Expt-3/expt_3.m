clc;
clear all;
close all;
pi=3.14;
n=1.46;
l=[0.63 1 1.3].*10^-6;
p=0.286;
b=7.*(10.^-11);
k=1.381.*(10.^-23);
t=1400;
y=(8.*((pi).^3).*((n).^8).*((p).^2).*b.*k.*t)./(3.*((l).^4))
l1=850:100:1550;
y1=(8.*((pi).^3).*((n).^8).*((p).^2).*b.*k.*t)./(3.*((l1).^4))
plot(l1,y1);
xlabel('lambda')
ylabel('loss in optical fiber')
alpha=exp(-(y.*1000));
disp('alpha=');
disp(alpha)
a=1./alpha;
alphadb=-10.*log10(alpha);
disp('alphadb=');
disp(alphadb)