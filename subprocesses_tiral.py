#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import subprocess
import threading
import locale
import sys
import os

locale.setlocale (locale.LC_ALL, '')

def func (**dic):
  """
  スレッド内で実行される処理を記述した関数
  id  : 表示中の識別用番号
  cmd : 「コマンド + 引数」のリスト
  cwd : 作業ディレクトリ
  """
  id       = dic['id']
  argslist = dic['cmd']
  subproc_args = { 'stdin'     : subprocess.PIPE,
                   'stdout'    : subprocess.PIPE,
                   'stderr'    : subprocess.STDOUT,
                   'cwd'       : dic['cwd'],
                   'close_fds' : True,              }
  try:
    p = subprocess.Popen (argslist, **subproc_args)
  except OSError as e:
    print ('Failed to execute command "{0}": [{1}] {2}'.format (argslist[0], e.errno, e.strerror), file=sys.stderr)
    return
  (stdouterr, stdin) = (p.stdout, p.stdin)
  print ('-- output [{0}] begin --'.format (id))
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
  print ('-- output [{0}] end --'.format (id))
  ret = p.wait ()
  print ('[{0}] Return code: {1}'.format (id, ret))

# 関数定義ここまで

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


thr1 = threading.Thread (target=func,kwargs=dic1)
print ('before thr1.start()')
thr1.start ()  # 開始
print ('after thr1.start()')
print ('before thr1.join() waiting...')
thr1.join ()  # thr1が終了するのを待ち、一旦止まる
print ('after thr1.join()')

# 以下、2つのプロセスを続けてバックグラウンド実行するテスト
thr2 = threading.Thread (target=func,kwargs=dic2)
print ('before thr2.start()')
thr2.start ()
print ('after thr2.start()')
thr3 = threading.Thread (target=func,kwargs=dic3)
print ('before thr3.start()')
thr3.start ()
print ('after thr3.start()')
