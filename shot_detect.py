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

    rgb_th = 20000
    hsv_th = 38000
    yiq_th = 20000

    rgb = []
    hsv = []
    yiq = []
    path = []

    shot_h = []
    shot_r = []
    shot_y = []

    cur_s_h = -1
    cur_e_h = -1

    cur_s_r = -1
    cur_e_r = -1

    cur_s_y = -1
    cur_e_y = -1

    ws = 5

    for line in df:
        l = line.split('\t')
        path.append(l[0])
        rgb.append(int(l[1]))
        hsv.append(int(l[2]))
        yiq.append(int(l[3]))

    for i in range(0,len(rgb)):
        
        if hsv[i]>hsv_th:
            if i > cur_e_h and i > cur_s_h:
                cur_s_h = i
                k = i + ws
            
                if k > len(rgb):
                    k = len(rgb)

                for j in range(i,k):
                    if hsv[j] > hsv_th and j > cur_e_h:
                        cur_e_h = j
          
            if i == cur_e_h:
                e = False
                k = i + ws
                if k > len(rgb):
                    k = len(rgb)
                
                for j in range(i,k):
                    if hsv[j] > hsv_th and j > cur_e_h:
                        e = True
                        cur_e_h = j

                if not e:
                    shot_h.append((cur_s_h,cur_e_h))
         
        if rgb[i]>rgb_th:
            if i > cur_e_r and i > cur_s_r:
                cur_s_r = i
                k = i + ws
            
                if k > len(rgb):
                    k = len(rgb)

                for j in range(i,k):
                    if rgb[j] > rgb_th and j > cur_e_r:
                        cur_e_r = j
          
            if i == cur_e_r:
                e = False
                k = i + ws
                if k > len(rgb):
                    k = len(rgb)
                
                for j in range(i,k):
                    if rgb[j] > rgb_th and j > cur_e_r:
                        e = True
                        cur_e_r = j

                if not e:
                    shot_r.append((cur_s_r,cur_e_r))
         
        if yiq[i]>yiq_th:
            if i > cur_e_y and i > cur_s_y:
                cur_s_y = i
                k = i + ws
            
                if k > len(rgb):
                    k = len(rgb)

                for j in range(i,k):
                    if yiq[j] > yiq_th and j > cur_e_y:
                        cur_e_y = j
          
            if i == cur_e_y:
                e = False
                k = i + ws
                if k > len(rgb):
                    k = len(rgb)
                
                for j in range(i,k):
                    if yiq[j] > yiq_th and j > cur_e_y:
                        e = True
                        cur_e_y = j

                if not e:
                    shot_y.append((cur_s_y,cur_e_y))
         
    lh = len(shot_h)
    lr = len(shot_r)
    ly = len(shot_y)

    for i in range(0,max(lh,max(lr,ly))):
        if i < lh:
            print shot_h[i],'\t',
        else:
            print "       ",'\t',

        if i < lr:
            print shot_r[i],'\t',
        else:
            print "       ",'\t',

        if i < ly:
            print shot_y[i]
        else:
            print "       "

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage:'
        print 'python shot_detect.py diff_file_gen_by_histogram.py answer'
    else:
        main(sys.argv[1],"")
