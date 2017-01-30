# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: schedexec.py
#                       Last Change : 2016-10-14
#                       Editted by : Katsurou Takahashi
######################################################################

######################################################################
#                       Import
######################################################################
import time,sys,os,sched # relative import 
sys.path.append(os.pardir) # relative import 
import check as ck # check, time stamp, demo, help

######################################################################
#                       Method
######################################################################
def main(cmd, inc=60):
    ''' コマンドcmd の予定実行。ただし、「Ctl+C」 でないと停止できない。'''
    schedule = sched.scheduler(time.time, time.sleep)
    def perform_command(cmd, inc):
        schedule.enter(inc, 0, perform_command, (cmd, inc)) #
        os.system(cmd)
        #-----------------------------------------------------------------
        #                       Return
        #-----------------------------------------------------------------
        return None
    def main(cmd, inc=60):
        schedule.enter(0,0,perform_command, (cmd, inc)) # 0 は今すぐ
        schedule.run()
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
