#!/usr/bin/python
'''
calucate the rate of download video from bb qq ...
the method  is
pre : previous size of dir eg tmp/qq
now : now size of dir eg tmp/qq
rate : (now - pre) / 5
'''
#cal all the doc in the tmp dir and tmp must in the 
import os
import time
import fnmatch
import sys
def dirsize(path):
    size = 0
    for root,dirnames,filenames in os.walk(path):
        for filename in filenames:
            size = size + os.path.getsize(os.path.join(root,filename))
    return size

def cal(path,pre):
    now = dirsize(path)
    return now, (now - pre) / 5

if __name__ == '__main__':
    datafile = ""
    if ( len(sys.argv) < 2 ):
        print (" missing datafile\n example:python allrate.py downloaddata\n")
        exit()
    datafile = sys.argv[1]
    workdir = os.path.join(os.getcwd(),"./tmp") #can be changed to input by keyboard
    presize = [0 for x in range(0, 20)]
    nowsize = [0 for x in range(0, 20)]     #max<20
    for document in os.listdir(workdir):  
        count = 0
        presize[count] = dirsize(os.path.join( workdir , document))
        count = count + 1
    try:
        while True:
            f = open( datafile ,"a")
            t = time.strftime("%m-%d %H:%M:%S", time.localtime())
            count = 0
            for document in os.listdir( workdir ): 
                path = os.path.join( workdir , document )
                nowsize[count] , rate = cal( path , presize[count] )
                f.write(t + "\n")
                f.write( document + ":" + str( rate ) + "\n")
                presize[count] = nowsize[count]
                count = count + 1
            time.sleep(5)
    except:
        KeyboardInterrupt
    finally:
        f.close()
