# We import the expect library for python
import telnetlib
import sys
import csv
import time
import threading

# --- Timers
TimeLogin = 10
TelnetWriteTimeout = 1
TelnetReadTimeout = 2
# --- CSV
FileCsv = "/home/lucas/Documents/script/file.csv"
# --- Extras
cr="\n"

# variables
IP = "A.B.C.D"
User = ["user","password"]
CliLogin = "telnet " + IP
Prompt = ["root@host.*]#"]
PromptLogin = ["login:"]
PromptLogout = ["logout"]
PromptPass = ["Password:"]
CliLine = "ls -l"

class MiThread(threading.Thread):  
    def __init__(self,num,datos):  
        threading.Thread.__init__(self)
        self.num = num
        self.datos = datos
        self.systemIP = self.datos[0]
        self.tn = telnetlib.Telnet(IP)
        self.tn.timeout = TimeLogin

        # File declaration
        self.FileOutGen = self.systemIP + "_commands"
        self.FileOutSend = self.systemIP + "_output"
        self.FileOutRx = self.systemIP + "_rx"      
        self.fg = open(self.FileOutGen,"w")
        self.fr = open(self.FileOutRx,"a")
        self.fs = open(self.FileOutSend,"w")

    def run(self):  
        print "Soy el hilo", self.num
        self.telnetLogin()
        self.runLs()
        self.telnetLogout()

    def telnetLogin(self):      
        i=self.tn.expect(PromptLogin)
        print i
        if i:
            writeTelnet(User[0],TelnetWriteTimeout)
            j=self.tn.expect(PromptPass)
            print j
            if j:
                writeTelnet(User[1],TelnetWriteTimeout)

    def telnetLogout(self):
        i=self.tn.expect(Prompt)
        if i:
            writeTelnet("exit",TelnetWriteTimeout)
            j=self.tn.expect(PromptLogout)
            if j:
                print "Logged out OK from SAM"

    def runLs(self):
        writeLog("Prueba de Ls " + self.systemIP)
        self.writeCsv(self.systemIP,1)
        i=self.tn.expect(Prompt,TimeLogin)
        print i
        if i:
            # Prompt
            CliLine = "ls -l "
            writeTelnet(CliLine,TelnetWriteTimeout)

    def writeCsv(self,inText,lastIn):
        lock.acquire(1)
        if lastIn==0:
            fc.write(inText + ",")
        elif lastIn==1:
            fc.write(inText + "\n")
        lock.release()

def writeTelnet(inText, timer):
    tn.write(inText + cr)
    time.sleep(timer)

def writeLog(inText):
    print (inText)
    t.fs.write("\n" + inText)

def printConsole(inText):
    print (inText)

oFile = csv.reader(open(FileCsv,"r"), delimiter=",", quotechar="|")

lock = threading.Lock()
routers = list(oFile)
threads_list = []

for i in range(len(routers)):
    FileOutCsv = "00_log.csv"

    # creating output file
    fc = open(FileOutCsv,"a")

    # running routine
    t = MiThread(i,routers[i])
    threads_list.append(t)
    t.start()
