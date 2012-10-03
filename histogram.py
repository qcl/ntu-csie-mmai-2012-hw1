# -*- coding:utf-8 -*-
# Qing-Cheng Li
# R01922024
#
# qingcheng.li@qcl.tw / r01922024@csie.ntu.edu.tw
#
# MMAI 2012 Homework#1
#
import sys,os
import Image,colorsys

def main(path,start,end):
    
    if start > end:
        print 'index error (start>end)'
        return
    
    if not path[:-1] == '/':
        path = path + '/'
   
    rgb_h_f = open(path+'rgb_h','w')

    for i in range(start,end+1):
        filename = path+str(i)+'.jpg'
        
        if os.path.exists(filename):
            # read Image
            image = Image.open(filename)
            
            # get image width and height
            width = image.size[0]
            height = image.size[1]

            

            # histogram
            rgb_h = []
            for x in range(0,4):
                rgb_h.append([])
                for y in range(0,4):
                    rgb_h[x].append([])
                    for z in range(0,4):
                        rgb_h[x][y].append(0)

                                    
            

            # get pixel value from image
            image = image.convert('RGB')
            
            for x in range(0,width):
                for y in range(0,height):
                    
                    # get R,G,B value 
                    r,g,b = image.getpixel((x,y))
                    rgb_h[r/64][g/64][b/64] = rgb_h[r/64][g/64][b/64] + 1

            print filename
            
            for x in range(0,4):
                for y in range(0,4):
                    for z in range(0,4):
                        rgb_h_f.write(str(rgb_h[x][y][z])+',')
            
            rgb_h_f.write("\n")



        else:
            print filename,'do not exist'
    
    rgb_h_f.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: python histogram.py frame_dir 1st# last#'
        print 'e.g.'
        print 'python histogram.py videos.hw01/01_frame 0 828'
    else:
        main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
