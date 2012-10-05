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

def main(difffile,answer):
    df = open(difffile,'r')
    #df = open(answer,'r')

    rgb_th = 10000
    hsv_th = 40000
    yiq_th = 20000

    rgb = []
    hsv = []
    yiq = []
    path = []

    shot = []

    cur_s = -1
    cur_e = -1

    ws = 5

    for line in df:
        l = line.split('\t')
        path.append(l[0])
        rgb.append(int(l[1]))
        hsv.append(int(l[2]))
        yiq.append(int(l[3]))

    for i in range(0,len(rgb)):
        
        if hsv[i]>hsv_th:
            if i > cur_e and i > cur_s:
                cur_s = i
                k = i + ws
            
                if k > len(rgb):
                    k = len(rgb)

                for j in range(i,k):
                    if hsv[j] > hsv_th and j > cur_e:
                        cur_e = j
          
            if i == cur_e:
                e = False
                k = i + ws
                if k > len(rgb):
                    k = len(rgb)
                
                for j in range(i,k):
                    if hsv[j] > hsv_th and j > cur_e:
                        e = True
                        cur_e = j

                if not e:
                    shot.append((cur_s,cur_e))
         

    for pair in shot:
        print pair
        #r = False
        #h = False
        #y = False

        #if(rgb>rgb_th):
        #    r = True
        #if(hsv>hsv_th):
        #    h = True
        #if(yiq>yiq_th):
        #    y = True

        #if r or h or y:
        #    print frame,
        #    if r:
        #        print 'RGB',
        #    if h:
        #        print 'HSV',
        #    if y:
        #        print 'YIQ',
        #    print ''
            


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage:'
        print 'python shot_detect.py diff_file_gen_by_histogram.py answer'
    else:
        main(sys.argv[1],"")
