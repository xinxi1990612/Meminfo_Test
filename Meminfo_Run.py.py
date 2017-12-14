#coding=utf-8
import os
#运行查询内存数据
def run():
    print ('start runing!!!')
    #os.system('adb devices')
    os.popen('adb shell top -d l | findstr "com.wuba" >'+os.getcwd()+'\\'+'meminfo.log')


if __name__ == '__main__':
    run()