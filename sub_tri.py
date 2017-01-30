import subprocess, time, os, sys                                                        
import logging                                                                          
import numpy as np                                                                      
import random                                                                           
import threading                                                                        
import Queue                                                                            
                                                                                        
q = Queue.Queue()                                                                       
                                                                                        
n = 3                                                                                   
workspace = np.zeros((n, n))                                                            
for i in range(n):                                                                      
    for j in range(i):                                                                  
        workspace[i,j] = 4                                                              
                                                                                        
helloes = [ [ None for i in range(n)] for j in range(n)]                                
t = threading.Thread                                                                    
worker_servers = {"mcs01": 2} # 2  = "Vacant"                                           
worker_servers.update({"mcs02": 2})                                                     
worker_servers.update({"mcs03": 2})                                                     
                                                                                        
def worker(i,j):                                                                        
    """thread worker function"""                                                        
    outputs = []                                                                        
    cmd = [sys.executable, 'say_hello.py', str(i), str(j)]                              
    p = subprocess.Popen(cmd,                                                           
                         stdout=subprocess.PIPE,                                        
                         stderr=subprocess.STDOUT)                                      
    helloes[i][j] = p.stdout.read()                                                     
    time.sleep(1)                                                                       
    print(p.stdout.read())                                                              
    return helloes[i][j]                                                                
                                                                                        
def hello():                                                                            
    return None                                                                         
                                                                                        
def rlogin_worker_server(workspace, worker_servers, i, j, k):                           
    from operator import itemgetter                                                     
    if max(worker_servers.values()) != 1 and workspace[i,j] != 4:                       
        login_server = max(worker_servers.items(), key=itemgetter(1))[0]                
        print(login_server)                                                             
        cmd3 = ['rlogin', login_server]                                                 
        p = subprocess.Popen(cmd3, shell=False)                                         
        worker_servers[login_server] = 1                                                
        workspace[i,j] = 1                                                              
        t = threading.Thread(target=worker, args=(i,j))                                 
        workspace[i,j] = 2                                                              
        k += 1                                                                          
        cmd4 = ['exit']                                                                 
        p_end = subprocess.Popen(cmd4, shell=True)                                      
        time.sleep(1)                                                                   
        # q.put(k)                                                                      
        return [workspace, worker_servers, k, t]                                        
    elif max(worker_servers.values()) != 1 and workspace[i,j] == 4:                     
        k += 1                                                                          
        t = threading.Thread(target=hello)                                              
        time.sleep(1)                                                                   
        # q.put(k)                                                                      
        return [workspace, worker_servers, k, t]                                        
    else:                                                                               
        ind2 = random.randint(0,2)                                                      
        servers = ["mcs01", "mcs02", "mcs03"]                                           
        server = servers[ind2]                                                          
        worker_servers[server] = 2                                                      
        t = threading.Thread(target=hello)                                              
        time.sleep(1)                                                                   
        # q.put(k)                                                                      
        return [workspace, worker_servers, k, t]                                        
                                                                                        
k = 0                                                                                   
i = 0                                                                                   
j = 0                                                                                   
outputs = []                                                                            
threads = []                                                                            
while np.min(workspace) == 0.0:                                                         
    i = k // n                                                                          
    j = (n-1) - (k % n )                                                                
    print("i, j:",i,j)                                                                  
    [workspace, worker_servers, k, t] = rlogin_worker_server(workspace, worker_servers, i, j, k)                                                                               
    threads.append(t)                                                                   
    t.start()                                                                           
    time.sleep(3)                                                                       
    print(helloes)                                                                      

