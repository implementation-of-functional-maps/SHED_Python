#-*- coding:utf-8 -*-

import urllib.request
import sys
import re

def _(pattern, url):
    matchOB = re.match(pattern , url)
    import download
    file_name = "model.zip"
    if matchOB:
        download._(url, file_name)
# "https://3dwarehouse.sketchup.com/warehouse/getbinary"
# "https://3dwarehouse.sketchup.com/warehouse/getbinary?subjectId=[.*]&subjectClass=entity&name=s15&fn="
if __name__ == "__main__":
    download()
