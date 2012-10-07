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
# detect shot boundary.
import sys,os,math
import histogram

def main(argv):

    path = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    color_space = sys.argv[4]
    
    cache = False
    threshold = 40000

    if len(sys.argv)>5:
        for i in range(5,len(sys.argv)):
            if sys.argv[i] == '-c':
                cache = True
            elif sys.argv[i] == '-t':
                threshold = int(sys.argv[i+1])

    # check cache
    if not os.path.exists(path+color_space+'_frameDiff'):
        cache = True

    # get frames difference
    frames = histogram.getFramesDifference(path,start,end,color_space,cache)

    # check result.
    if len(frames) != 2:
        print 'no frames'
        return
    else:
        frameDiff = frames['frameDiff']
        frameID   = frames['frameID']

    shot = []
    windowSize = 5
    status = 0      #NotFound
    w = 0

    startFrame = -1
    endFrame = -1

    for i in range(0,len(frameDiff)):
        if frameDiff[i] > threshold:
            w = windowSize
            
            #each difference > threshold may be the end of transition
            endFrame = i        
            
            if status == 0:
                status = 1      #Start of transition
                startFrame = i
        else:
            if status == 1:
                if w > 0:
                    w = w - 1
                else:
                    status = 0  #Find a transition!
                    shot.append((startFrame,endFrame))
    
    # get the last transition
    if status == 1:
        shot.append((startFrame,endFrame))
    
    # calculate the real boundary
    shotStart = [0]

    # if diff < noChangeThreshold, there is almost no change between
    # frame i & i+1
    noChangeThreshold = 100

    # If it's a cut:
    #      
    #      .
    #      ..
    # -------------- threshold
    # .  . .. .. 
    # ............
    # .............
    #      *--------> shot boundary
    #

    # If it's fade transition:
    #       
    #       .  .
    #   .   .  .
    # -------------- threshold
    #   .  ..  .  .
    # -------------- noChangeIndex
    # .......  .....
    # ..............
    #         *--------> I think here is shot boundary 

    # So I use the method below to find it.

    for transition in shot:
        maxDiff = 0
        maxDiffIndex = transition[0]
        noChangeIndex = -1

        for i in range(transition[0],transition[1]+1):
            # Find the max diff
            if frameDiff[i] > maxDiff:
                maxDiff = frameDiff[i]
                maxDiffIndex = i
            # Or the no change frame -> usually Fade in black
            if frameDiff[i] < noChangeThreshold:
                noChangeIndex = i

        if noChangeIndex > 0:
            boundaryIndex = noChangeIndex + 1
        else:
            boundaryIndex = maxDiffIndex

        shotStart.append(boundaryIndex)

    # Append the last frame into list
    shotStart.append(len(frameID))

    print ''
    print 'Frame path:',path
    print 'From frame#'+str(frameID[0])+' to #'+str(frameID[-1])
    print 'Using ',color_space
    print 'Threshold',threshold

    print ''
    print 'Shot Boundaries'
    for i in range(1,len(shotStart)-1):
        print frameID[shotStart[i]]
    print ''
    print 'Shot:'
    for i in range(0,len(shotStart)-1):
        print 'Shot #%03d frame #%04d - #%04d' % (i+1,frameID[shotStart[i]],frameID[shotStart[i+1]-1])

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print 'Usage:'
        print 'python shot_detect.py frame_dir start_frame end_frame color_space (-t threshold) (-c)'
        print 'e.g.'
        print 'python shot_detect.py videos.hw01/01_frame 0 828 hsv'
        print 'or'
        print 'python shot_detect.py videos.hw01/01_frame 0 828 hsv -t 40000'
        print 'or'
        print 'python shot_detect.py videos.hw01/01_frame 0 828 hsv -t 40000 -c'
        print 'or'
        print 'python shot_detect.py videos.hw01/01_frame 0 828 hsv -c'
    else:
        main(sys.argv)
