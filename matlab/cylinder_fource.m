function cyl_fource = cylinder_fource (th_1, th_2, l1, l2, F, e)
    % cyl 1
    ar1_x = cos(th_1) * l1 + cos(th_2) * l2;
    mt1 = ar1_x * F;
    % mt = cyl_m = e * cyl_f
    cyl_fource = mt1 ./ e;
end