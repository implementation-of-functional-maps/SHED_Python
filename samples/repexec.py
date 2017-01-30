# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: repexec.py
#                       Last Change : 2016-10-14
#                       Editted by : Katsurou Takahashi
######################################################################

######################################################################
#                       Import
######################################################################
import time,sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import check as ck # check, time stamp, demo, help

######################################################################
#                       Method
######################################################################
def main(cmd, inc=60):
    ''' コマンドcmd の反復実行。ただし、「Ctl+C」 でないと停止できない。''' 
    while True:
        os.system(cmd)
        time.sleep(inc)
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return None

######################################################################
#                           Main
######################################################################
if __name__ == '__main__':
    #ck.main(test, 10) 
    # (exec_func, *inputs)
    numargs = len(sys.argv) - 1 # nargin と同じ...
    if numargs < 1 or numargs > 2:
        print("usage:"+ sys.argv[0] +" command [seconds_delay]")
        sys.exit(1)
    cmd = sys.argv[1]
    if numargs < 2:
        main(cmd)
    else:
        inc = int(sys.argv[2])
        main(cmd, inc)
        
######################################################################
#                           END
######################################################################
# chekced
