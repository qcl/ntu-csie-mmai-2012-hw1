# -*- coding: utf-8 -*-
#


import sys

if len(sys.argv) == 2:
    f = open(sys.argv[1],'r')
    fn = sys.argv[1].split('_')[0]
    d = ['l1d_rgb','l1d_hsv','l1d_yiq','l2d_rgb','l2d_hsv','l2d_yiq']
    for line in f:
        l = line.split()
        for i in range(0,6):
            filename = fn + '_' + d[i]
            fo = open(filename,'a')
            fo.write(l[0])
            for j in range(0,16):
                fo.write(' '+l[6*j+(i+1)])
            fo.write('\n')
            fo.close()

    f.close()



