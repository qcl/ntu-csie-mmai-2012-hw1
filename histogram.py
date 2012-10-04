# -*- coding:utf-8 -*-
# Qing-Cheng Li
# R01922024
#
# qingcheng.li@qcl.tw / r01922024@csie.ntu.edu.tw
#
# MMAI 2012 Homework#1
#
# histogram.py 
# read frame image, then calculate RGB, HSV, YIQ histogram, 
# then output as files
#
import sys,os,math,copy
import Image,colorsys

def main(path,start,end):

    if start > end:
        print 'index error (start>end)'
        return
    
    if not path[-1] == '/':
        path = path + '/'
   
    rgb_h_f = open(path+'rgb_h','w')
    hsv_h_f = open(path+'hsv_h','w')
    yiq_h_f = open(path+'yiq_h','w')
    diff_f  = open(path+'diff_h','w')

    last_rgb_h = None
    last_hsv_h = None
    last_yiq_h = None
    
    # RGB histogram initialize
    rgb_h = []
    for x in range(0,4):
        rgb_h.append([])
        for y in range(0,4):
            rgb_h[x].append([])
            for z in range(0,4):
                rgb_h[x][y].append(0)

    # HSV histogram initialize
    hsv_h = []
    for x in range(0,18):
        hsv_h.append([])
        for y in range(0,3):
            hsv_h[x].append([])
            for z in range(0,3):
                hsv_h[x][y].append(0)

    # YIQ histogram initialize
    yiq_h = []
    for x in range(0,12):
        yiq_h.append([])
        for y in range(0,3):
            yiq_h[x].append([])
            for z in range(0,3):
                yiq_h[x][y].append(0)
            

    for frame in range(start,end+1):
        filename = path+str(frame)+'.jpg'
            
        
        if os.path.exists(filename):
            # read Image
            image = Image.open(filename)
            
            # get image width and height
            width = image.size[0]
            height = image.size[1]

            


            # get pixel value from image
            image = image.convert('RGB')
           
            for x in range(0,width):
                for y in range(0,height):
                    
                    # get R,G,B value 
                    r,g,b = image.getpixel((x,y))
                    rgb_h[r/64][g/64][b/64] = rgb_h[r/64][g/64][b/64] + 1

                    # get H,S,V
                    r = r/float(255)
                    g = g/float(255)
                    b = b/float(255)

                    h,s,v = colorsys.rgb_to_hsv(r,g,b)
                    h = h*18
                    s = s*3
                    v = v*3
                    if h >= 18.0:
                        h = 17
                    if s >= 3.0:
                        s = 2
                    if v >= 3.0:
                        v = 2
                    h = int(h)
                    s = int(s)
                    v = int(v)
                    hsv_h[h][s][v] = hsv_h[h][s][v] + 1

                    # get Y,I,Q
                    Y,I,Q = colorsys.rgb_to_yiq(r,g,b)
                    Y = Y*12
                    I = (I+0.5957)*3/(0.5957*2) 
                    Q = (Q+0.5226)*3/(0.5226*2)
                    if Y >= 12.0:
                        Y = 11
                    if I >= 3.0:
                        I = 2
                    if Q >= 3.0:
                        Q = 2
                    Y = int(Y)
                    I = int(I)
                    Q = int(Q)
                    yiq_h[Y][I][Q] = yiq_h[Y][I][Q] + 1

            
            #Calculate L1 for RGB
            diff_rgb = 0
            if last_rgb_h!=None:
                for x in range(0,4):
                    for y in range(0,4):
                        for z in range(0,4):
                            #rgb_h_f.write(str(rgb_h[x][y][z])+',')
                            print last_rgb_h[x][y][z],rgb_h[x][y][z]
                            diff_rgb = diff_rgb + math.fabs(last_rgb_h[x][y][z]-rgb_h[x][y][z])
                            last_rgb_h[x][y][z] = rgb_h[x][y][z]
                            rgb_h[x][y][z] = 0
                            

             
            #rgb_h_f.write("\n")
            
            #Calculate L1 for HSV
            diff_hsv = 0
            if last_hsv_h!=None:
                for x in range(0,18):
                    for y in range(0,3):
                        for z in range(0,3):
                            #hsv_h_f.write(str(hsv_h[x][y][z])+',')
                            diff_hsv = diff_hsv + math.fabs(last_hsv_h[x][y][z]-hsv_h[x][y][z])
                            last_hsv_h[x][y][z] = hsv_h[x][y][z]
                            hsv_h[x][y][z] = 0
             
            #hsv_h_f.write("\n")

            #Calculate L1 for YIQ
            diff_yiq = 0
            if last_yiq_h!=None:
                for x in range(0,12):
                    for y in range(0,3):
                        for z in range(0,3):
                            #yiq_h_f.write(str(yiq_h[x][y][z])+',')
                            diff_yiq = diff_yiq + math.fabs(last_yiq_h[x][y][z]-yiq_h[x][y][z])
                            last_yiq_h[x][y][z] = yiq_h[x][y][z]
                            yiq_h[x][y][z] = 0
             
            #yiq_h_f.write("\n")

            if last_rgb_h == None:
                last_rgb_h = copy.deepcopy(rgb_h)
                last_hsv_h = copy.deepcopy(hsv_h)
                last_yiq_h = copy.deepcopy(yiq_h)
                print last_rgb_h

            print filename,diff_rgb,diff_hsv,diff_yiq
            #diff_f.write(filename+'\t'+str(diff_rgb)+'\t'+str(diff_hsv)+'\t'+str(diff_yiq)+'\n')

        else:
            print filename,'do not exist'
    
    rgb_h_f.close()
    hsv_h_f.close()
    yiq_h_f.close()
    diff_f.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: python histogram.py frame_dir 1st# last#'
        print 'e.g.'
        print 'python histogram.py videos.hw01/01_frame 0 828'
    else:
        main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
