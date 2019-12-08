% PLOT FOURIER TRANSFORM

% Define variables
fs = 1000;              % Sampling frequency
N = 500;                % Number of fft
t = 0:1/fs:20;          % Time vector
f = (0:N-1)*fs/N;       % frequency vector

x = cos(2*pi*10*t) + sin(2*pi*250*t);    % Signal Vector
xfft = fft(x, N);       % Fourier transform of signal

% Plot
figure;
plot(f(1:N/2), abs(xfft(1:N/2)));
title('Fourier Transfrom')
xlabel('Frequency (hz)'); ylabel('Amplitude');