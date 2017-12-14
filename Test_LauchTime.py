#/usr/bin/python
#encoding:utf-8

import os

# print os.popen("adb shell")
try:
    os.system("adb logcat  | findstr com.wuba | findstr ActivityManager > C:\\Users\\58\\Desktop\\Launch_Time.txt")
    # print str(result.read())
    # with open(os.getcwd()+'Launch_Time.txt', 'ab+') as f:
    #      f.write(str(result.read()))

    print "save_done"
except  BaseException,e:
    print e

