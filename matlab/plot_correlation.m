% PLOT CORRELATION BETWEEN TWO SIGNALS

t = -10:0.01:10;                        % Time vecotr
x = rectangularPulse(-1/2, 1/2, t);     % Signal x(t)
y = heaviside(t).*exp(-0.2*t);          % Signal y(t)

[corr, lags] = xcorr(x, y);              % Correlation


% plot
figure;
plot(lags, corr);
title('Correlation');
xlabel('lags (s)'); ylabel('Amplitude');