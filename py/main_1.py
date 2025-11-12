#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import par # local parameters

t = np.r_[0:len(par.th_1)]

z = par.L_0 + np.sin( par.th_1 ) * par.l1 + np.sin( par.th_1 + par.th_2 ) * par.l2

plt.subplot(2,2,1)
plt.plot(t, z)

x = np.cos( par.th_1 ) * par.l1 + np.cos( par.th_1 + par.th_2 ) * par.l2

plt.subplot(2,2,2)
plt.plot(x, z)

plt.show()
