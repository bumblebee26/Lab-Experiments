clc
clear all
close all
length = input('Enter length of number of bits of power 2 : ');
walsh = hadamard(length)
codelength = input('Enter codelength required : ');
userno = input('Enter the number of users required : ');
orth_mat = walsh(1:userno,1:codelength)
