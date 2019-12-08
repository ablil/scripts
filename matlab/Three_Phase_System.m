% initiation
clear;
V_eff = 5; % 5 volts
freq = 0.1; % frequence
w = 2*pi*freq; % pulsation


syms t;
v1 = @(t) V_eff*sqrt(2)*sin(w.*t);
v2 = @(t) V_eff*sqrt(2)*sin(w.*t - 2*pi/3);
v3 = @(t) V_eff*sqrt(2)*sin(w.*t - 4*pi/3);

disp('tensions simples : ');
disp('v1(t) = '), disp(v1);
disp('v2(t) = '), disp(v2);
disp('v3(t) = '), disp(v2);

% tension simple
t = 0:.1:15;
V1 = v1(t);
V2 = v2(t);
V3 = v3(t);

% tension compose
u12 = V1 - V2;
u23 = V2 - V3;
u31 = V3 - V1;


% tension simple
figure;
subplot(3, 1, 1);
plot(t, V1); grid on;
hold on;
plot(t, V3, 'r');
plot(t, V2, 'c');
plot(t, V1 + V2 + V3,'g', 'LineWidth', 2);
title('Tension simple du source Triphase');
xlabel('Temps (s) ');ylabel('Amplitude');
legend('v1(t)', 'v2(t)', 'v3(t)');
hold off;

disp('tension composees');
disp('u12 = v1 - v2');
disp('u23 = v2 - v3');
disp('u31 = v3 - v3');

% tension composee
subplot(3,1,2);grid on; hold on;
plot(t, u12,'r', 'DisplayName', 'u12');
plot(t, u23,'g', 'DisplayName', 'u23');
plot(t, u31,'b', 'DisplayName', 'u31 ');
title('tension simple et compose');

subplot(3,1,3); grid on; hold on;
plot(t, V1 -V2, 'k', 'DisplayName', 'u12');
plot(t, V2 - V1,'r', 'DisplayName', 'u21');
plot(t, V1 - V3,'g', 'DisplayName','u13');
plot(t, V3 - V1,'m', 'DisplayName', 'u31');
plot(t, V2 - V3,'b', 'DisplayName','u23');
plot(t, V3-V2,'c', 'DisplayName', 'u32');
legend('u12', 'u21', 'u13', 'u31', 'u23', 'u32');

