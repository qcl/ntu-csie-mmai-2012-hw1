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
# then output diff to stdout
#
import sys,os,math,copy
import Image,colorsys

def main(path,start,end):

    if start > end:
        print 'index error (start>end)'
        return
    
    if not path[-1] == '/':
        path = path + '/'
   
    #rgb_h_f = open(path+'rgb_h','w')
    #hsv_h_f = open(path+'hsv_h','w')
    #yiq_h_f = open(path+'yiq_h','w')
    #diff_f  = open(path+'diff_h','w')

    last_rgb_h = None
    last_hsv_h = None
    last_yiq_h = None
    
    rgb_h = []
    hsv_h = []
    yiq_h = []
    l1d_rgb = []
    l1d_hsv = []
    l1d_yiq = []
    l2d_rgb = []
    l2d_hsv = []
    l2d_yiq = []
    for w in range(0,4):
        rgb_h.append([])
        hsv_h.append([])
        yiq_h.append([])
        l1d_rgb.append([])
        l1d_hsv.append([])
        l1d_yiq.append([])
        l2d_rgb.append([])
        l2d_hsv.append([])
        l2d_yiq.append([])

        for h in range(0,4):
            rgb_h[w].append([])
            hsv_h[w].append([])
            yiq_h[w].append([])
            l1d_rgb[w].append(0)
            l1d_hsv[w].append(0)
            l1d_yiq[w].append(0)
            l2d_rgb[w].append(0)
            l2d_hsv[w].append(0)
            l2d_yiq[w].append(0)

    
            # RGB histogram initialize
            for x in range(0,4):
                rgb_h[w][h].append([])
                for y in range(0,4):
                    rgb_h[w][h][x].append([])
                    for z in range(0,4):
                        rgb_h[w][h][x][y].append(0)

            # HSV histogram initialize
            for x in range(0,18):
                hsv_h[w][h].append([])
                for y in range(0,3):
                    hsv_h[w][h][x].append([])
                    for z in range(0,3):
                        hsv_h[w][h][x][y].append(0)

            # YIQ histogram initialize
            for x in range(0,12):
                yiq_h[w][h].append([])
                for y in range(0,3):
                    yiq_h[w][h][x].append([])
                    for z in range(0,3):
                        yiq_h[w][h][x][y].append(0)
            

    for frame in range(start,end+1):
        filename = path+str(frame)+'.jpg'
            
        
        if os.path.exists(filename):
            # read Image
            image = Image.open(filename)

            # resize image
            image = image.resize((320,240),Image.ANTIALIAS)
            
            # get image width and height
            width = image.size[0]
            height = image.size[1]

            


            # get pixel value from image
            image = image.convert('RGB')
           
            for x in range(0,width):
                for y in range(0,height):
                    
                    # get R,G,B value 
                    r,g,b = image.getpixel((x,y))

                    xr = x/80
                    yr = y/60

                    rgb_h[xr][yr][r/64][g/64][b/64] = rgb_h[xr][yr][r/64][g/64][b/64] + 1

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
                    hsv_h[xr][yr][h][s][v] = hsv_h[xr][yr][h][s][v] + 1

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
                    yiq_h[xr][yr][Y][I][Q] = yiq_h[xr][yr][Y][I][Q] + 1

            
            if last_rgb_h != None:
                for w in range(0,4):
                    for h in range(0,4):
                        for x in range(0,18):
                            for y in range(0,4):
                                for z in range(0,4):
                                    if x < 4:
                                        #Calculate L1/L2 for RGB
                                        diff = int(math.fabs(last_rgb_h[w][h][x][y][z]-rgb_h[w][h][x][y][z]))
                                        l1d_rgb[w][h] = l1d_rgb[w][h] + diff
                                        l2d_rgb[w][h] = l2d_rgb[w][h] + diff*diff
                                        last_rgb_h[w][h][x][y][z] = rgb_h[w][h][x][y][z]
                                        rgb_h[w][h][x][y][z] = 0
                                    if y < 3 and z < 3:
                                        #Calculate L1/L2 for HSV
                                        diff = int(math.fabs(last_hsv_h[w][h][x][y][z]-hsv_h[w][h][x][y][z]))
                                        l1d_hsv[w][h] = l1d_hsv[w][h] + diff
                                        l2d_hsv[w][h] = l2d_hsv[w][h] + diff*diff
                                        last_hsv_h[w][h][x][y][z] = hsv_h[w][h][x][y][z]
                                        hsv_h[w][h][x][y][z] = 0
                                        if x < 9:
                                            #Calculate L1/L2 for YIQ
                                            diff = int(math.fabs(last_yiq_h[w][h][x][y][z]-yiq_h[w][h][x][y][z]))
                                            l1d_yiq[w][h] = l1d_yiq[w][h] + diff
                                            l2d_yiq[w][h] = l2d_yiq[w][h] + diff*diff
                                            last_yiq_h[w][h][x][y][z] = yiq_h[w][h][x][y][z]
                                            yiq_h[w][h][x][y][z] = 0
            else:
                last_rgb_h = copy.deepcopy(rgb_h)
                last_hsv_h = copy.deepcopy(hsv_h)
                last_yiq_h = copy.deepcopy(yiq_h)
                for w in range(0,4):
                    for h in range(0,4):
                        for x in range(0,18):
                            for y in range(0,4):
                                for z in range(0,4):
                                    if x < 4 :
                                        rgb_h[w][h][x][y][z] = 0
                                    if y < 3 and z < 3:
                                        hsv_h[w][h][x][y][z] = 0
                                        if x < 9:
                                            yiq_h[w][h][x][y][z] = 0

            print filename,
           
            for w in range(0,4):
                for h in range(0,4):
                    print l1d_rgb[w][h],l1d_hsv[w][h],l1d_yiq[w][h],l2d_rgb[w][h],l2d_hsv[w][h],l2d_yiq[w][h],
                    l1d_rgb[w][h]=0
                    l1d_hsv[w][h]=0
                    l1d_yiq[w][h]=0
                    l2d_rgb[w][h]=0
                    l2d_hsv[w][h]=0
                    l2d_yiq[w][h]=0
            
            print ''
            #diff_f.write(filename+'\t'+str(diff_rgb)+'\t'+str(diff_hsv)+'\t'+str(diff_yiq)+'\n')

        else:
            pass
            #print filename,'do not exist'
    
    #rgb_h_f.close()
    #hsv_h_f.close()
    #yiq_h_f.close()
    #diff_f.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: python histogram.py frame_dir 1st# last#'
        print 'e.g.'
        print 'python histogram.py videos.hw01/01_frame 0 828'
    else:
        main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
