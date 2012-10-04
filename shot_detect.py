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

    for line in df:
        l = line.split('\t')
        frame = l[0]
        rgb = int(l[1])
        hsv = int(l[2])
        yiq = int(l[3])

        if(rgb>rgb_th):
            print frame


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage:'
        print 'python shot_detect.py diff_file_gen_by_histogram.py'
    else:
        main(sys.argv[1])
