#-*- coding:utf-8 -*-

import urllib.request
import sys
import re

def _(url, file_name):
    urllib.request.urlretrieve(url,"{0}".format(file_name))

if __name__ == "__main__":
    download()
