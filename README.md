# data_recording-in-inflab
to record the time-delay and the download speed of some website
there will be some explanations for the python programs
example pingscript:it has two parameters.the first is website and the second is the data document
        python pingscript.py www.baidu.com data/baidu
example loopdownload:it has two parameters.the first is video website and the second is output . it will download the video from website 
                     like youku,bilibili and then delete the video again and again
        python loopdownload.py https://www.bilibili.com/bangumi/play/ep84776?from=search ./tmp/bb
example allrate:it has one parameter as the output of the download speed data and it will calculate all the the download speed 
                in the directory by measuring the size of every document
        python allrate.py downloaddata.txt
example clean_specially:it has one parameter .usually used when debuging and delete the .download document
        python clean.py ./tmp/bb
