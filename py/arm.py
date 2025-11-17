#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import par

# vars
#

for t in range(len(par.th_1)):
    th_1 = par.th_1[t]
    th_2 = par.th_2[t]

    p0 =      np.array([0, 0])
    p1 =      np.array([0, par.L_0])
    p2 = p1 + np.array([np.cos(th_1), np.sin(th_1)]) * par.l1
    p3 = p2 + np.array([np.cos(th_2), np.sin(th_2)]) * par.l2

    plt.clf()
    plt.plot()
    plt.plot([p0[0], p1[0]], [p0[1], p1[1]], '-b')
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], '-b')
    plt.plot([p2[0], p3[0]], [p2[1], p3[1]], '-b')

    plt.xlim(-1, 6)
    plt.ylim(-1, 6)

    plt.pause(0.1)
