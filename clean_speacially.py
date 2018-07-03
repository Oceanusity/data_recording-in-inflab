import os
import time
import fnmatch
import sys

def clean(dirname):
    workdir = os.getcwd()
    fullname = os.path.join(workdir,dirname)
    if os.path.exists(fullname):
        for videoname in os.listdir(fullname):
            print videoname
            if os.path.getsize(os.path.join(fullname,videoname)) > 1000 :
                os.remove(os.path.join(fullname,videoname))
    else :
        print "dir not exits"
if __name__ == '__main__':
    dirname = ""
    dirname = sys.argv[1]
    if(dirname == "./tmp/bb" or dirname  =="./tmp/qq" or dirname == "./tmp/iqiyi" or dirname == "./tmp/youku"):
        time.sleep(10)
        clean(dirname)
    else:
        print("input dirname such as ./tmp/bb")