import pickle as p
import linecache as lc
import random
import time

file = open('dictionary.pkl', 'rb')
dictionary = p.load(file)
file.close()

myfile = open( 'new_extractionSorted.csv')

dict_Subject = dictionary['Subject']
dict_Resource = dictionary['Resource']
dict_Action = dictionary['Action']
dict_Condition = dictionary['Condition']

dict_Subject_len = len(dict_Subject)
dict_Resource_len = len(dict_Resource)
dict_Action_len = len(dict_Action)
dict_Condition_len = len(dict_Condition)


def Running_time(n):
    i = 0
    k_init = time.clock()
    # print(k_init)
    k_sum = k_init - k_init
    while i < n:
        #生成随机数模拟随机的一条策略集
        int1 = random.randint(0, dict_Subject_len - 1)
        int2 = random.randint(0, dict_Resource_len - 1)
        int3 = random.randint(0, dict_Action_len - 1)
        int4 = random.randint(0, dict_Condition_len - 1)

        #根据随机数获取键值，用来计算数值化的时间，
        key1 = Key_get(int1, dict_Subject)
        key2 = Key_get(int2, dict_Resource)
        key3 = Key_get(int3, dict_Action)
        key4 = Key_get(int4, dict_Condition)

        begin = time.clock()#程序运行起始时间

        #数值化，根据键值获取值，我们对策略集匹配第一步数值化的时间应该被计算
        value1 = int(dict_Subject[key1])
        value2 = int(dict_Resource[key2])
        value3 = int(dict_Action[key3])
        value4 = int(dict_Condition[key4])

        #用来计算索引的几个参数，count_int1表示sub的个（种类）数count_int2表示res的个数，count_int3表示act的个数count_int4表示con的个数，
        count_int1 = dict_Subject_len
        count_int2 = dict_Resource_len
        count_int3 = dict_Action_len
        count_int4 = dict_Condition_len

        index = value1 * count_int2 * count_int3 * count_int4 + value2 * count_int3 * count_int4 + value3 * count_int4 + value4+1

        end = time.clock()#程序运行结束时间
        print(value1, value2, value3, value4)
        print(index)
        # print(begin,end)
        k = end - begin#单次运行时间
        # print(k)
        k_sum += k
        # print(str,index)
        i+=1
    return k_sum

def Key_get(n,dict_):#参数为数字和对应的字典，返回它对应的键值
    for key in dict_:
        value_=dict_[key]
        if value_==n:
            return key


if __name__=='__main__':
    file_record = open('runtime.csv', 'w+')
    # file_record.close()
    # k_sum = Running_time(5)
    # print(k_sum)
    i=0
    n=1
    str_title=''
    for x in range(1,21):#写入第一行500,1000,...,10000
        str_title += str(x*500)+','
    str_title += '\n'
    file_record.writelines(str_title)
    while i<20:#运行20次，记录20行数据，求平均
        str_=''
        while n<=20:
            k_sum = Running_time(n*500)#记录匹配500,1000,...,10000条的时间
            str_+=str(k_sum)+','
            print(k_sum)
            n+=1
        str_+='\n'
        file_record.writelines(str_)
        n=1
        i+=1
    file_record.close()
