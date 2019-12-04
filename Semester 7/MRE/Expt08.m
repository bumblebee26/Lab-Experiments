clc;
close all;
clear all;

wh=0.1:0.05:5;
w=2.5;
er=10.5;
h=w./wh;

for i=1:length(wh)
    if(wh(i)<=1)
        eff0(i)=(er+1)/2 + (er-1)/2 * ((1+(12*1/wh(i)))^(-0.5) + 0.04*(1-wh(i))^(2));
        z0(i)=(60/sqrt(eff0(i))) * log((8/wh(i))+(wh(i)/4));
    else
        eff0(i)=(er+1)/2 + (er-1)/2 * ((1+(12*1/wh(i)))^(-0.5));
        z0(i)=(120*pi)/(sqrt(eff0(i))*(wh(i) + 1.393 + 0.667 * log(wh(i) + 1.444)));
    end
end

wh=0.1:0.05:5;
w=2.5;
er=4.4;
h=w./wh;

for i=1:length(wh)
    if(wh(i)<=1)
        eff1(i)=(er+1)/2 + (er-1)/2 * ((1+(12*1/wh(i)))^(-0.5) + 0.04*(1-wh(i))^(2));
        z1(i)=(60/sqrt(eff1(i))) * log((8/wh(i))+(wh(i)/4));
    else
        eff1(i)=(er+1)/2 + (er-1)/2 * ((1+(12*1/wh(i)))^(-0.5));
        z1(i)=(120*pi)/(sqrt(eff1(i))*(wh(i) + 1.393 + 0.667 * log(wh(i) + 1.444)));
    end
end

wh=0.1:0.05:5;
w=2.5;
er=2.2;
h=w./wh;

for i=1:length(wh)
    if(wh(i)<=1)
        eff2(i)=(er+1)/2 + (er-1)/2 * ((1+(12*1/wh(i)))^(-0.5) + 0.04*(1-wh(i))^(2));
        z2(i)=(60/sqrt(eff2(i))) * log((8/wh(i))+(wh(i)/4));
    else
        eff2(i)=(er+1)/2 + (er-1)/2 * ((1+(12*1/wh(i)))^(-0.5));
        z2(i)=(120*pi)/(sqrt(eff2(i))*(wh(i) + 1.393 + 0.667 * log(wh(i) + 1.444)));
    end
end

figure
plot(h,z0,h,z1,h,z2)
xlabel('h')
ylabel('characteristic impedence')
legend('er=10.5','er=4.4','er=2.2')

wh=0.1:0.05:5;
h=1.6;
er=10.5;
w=wh.*h;

for i=1:length(wh)
    if(wh(i)<=1)
        eff3(i)=(er+1)/2 + (er-1)/2 * ((1+(12*1/wh(i)))^(-0.5) + 0.04*(1-wh(i))^(2));
        z3(i)=(60/sqrt(eff3(i))) * log((8/wh(i))+(wh(i)/4));
    else
        eff3(i)=(er+1)/2 + (er-1)/2 * ((1+(12*1/wh(i)))^(-0.5));
        z3(i)=(120*pi)/(sqrt(eff3(i))*(wh(i) + 1.393 + 0.667 * log(wh(i) + 1.444)));
    end
end

figure
plot(wh,z3)
xlabel('wh')
ylabel('characteristic impedence')

