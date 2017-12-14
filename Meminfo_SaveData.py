#/usr/bin/python
#encoding:utf-8
import csv
import os
import  time
import sys
import json

#控制类
class Controller(object):
    def __init__(self):
        #定义收集数据的数组
        self.alldata = []
        #保存id、vss、rss

    #停止adb服务的方法
    def stop(self):
        print os.system('adb kill-server')

    #分析数据
    def analyzedata(self):
        content = self.readfile()
        i = 0
        for line in content:
            if "com.wuba" in line:
                line = "#".join(line.split())
                vss = line.split("#")[7].strip("K")#过滤出来虚拟耗用内存
                rss = line.split("#")[8].strip("K")#过滤出来实体使用物理内存
                #将获取到的数据存到数组中
                i += 1
                dict={}
                dict["id"]=int(i)
                dict["vss"]=int(vss)/100000
                dict["rss"]=int(rss)/100000
                self.alldata.append(dict)

    #数据的存储
    def SaveDataToCSV(self):
        f=open(os.getcwd()+'\\'+'meminfo_result.txt',"a")
        for index in  self.alldata:
            f.write(json.dumps(index)+"\n")



    #读取数据文件
    def readfile(self):
        mfile = file(os.getcwd()+'\\'+'meminfo.log', "r")
        content = mfile.readlines()
        mfile.close()
        return  content



if __name__ == "__main__":
    controller = Controller()

    controller.stop()

    controller.analyzedata()
    controller.SaveDataToCSV()




