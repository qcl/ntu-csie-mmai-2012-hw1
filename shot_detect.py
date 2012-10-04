# -*- coding:utf-8 -*-
# Qing-Cheng Li
# R01922024
#
# qingcheng.li@qcl.tw / r01922024@csie.ntu.edu.tw
#
# MMAI 2012 Homework#1
#
# shot_detect.py 
#
import sys,os,math

def main(difffile):
    df = open(difffile,'r')

    rgb_th = 30000
    hsv_th = 60000
    yiq_th = 25000

    for line in df:
        l = line.split('\t')
        frame = l[0]
        rgb = int(l[1])
        hsv = int(l[2])
        yiq = int(l[3])

        r = False
        h = False
        y = False

        if(rgb>rgb_th):
            r = True
        if(hsv>hsv_th):
            h = True
        if(yiq>yiq_th):
            y = True

        if r or h or y:
            print frame,
            if r:
                print 'RGB',
            if h:
                print 'HSV',
            if y:
                print 'YIQ',
            print ''
            


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage:'
        print 'python shot_detect.py diff_file_gen_by_histogram.py'
    else:
        main(sys.argv[1])
