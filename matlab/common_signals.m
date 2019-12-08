% PLOT COMMON SIGNALS USED IN SIGNAL PROCESSING
clc; clear;

disp('1/ heaviside');
disp('2/ rectangular pulse');
disp('3/ square signal');
disp('4/ sawtooth signal');

choice = input('Type a number: ');

t = -10:.01:10;                 % Time vector

if ( choice == 1 )
    x = heaviside(t);
elseif ( choice == 2)
    x = rectangularPulse(-1/2, 1/2, t);
elseif ( choice == 3 )
    x = square(2*pi*1.5*t);
elseif ( choice == 4 )
    x = sawtooth(t, 0.75);
else
    disp('Invalide choice');
    x = 0*t;
end

figure;
plot(t, x);
axis equal;
title('Signal');
xlabel('Time (s)'); ylabel('Amplitude');
     