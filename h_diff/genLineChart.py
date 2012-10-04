# -*- coding: utf-8 -*-
#
# 

import sys,Gnuplot
if len(sys.argv) == 2:
    filename = sys.argv[1]
    gp = Gnuplot.Gnuplot()
    gp('set terminal png')
    gp('set grid')
    gp('set style data linespoints')
    gp("set output '"+filename+"_rgb.png'")
    gp('plot "'+filename+'" u 0:2 title "RGB"')
    gp('reset')
    gp('set terminal png')
    gp('set grid')
    gp('set style data linespoints')
    gp("set output '"+filename+"_hsv.png'")
    gp('plot "'+filename+'" u 0:3 title "HSV"')
    gp('reset')
    gp('set terminal png')
    gp('set grid')
    gp('set style data linespoints')
    gp("set output '"+filename+"_yiq.png'")
    gp('plot "'+filename+'" u 0:4 title "YIQ"')
    gp('reset')
    gp('set terminal png')
    gp('set grid')
    gp('set style data linespoints')
    gp("set output '"+filename+"_all.png'")
    gp('plot "'+filename+'" u 0:2 title "RGB","" u 0:3 title "HSV", "" u 0:4 title "YIQ"')
    
