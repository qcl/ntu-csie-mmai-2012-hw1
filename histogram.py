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
# then return frames difference
#
import sys,os,math,copy
import Image,colorsys

debug = False

def getFramesDifference(path,start,end,color_space='hsv',cache=False):
    """
    Get frames difference for frames in `path` 
    from `start` to `end` for color space `color_space`.

    This function will return {'frameDiff':[],'frameID':[]}
    """

    #Check index
    if start > end:
        print 'index error (start>end)'
        return {}
   
    #Check color space
    color_space = color_space.lower()
    if not color_space in ['hsv','rgb','yiq']:
        print 'Unknow color space',color_space
        return {}

    #Check path
    if not path[-1] == '/':
        path = path + '/'


    frameDiff = []
    frameID   = []

    # save the result
    cacheFilename = path+color_space+'_frameDiff'
    if cache:
        of = open(cacheFilename,'w')
    
    elif os.path.exists(cacheFilename):
        # if cache file exists, read it then return.
        print 'reading cache'
        histogramf = open(cacheFilename,'r')

        for line in histogramf:
            l = line.split()
            frameID.append(int(l[0]))
            frameDiff.append(int(l[1]))

        histogramf.close()
    
        return {'frameDiff':frameDiff,'frameID':frameID}

    else:
        pass
        # no cache file.

    # output histograms for debug
    if debug:
        dbgFilename = path+color_space+'_histogram'
        dbgf = open(dbfDBGFilename,'w')

    
    histo = []              # histogram of current image
    last_histogram = None   # histogram of last image

    X,Y,Z = (18,3,3)    #default is H,S,V
    if color_space == 'rgb':
        X,Y,Z = (4,4,4) #R,G,B
    elif color_space == 'yiq':
        X,Y,Z = (9,3,3) #Y,I,Q

    #initialize
    for x in range(0,X):
        histo.append([])
        for y in range(0,Y):
            histo[x].append([])
            for z in range(0,Z):
                histo[x][y].append(0)


    # Start read frames
    for frame in range(start,end+1):
        filename = path+str(frame)+'.jpg'
            
        if os.path.exists(filename):

            print 'reading',filename
            
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

                    if color_space == 'rgb':
                        histo[r/64][g/64][b/64] = histo[r/64][g/64][b/64] + 1
                    else:
                        r = r/float(255)
                        g = g/float(255)
                        b = b/float(255)

                        # get H,S,V/Y,I,Q
                        if color_space == 'hsv':
                            a,b,c = colorsys.rgb_to_hsv(r,g,b)
                        else:
                            a,b,c = colorsys.rgb_to_yiq(r,g,b)
                        
                        a = a*X
                        b = b*Y
                        c = c*Z

                        if a >= float(X):
                            a = X-1
                        if b >= float(Y):
                            b = Y-1
                        if c >= float(Z):
                            c = Z-1

                        a = int(a)
                        b = int(b)
                        c = int(c)

                        # build histogram
                        histo[a][b][c] = histo[a][b][c] + 1

            # calculate frame difference
            diff = 0
            
            if debug:
                dbgf.write(str(frame))
            
            if last_histogram != None:
                for x in range(0,X):
                    for y in range(0,Y):
                        for z in range(0,Z):
                            # L1 
                            diff = diff + abs(histo[x][y][z]-last_histogram[x][y][z])
                            if debug:
                                dbgf.write(','+str(histo[x][y][z]))

                            # copy histogram to last_histogram
                            last_histogram[x][y][z] = histo[x][y][z]
                            # clear histogram
                            histo[x][y][z] = 0

            else:
                # copy histogram to last_histogram
                last_histogram = copy.deepcopy(histo)

                # clear histogram
                for x in range(0,X):
                    for y in range(0,Y):
                        for z in range(0,Z):
                            if debug:
                                dbgf.write(','+str(histo[x][y][z]))
                            histo[x][y][z] = 0
            
            if debug:
                dbgf.write('\n')

            frameID.append(frame)
            frameDiff.append(diff)

            if cache:
                of.write(str(frame)+' '+str(diff)+'\n')

        else:
            pass
            print filename,'do not exist'
    
    if cache:
        of.close()
    if debug:
        dbgf.close()

    return {'frameDiff':frameDiff,'frameID':frameID}

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print 'Usage: python histogram.py frame_dir 1st# last# color_space (cache)'
        print 'e.g.'
        print 'python histogram.py videos.hw01/01_frame 0 828 hsv'
        print 'or if you want to build cache file:'
        print 'python histogram.py videos.hw01/01_frame 0 828 hsv cache'
    else:
        if len(sys.argv) > 5:
            getFramesDifference(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],True)
        else: 
            getFramesDifference(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4])
