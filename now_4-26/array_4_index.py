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

dict_Subject_len = len(list(dict_Subject))
dict_Resource_len = len(list(dict_Resource))
dict_Action_len = len(list(dict_Action))
dict_Condition_len = len(list(dict_Condition))

def Index_get():
    int1 = random.randint(0, dict_Subject_len - 1)
    int2 = random.randint(0, dict_Resource_len - 1)
    int3 = random.randint(0, dict_Action_len - 1)
    int4 = random.randint(0, dict_Condition_len - 1)
    int1_str = str(int1)
    int2_str = str(int2)
    int3_str = str(int3)
    int4_str = str(int4)
    key1 = Key_get(int1, dict_Subject)
    key2 = Key_get(int2, dict_Resource)
    key3 = Key_get(int3, dict_Action)
    key4 = Key_get(int4, dict_Condition)
    count_int1 = dict_Subject[key1][1]
    count_int2 = dict_Resource[key2][1]
    count_int3 = dict_Action[key3][1]
    count_int4 = dict_Condition[key4][1]
    index=int4*count_int4+int1*count_int1/dict_Condition_len+int2*count_int2/(dict_Condition_len*dict_Subject_len)+\
          int3*count_int3/(dict_Condition_len*dict_Subject_len*dict_Resource_len)+1
    return int(index),int1_str,int2_str,int3_str,int4_str
    # print(int1,int2,int3,int4,index)

def Running_time(n):
    i = 0
    k_init = time.clock()
    # print(k_init)
    k_sum = k_init - k_init
    while i < n:
        begin = time.clock()
        index,int1_str,int2_str,int3_str,int4_str=Index_get()
        str = lc.getline('new_extractionSorted.csv', index)
        str = str.strip()  # 去掉首位空白符'\n','\r','\t',' '
        strFromLine = str.split(',')
        if int1_str == strFromLine[1] and int2_str == strFromLine[2] and int3_str == strFromLine[3] and int4_str == \
                strFromLine[4]:
            res = strFromLine[0]
            # break
        end = time.clock()
        # print(begin,end)
        k = end - begin
        # print(k)
        k_sum += k
        # print(str,index)
        i+=1
    return k_sum

def Key_get(n,dict_):
    for key in dict_:
        value_=dict_[key]
        if value_[0]==n:
            return key

# def Create_index(dict_):
#     dict_index =copy.deepcopy(dict_)
#     dict_len = len(list(dict_))
#     i=1
#     while i<dict_len:
#         dict_index[Key_get(i,dict_)][1]+=dict_index[Key_get(i-1,dict_)][1]
#         i+=1
#     return  dict_index
#
# def train(Subjects,listSubjects):
#     res = {}
#     dictSubjects = {}
#     i=0
#
#     for Subject in listSubjects:
#         dictSubjects[Subject] = []
#         dictSubjects[Subject].append(i)
#         i += 1
#         dictSubjects[Subject].append(Subjects.count(Subject))
#     res['Condition3'] = dictSubjects
#     print(res)
#
#     # file = open('Condition_dictionary.txt', 'w')
#     # file.write(str(res))
#     # file.close()
#     # file = open('Condition_dictionary.pkl', 'wb')
#     # p.dump(res, file)
#     # file.close()
#     return res
#
# def loadDataSet_Subject(filename,index_low,index_high):
#     Subjects=[]
#     listSubjects = []
#     i=index_low
#     while i<=index_high:
#         line = lc.getline(filename, i)
#         line = line.strip()#去掉首位空格
#         listFromLine = line.split(',')
#         Subjects.append(listFromLine[1])
#         if listFromLine[1] not in listSubjects:
#             listSubjects.append(listFromLine[1])
#         i+=1
#     print(listSubjects)
#     return Subjects, listSubjects
#
# def loadDataSet_Resource(filename,index_low,index_high):
#     Resources=[]
#     listResources = []
#     i=index_low
#     while i<=index_high:
#         line = lc.getline(filename, i)
#         line = line.strip()#去掉首位空格
#         listFromLine = line.split(',')
#         Resources.append(listFromLine[2])
#         if listFromLine[2] not in listResources:
#             listResources.append(listFromLine[2])
#         i+=1
#     print(listResources)
#     return Resources, listResources



if __name__=='__main__':
    file_record = open('runtime.csv', 'w+')
    i=0
    n=1
    str_title=''
    for x in range(1,20):
        str_title += str(n*500)+','
    str_title += '\n'
    file_record.writelines(str_title)
    while i<100:
        str_=''
        while n<=20:
            k_sum = Running_time(n*500)
            str_+=str(k_sum)+','
            print(k_sum)
            n+=1
        str_+='\n'
        file_record.writelines(str_)
        n=1
        i+=1
    file_record.close()
