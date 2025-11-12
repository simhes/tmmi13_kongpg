%% z (t)
% lound in par
clear
par

%% time
t = 1:1:length(th_1);

%% pozitions plot
% plot z
z = L_0 + sin(th_1) .* l1 + sin(th_1 + th_2) .* l2;
disp('Figure 1, Crane hite over time')
figure(1)
subplot(2,2,1)

plot(t, z)
title('Crane hite over time')
xlabel('Time [s]')
ylabel('Higth [m]')
grid on

% plot x
x = cos(th_1) .* l1 + cos(th_1 + th_2) .* l2;
disp('Figure 2, Crane horizonal reach')

%figure(2)
subplot(2,2,2)

plot(x, z)
title('Crane horizonal reach over time')
xlabel('Horysentel dist [m]')
ylabel('Higth [m]')
grid on

%% fource plot
F = mt * g; 

% cyl 1
cyl1_f = cylinder_fource(th_1, th_2, l1, l2, F, e_1);
disp('Force on cylinder 1')

subplot(2,2,[3,4])

plot(t,cyl1_f)
title('Figure 3, Force on cylinder 1')
xlabel('Time [s]')
ylabel('Fource [N]')

% cyl 2
cyl2_f = cylinder_fource(th_1, th_2, 0, l2, F, e_2);

hold on
plot(t, cyl2_f)
disp('Figure 4, Force on cylinder 2')
grid on
title('Force on cylinder 2')
xlabel('Time [s]')
ylabel('Fource [N]')
legend('Cyl1', 'Cyl2')
hold off
%% wors case
% th_#_wc_cyl#
F_max = g * mt_max;
% wc läge cyl 1
cyl_1_wc1 = cylinder_fource(th_1_wc_cyl1, th_2_wc_cyl1, l1, l2, F_max, e_1_wc_cyl1);
cyl_2_wc1 = cylinder_fource(th_1_wc_cyl1, th_2_wc_cyl1,  0, l2, F_max, e_1_wc_cyl2);

% wc 
cyl_1_wc2 = cylinder_fource(th_1_wc_cyl2, th_2_wc_cyl2, l1, l2, F_max, e_2_wc_cyl1);
cyl_2_wc2 = cylinder_fource(th_1_wc_cyl2, th_2_wc_cyl2,  0, l2, F_max, e_2_wc_cyl2);

disp('Worst case: ')
disp(   '+======================+')
fprintf('| wc cyl1:             |\n')
fprintf('| * cyl1: %d |\n', cyl_1_wc1)
fprintf('|   cyl2: %d |\n', cyl_2_wc1)
disp(   '+======================+')
fprintf('| wc cyl2:             |\n')
fprintf('|   cyl1: %d |\n', cyl_1_wc2)
fprintf('| * cyl2: %d |\n', cyl_2_wc2)
disp(   '+======================+')
