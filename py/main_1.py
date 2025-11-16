#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import par # local parameters

def cylinder_fource (th_1, th_2, l1, l2, F, e) -> float:
    # cyl 1
    ar1_x = np.cos(th_1) * l1 + np.cos(th_1 + th_2) * l2;
    mt1 = ar1_x * F;
    # mt = cyl_m = e * cyl_f
    return mt1 / e

t = np.r_[0:len(par.th_1)]

# z(t)
z = par.L_0 + np.sin( par.th_1 ) * par.l1 + np.sin( par.th_1 + par.th_2 ) * par.l2

plt.figure(1)
plt.subplot(2,2,1)
plt.plot(t, z)
plt.title('t-z')

# x(t)
x = np.cos( par.th_1 ) * par.l1 + np.cos( par.th_1 + par.th_2 ) * par.l2


plt.subplot(2,2,2)
plt.plot(t, x)
plt.title('t-x')

# x(z)
plt.subplot(2,2,3)
plt.plot(x, z)
plt.title('x-z')

F = par.mt * par.g
cyl1_f = cylinder_fource(par.th_1, par.th_2, par.l1, par.l2, F, par.e_1)
cyl2_f = cylinder_fource(par.th_1, par.th_2,      0, par.l2, F, par.e_2)

plt.subplot(2,2,4)
plt.plot(t,cyl1_f)
plt.plot(t,cyl2_f)

fig = plt.figure(2)
ax = fig.add_subplot(projection='3d')
ax.plot3D(t, x, z)

ax.view_init(elev=20, azim=45, roll=10)
ax.set_xlabel('Time')
ax.set_ylabel('Reach [m]')
ax.set_zlabel('Hegth [m]')

plt.show()
