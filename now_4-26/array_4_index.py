import pickle as p
import linecache as lc
import copy

file = open('dictionary.pkl', 'rb')
dictionary = p.load(file)
file.close()

dict_Subject = dictionary['Subject']
dict_Resource = dictionary['Resource']
dict_Action = dictionary['Action']
dict_Condition = dictionary['Condition']

def Key_get(n,dict_):
    for key in dict_:
        value_=dict_[key]
        if value_[0]==n:
            return key

def Create_index(dict_):
    dict_index =copy.deepcopy(dict_)
    dict_len = len(list(dict_))
    i=1
    while i<dict_len:
        dict_index[Key_get(i,dict_)][1]+=dict_index[Key_get(i-1,dict_)][1]
        i+=1
    return  dict_index

def train(Subjects,listSubjects):
    res = {}
    dictSubjects = {}
    i=0

    for Subject in listSubjects:
        dictSubjects[Subject] = []
        dictSubjects[Subject].append(i)
        i += 1
        dictSubjects[Subject].append(Subjects.count(Subject))
    res['Condition3'] = dictSubjects
    print(res)

    # file = open('Condition_dictionary.txt', 'w')
    # file.write(str(res))
    # file.close()
    # file = open('Condition_dictionary.pkl', 'wb')
    # p.dump(res, file)
    # file.close()
    return res

def loadDataSet_Subject(filename,index_low,index_high):
    Subjects=[]
    listSubjects = []
    i=index_low
    while i<=index_high:
        line = lc.getline(filename, i)
        line = line.strip()#去掉首位空格
        listFromLine = line.split(',')
        Subjects.append(listFromLine[1])
        if listFromLine[1] not in listSubjects:
            listSubjects.append(listFromLine[1])
        i+=1
    print(listSubjects)
    return Subjects, listSubjects

def loadDataSet_Resource(filename,index_low,index_high):
    Resources=[]
    listResources = []
    i=index_low
    while i<=index_high:
        line = lc.getline(filename, i)
        line = line.strip()#去掉首位空格
        listFromLine = line.split(',')
        Resources.append(listFromLine[2])
        if listFromLine[2] not in listResources:
            listResources.append(listFromLine[2])
        i+=1
    print(listResources)
    return Resources, listResources

if __name__=='__main__':
    filename='new_extractionSorted.csv'
    int1=3
    key_Condition = Key_get(int1,dict_Condition)
    dict_Condition_index = Create_index(dict_Condition)
    print(dict_Condition_index)
    index_high = dict_Condition_index[key_Condition][1]
    index_low = index_high - dict_Condition[key_Condition][1] + 1
    Subjects, listSubjects = loadDataSet_Subject(filename,index_low,index_high)
    res=train(Subjects, listSubjects)
    dict_S=res['Condition3']
    print (dict_S)
    print(str(index_high),str(index_low))
    key_Subject = Key_get(int1, dict_Subject)
    dict_S_index = Create_index(dict_S)
    print(dict_S_index)
    index_h = dict_S_index[str(0)][1]
    index_l = index_h - dict_S[str(0)][1] + 1
    print(str(index_h), str(index_l))
    Resources, listResources = loadDataSet_Resource(filename, index_low+index_l-1, index_high+index_h)
    # res = train(Subjects, listSubjects)
    # Subjects, listSubjects = loadDataSet_Subject(filename, index_l, index_h)
