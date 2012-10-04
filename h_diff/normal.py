# -*- coding: utf-8 -*-
#
# normalization
#
import sys,math

if len(sys.argv) == 4:
    filename = sys.argv[1]
    width = float(sys.argv[2])
    height = float(sys.argv[3])

    f = open(filename,'r')
    o = open('n_'+filename+'_320_240','w')

    for line in f:
        l = line.split('\t')
        path = l[0]
        rgb = int(float(l[1])*(320.0*240.0)/(width*height))
        hsv = int(float(l[2])*(320.0*240.0)/(width*height))
        yiq = int(float(l[3])*(320.0*240.0)/(width*height))
        o.write(path+'\t'+str(rgb)+'\t'+str(hsv)+'\t'+str(yiq)+'\n')
    f.close()
    o.close()
        

