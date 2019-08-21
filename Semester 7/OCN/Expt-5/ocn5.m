clc; clear; close all;

S0=0.070;
lambda_o=1550;
n2=1.48;
der=0.26;
rri=0.002;
lambda=1250:1:1600;
c=3*(10^5);

Dwg=(((-1)*n2*rri*der)./(c.*lambda))*(10^(12));
Dt=(lambda.*S0.*(1-((lambda_o./lambda).^4)))/4;

Dm=Dt-Dwg;
figure;
xlabel('Wavelength (nm)');
ylabel('Dispersion (ps/(nm*km))');
title('Dispersion profile');
plot(lambda,Dm);
hold all;
plot(lambda,Dwg);
hold all;
plot(lambda,Dt);
grid on;





