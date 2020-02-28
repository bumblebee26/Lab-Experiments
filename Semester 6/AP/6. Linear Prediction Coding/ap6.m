% Linear Predictor
clear all
close all 
clc
[y,fs]=audioread('s1.wav');
p=11;
N=160;

for k=1:20
    n=(k-1)*N+[1: N];
    frame=y(n);
    auto1=xcorr(frame)/N;
    r=auto1(N:N+p);
    R=toeplitz(r(1:p));
    a(:,k)=[1;-inv(R)*r(2:p+1)];
end

subplot(1,3,1)
plot(r)
subplot(1,3,2)
plot(R)
subplot(1,3,3)
plot(a)

