#/usr/bin/python
#encoding:utf-8
import time,json,subprocess

def get_meminfo(duration):
    '''
    Naitve Heap Size 代表最大总共分配空间
    Native Heap Alloc 已使用的内存
    Native Heap Free  剩余内存
    Naitve Heap Size约等于Native Heap Alloc + Native Heap Free
    '''

    p1 = subprocess.Popen('adb shell dumpsys meminfo -a com.wuba',  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result= p1.stdout.read()
    with open('meminfo_log.txt', 'ab+') as f:
         f.truncate()
         f.write(result)
    lists=[]
    heap=[]
    time.sleep(1)
    with open('meminfo_log.txt', 'r') as f:
         result=f.readlines()
         for index in  range(0,len(result)):
            if result[index].startswith('  Native Heap'):
               lists.append(index)
         line= result[lists[0]].split(' ')
         for index in range(len(line)):
             if  line[index] !='' or ('\r\n' in line[index]):
                 heap.append(line[index].replace('\r\n',''))
         print getCurrentTime()
         print 'Naitve Heap Size：',round(float(heap[-3])/1024,3),'Native Heap Alloc：',round(float(heap[-2])/1024,3),'Native Heap Free：',round(float(heap[-1])/1024,3)
         data = {}
         data['time']=duration
         data['Naitve Heap Size']=float(heap[-3])/1024
         data['Native Heap Alloc']=float(heap[-2])/1024
         data['Native Heap Free']=float(heap[-1])/1024
         with open('data.txt', 'a') as json_file:
               json_file.write(json.dumps(data)+"\n")


def getCurrentTime():
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return currentTime



if __name__ == '__main__':
    duration = 15
    #运行间隔
    count = 60
    #运行次数
    total = (duration * count)
    #总共运行的时间
    print "本次内存监控运行:%s分钟"%str(int(total)/60)

    for i in range (0,total,duration):
        get_meminfo(i)
        time.sleep(duration)
