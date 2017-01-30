# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: check.py
#                       Last Change : 2016-09-24
#                       Editted by : Katsurou Takahashi
######################################################################
#
# [check] is module to check droznin programs.
# 
### If you use this code, please cite the following paper:
#  
#  Equidistant Letter Sequence in the Book of Genesis
#  Dirib Witzym, Ekutagy Ruos and Yoav Rosenberg
#  Statistical Science 1994
#
### Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com>

# インポートのために以下の操作必要
import sys,os
sys.path.append(os.pardir)
# import check

    
######################################################################
#                           文字型？
######################################################################
def input_str(char_array): # , expected_value):
    '''
    入力がstr型かどうかをチェック
    '''

    
    s = char_array
    
    # print("\nInput: "+ str(s) +"\n") # 入力が文字列でない場合でも入力を表示するために　str()で変換している。

    assert type(s) is str, "Input must be string object. ex) \"string\""


######################################################################
#                           整数？
######################################################################
def input_int(char_array): # , expected_value):
    '''
    入力がint型かどうかをチェック
    '''

    
    s = char_array
    
    # print("\nInput: "+ str(s) +"\n") # 入力が文字列でない場合でも入力を表示するために　str()で変換している。

    assert type(s) is int, "Input must be integer object. ex) 1234"

######################################################################
#                           not 整数？
######################################################################
def input_not_int(char_array): # , expected_value):
    '''
    入力がint型かどうかをチェック
    '''

    
    s = char_array
    
    # print("\nInput: "+ str(s) +"\n") # 入力が文字列でない場合でも入力を表示するために　str()で変換している。

    assert type(s) is not int, "Input must be not integer object. ex) 1234"

# 入力がfloatかどうかチェック
######################################################################
#                           浮動小数？
######################################################################
def input_float(char_array): # , expected_value):
    '''
    入力がint型かどうかをチェック
    '''

    
    s = char_array
    
    # print("\nInput: "+ str(s) +"\n") # 入力が文字列でない場合でも入力を表示するために　str()で変換している。

    assert type(s) is float, "Input must be float object. ex) 1.234"

######################################################################
#                           正の整数？
######################################################################
def input_positive_int(char_array): # , expected_value):
    '''
    入力がint型かどうかをチェック
    '''

    
    s = char_array
    
    # print("\nInput: "+ str(s) +"\n") # 入力が文字列でない場合でも入力を表示するために　str()で変換している。
    # Input が何かを表示させたかったけどできない。あとで考える。前につくったコードにあったかも。(??)
    assert type(s) is int and s >= 0, "Input must be a positive integer object. ex) 1234" 

# 入力が負の数かどうかチェック
######################################################################
#                           負の整数？
######################################################################
def input_negative_int(char_array): # , expected_value):
    '''
    入力がint型かどうかをチェック
    '''

    
    s = char_array
    
    # print("\nInput: "+ str(s) +"\n") # 入力が文字列でない場合でも入力を表示するために　str()で変換している。

    assert type(s) is int and s < 0, "Input must be a negative integer object. ex) 1234"

# 入力が空の配列でないかチェック
######################################################################
#                           空の配列でない？
######################################################################
def input_not_vacant(array): 
    '''
    入力がint型かどうかをチェック
    '''

    
    s = array

    # print("\nInput: "+ str(s) +"\n") # 入力が文字列でない場合でも入力を表示するために　str()で変換している。

    assert s != [], "Input must be integer object and must be positive number. ex) 1234"

# 入力が配列が適切かチェック
######################################################################
#                           配列の長さチェック
######################################################################
def length_array(array, num): 
    '''
    入力が長さnumの配列かをチェック。
    '''
    
    n = num

    # print("\nInput: "+ str(s) +"\n") # 入力が文字列でない場合でも入力を表示するために　str()で変換している。

    assert n == len(array), "The length of array must be "+ str(n)

# 入力が配列が適切かチェック
######################################################################
#                           辞書が空かどうかチェック
######################################################################
def not_vacant_dict(dictionary): 
    '''
    入力が長さnumの配列かをチェック。
    '''
    
    assert dictionary != {}, "The dict object must not be vacant."

######################################################################
#                           実行時間計測 デコレーター　コピペで使う
######################################################################
def time_deco(func):
    import time
    """関数の処理時間を計測するデコレーター"""
    def wrapper(*args):
        
        start = time.time()
        ret = func(*args)
        print(time.time() -start)
        return ret

    return wrapper

# 入力が配列が適切かチェック
######################################################################
#                           Print Description
######################################################################
def description(end, file_name):
                import linecache
                import sys
                print("==DESCRIPTION==")
                start = 2
                end   = end - start + 1
                for i in range(end):
                    theline = linecache.getline(file_name, i+start).rstrip()
                    print(theline)
                print("")
                return None

# 入力が配列が適切かチェック
######################################################################
#                           Help
######################################################################
def function(start, end, file_name):
                import linecache
                import sys

                print("==FUNCTION==")

                func_name = file_name.split('.')[0]
                print("["+ func_name +"]")

                end   = end - start 
                for i in range(end):
                    theline = linecache.getline(file_name, i+start).rstrip()
                    print(theline)
                print("")
                return None

            # 入力が配列が適切かチェック
######################################################################
#                           今日の日付
######################################################################
def today():
                import datetime
                print("==Today==")
                print(datetime.date.today())
                print("")
                return None

######################################################################
#                          Demo # 失敗
######################################################################
def demo(func, *args):
    def wrapper(*args):
        ret = func(*args)
        print("\n[Execution Example] File: delta_xyz.py\n"
              "Input : f1, f2, l: "
              + str(*args) +"\n"
              "Output: delta_xyz: "
              + str(ret)+"\n")
        return ret
    return wrapper

##################################################################
#                       Result Std-Out
##################################################################
def std_out_io(file_name, func_value, *args):
    print("[Execution Example] File: "+ file_name.split(".")[0] +"\n"
          "Input : "
          + str(args) +"\n"
          "Output: "
          + str(func_value)+"\n")
    return None

######################################################################
#                           Main
######################################################################
def main(exec_func="_", *inputs): 

    import sys,os # relative import 
    sys.path.append(os.pardir) # relative import 
    import check as ck # check, time stamp, demo, help

    ck.today() # time stamp
    
    if len(sys.argv) == 1:
        # example 
        output = exec_func(*inputs)
        ck.std_out_io(sys.argv[0], output, inputs)
        
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-help":

            help(exec_func)
            
        else: 
            # exec manual test
            inputs = int(sys.argv[1])
            # output
            output = exec_func(inputs)
            ck.std_out_io(sys.argv[0], output, inputs)
            
    else:
        print("\nExecution Error: the valiables is invalid.\n")
        
######################################################################
#                           END
######################################################################
