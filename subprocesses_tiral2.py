#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import subprocess
import threading
import locale
import sys
import os

locale.setlocale (locale.LC_ALL, '')

class ExecuteBackground (threading.Thread):  # threading.Threadを継承
  """
  プロセスをバックグラウンドで実行する
  Threadクラスの子クラスとして定義(__init__()とrun()をオーバーライドして使用)
  threading.Thread.__init__(self)の呼び出しは必須
  """
  def __init__ (self, **dic):
    """
    オブジェクトの初期化
    """
    threading.Thread.__init__ (self)  # 必ず呼び出す
    self._id = dic['id']
    self._args = dic['cmd']
    self._subproc_args = { 'stdin'     : subprocess.PIPE,
                           'stdout'    : subprocess.PIPE,
                           'stderr'    : subprocess.STDOUT,
                           'cwd'       : dic['cwd'],
                           'close_fds' : True,              }

  def run (self):
    """
    スレッド内で行われる処理を記述
    """
    try:
      p = subprocess.Popen (self._args, **self._subproc_args)
    except OSError as e:
      print ('Failed to execute command "{0}": [{1}] {2}'.format (self._args[0], e.errno, e.strerror), file=sys.stderr)
      return
    (stdouterr, stdin) = (p.stdout, p.stdin)
    print ('-- output [{0}] begin --'.format (self._id))
    if sys.version_info.major == 3:
      while True:
        line = str (stdouterr.readline (), encoding='utf-8')
        #line = stdouterr.readline ().decode ('utf-8')  # decode()を用いる場合
        if not line:
          break
        print (line.rstrip ())
    else:
      while True:
        line = stdouterr.readline ()
        if not line:
          break
        print (line.rstrip ())
    print ('-- output [{0}] end --'.format (self._id))
    ret = p.wait ()
    print ('[{0}] Return code: {1}'.format (self._id, ret))

# クラス定義ここまで

os.environ['PATH'] = '/bin:/usr/bin'

cwd = '/'
# 5秒間停止するだけで何も出力しない
dic1 = { 'id'  : 1,
         'cmd' : ['sleep', '5'],
         'cwd' : cwd, }
# 毎秒数字を出力(後に終了)
dic2 = { 'id'  : 2,
         'cmd' : ['bash', '-c', 'for ((i = 1; i <= 5; i++)); do echo "Thread 2: $i"; sleep 1; done'],
         'cwd' : cwd, }
# 1秒間に2つの数字を出力(先に終了)
dic3 = { 'id'  : 3,
         'cmd' : ['bash', '-c', 'for ((i = 1; i <= 5; i++)); do echo "Thread 3: $i"; sleep 0.5; done'],
         'cwd' : cwd, }


cmd1 = ExecuteBackground (**dic1)
print ('before cmd1.start()')
cmd1.start ()  # run()を呼び出す
print ('after cmd1.start()')
print ('before cmd1.join() waiting...')
cmd1.join ()
print ('after cmd1.join()')

cmd2 = ExecuteBackground (**dic2)
print ('before cmd2.start()')
cmd2.start ()
print ('after cmd2.start()')
cmd3 = ExecuteBackground (**dic3)
print ('before cmd3.start()')
cmd3.start ()
print ('after cmd3.start()')
