clc
clear all
close all

n1=input('Enter n1 : ');
n2=input('Enter n2 : ');
cd=input('Enter core diameter : ');
cr=cd/2;
cr=cr/(1000000);
w=input('Enter wavelength : ');
w=w/(1000000000);
NA=power((n1)^(2)-(n2)^(2),0.5);
acc=asin(NA);
acc=(acc)*((180)/(3.14));
cri=asin(n2/n1);
cri=(cri)*((180)/(3.14));
V=((2*3.14)/w)*(cr)*(NA);
M=((V)^2)/(2);
disp('NA = ')
disp(NA)
disp('Acceptance angle = ');
disp(acc);
disp('Critical angle = ')
disp(cri)
disp('Normalized frequency = ');
disp(V)
disp('Number of modes = ')
disp(M);
