% PLOT CONVOLUTION BETWEEN TWO SIGNALS

t = -10:0.01:10;                        % Time vecotr
x = rectangularPulse(-1/2, 1/2, t);     % Signal x(t)
y = heaviside(t).*exp(-0.2*t);          % Signal y(t)

XY = conv(x, y);                         % Convolution


% plot
figure;
plot(XY);
title('Convolution');
xlabel('Time (s)'); ylabel('Amplitude');