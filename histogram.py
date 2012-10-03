# -*- coding:utf-8 -*-
# Qing-Cheng Li
# R01922024
#
# qingcheng.li@qcl.tw / r01922024@csie.ntu.edu.tw
#
# MMAI 2012 Homework#1
#
import sys
import Image,colorsys

def main():
    print 'main'

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: python histogram.py frame_dir 1st# last#'
        print 'e.g.'
        print 'python histogram.py videos.hw01/01_frame 0 828'
    else:
        main()
