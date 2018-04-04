pkg load control;
pkg load signal;
clear all;
clc;
close all;
%
N = 4;
k = 2;
%Take the so-called sine window or baseband prototype for N=4 subbands
figure(1)
h=sin(pi/8*((0:7)+0.5));
plot(h)
% The corresponding frequency response is
figure(2)
freqz(h)
subplot(2,1,1)
axis([0 1 -30 20])
% We see that this is indeed a low pass filter. It works as both, a window and a 
%low pass prototype filter. Now we construct the filter impulse response for 
%subband k=2
%h2 = h.* sqrt(2/N) * cos(pi/4 * ((0:7)+0.5+4/2) * (2.5));
h2 = h.* cos(pi/4 * ((0:7)+0.5+4/2) * (2.5));
%and we get the following frequency response,
figure(3)
freqz(h2)
subplot(2,1,1)
axis([0 1 -30 20])
%We see that our low pass filter is indeed shifted in frequency to become a 
%bandpass filter.