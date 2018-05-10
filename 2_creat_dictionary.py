import pickle as p

def train(listSubjects,listResources,listActions,listConditions):
    res = {}#包含dictSubjects dictResources dictActions dictConditions 四个子字典的字典
    dictSubjects = {}
    dictResources = {}
    dictActions = {}
    dictConditions = {}
    i = 0
    for Subject in listSubjects:#遍历listSubjects列表，将列表中的每一个元素作为字典的k，它在列表的下标为value
        dictSubjects[Subject] = i
        i += 1
    res['Subject'] = dictSubjects#将Subject作为key，dictSubjects作为value添加到res中
    i = 0
    for Resource in listResources:#遍历listResources列表，将列表中的每一个元素作为字典的k，它在列表的下标为value
        dictResources[Resource] = i
        i += 1
    res['Resource'] = dictResources#将Resource作为key，dictResources作为value添加到res中
    i = 0
    for Action in listActions:#遍历listActions列表，将列表中的每一个元素作为字典的k，它在列表的下标为value
        dictActions[Action] = i
        i += 1
    res['Action'] = dictActions#将Action作为key，dictActions作为value添加到res中
    i = 0
    for Condition in listConditions:#遍历listConditions列表，将列表中的每一个元素作为字典的k，它在列表的下标为value
        dictConditions[Condition] = i
        i+=1
    res['Condition'] = dictConditions#将Condition作为key，dictCondition作为value添加到res中
    file = open('dictionary.txt', 'w')
    file.write(str(res))
    file.close()
    file = open('dictionary.pkl', 'wb')
    p.dump(res, file)
    file.close()
    return res

def loadDataSet(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()

    listSubjects = []
    listResources = []
    listActions = []
    listConditions = []

    for line in arrayOLines:
        line = line.strip()#去掉首位空格
        listFromLine = line.split(',')
        #listFromLine[1]为subject，listFromLine[2]为resources，listFromLine[3]为action，listFromLine[4]为condition
        if listFromLine[1] not in listSubjects:#如果Subject在列表listSubjects中不存在，将其添加到列表
            listSubjects.append(listFromLine[1])
        if listFromLine[2] not in listResources:#如果Resource在列表listResources中不存在，将其添加到列表
            listResources.append(listFromLine[2])
        if listFromLine[3] not in listActions:#如果Action在列表listActions中不存在，将其添加到列表
            listActions.append(listFromLine[3])
        if listFromLine[4] not in listConditions:#如果Condition在列表listConditions中不存在，将其添加到列表
            listConditions.append(listFromLine[4])
    return listSubjects, listResources, listActions, listConditions

if __name__=='__main__':
    filename='extraction.csv'
    listSubjects, listResources, listActions, listConditions = loadDataSet(filename)
    train(listSubjects,listResources,listActions,listConditions)




