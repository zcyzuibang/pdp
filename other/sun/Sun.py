import pickle as p
import random
import linecache
import time
from decimal import *

filename = 'new_extraction.csv'
myfile = open(filename)
lines = len(myfile.readlines())

def Search(int1_str,int2_str,int3_str,int4_str):
    i=1
    res='NotApplicable'
    while i<=lines:
        str=linecache.getline(filename, i)
        str = str.strip()  # 去掉首位空白符'\n','\r','\t',' '
        strFromLine = str.split(',')
        if int1_str==strFromLine[1] and int2_str==strFromLine[2] and int3_str==strFromLine[3] and int4_str==strFromLine[4]:
            res=strFromLine[0]
            break
        # print(str)
        i+=1
    return res

def Size():
    file = open('dictionary.pkl', 'rb')
    dictionary = p.load(file)
    file.close()
    dict_Subject = dictionary['Subject']
    dict_Resource = dictionary['Resource']
    dict_Action = dictionary['Action']
    dict_Condition = dictionary['Condition']
    dict_Subject_len = len(list(dict_Subject))
    dict_Resource_len = len(list(dict_Resource))
    dict_Action_len = len(list(dict_Action))
    dict_Condition_len = len(list(dict_Condition))
    return dict_Subject_len,dict_Resource_len,dict_Action_len,dict_Condition_len
    # print(dict_Subject_len)
    # print(dict_Resource_len)
    # print(dict_Action_len)
    # print(dict_Condition_len)

def Running_time(n):
    dict_Subject_len, dict_Resource_len, dict_Action_len, dict_Condition_len = Size()
    i = 0
    k_init = time.time()
    # print(k_init)
    k_sum = k_init - k_init
    while i < n:
        int1 = random.randint(0, dict_Subject_len - 1)
        int2 = random.randint(0, dict_Resource_len - 1)
        int3 = random.randint(0, dict_Action_len - 1)
        int4 = random.randint(0, dict_Condition_len - 1)
        # int1 = 0
        # int2 = 0
        # int3 = 0
        # int4 = 0
        int1_str = str(int1)
        int2_str = str(int2)
        int3_str = str(int3)
        int4_str = str(int4)
        begin = time.clock()
        res = Search(int1_str, int2_str, int3_str, int4_str)
        end = time.clock()
        k = end - begin
        # print(k)
        k_sum += k
        # print(k.total_seconds())
        # print(int1_str + ' ' + int2_str + ' ' + int3_str + ' ' + int4_str + ' ' + res)
        i+=1
    return k_sum

if __name__=='__main__':
    k_sum=Running_time(500)
    print(k_sum)
    # print(k_sum.total_seconds())
    # print(time.clock())
    # time.clock()
    # t=time.clock();
    # print(Decimal(time.time()))
    # print(time.time(), time.clock())

