import pickle as p

def train(Effects,Subjects,Resources,Actions,Conditions,listSubjects,listResources,listActions,listConditions):
    res = {}
    dictSubjects = {}
    dictResources = {}
    dictActions = {}
    dictConditions = {}
    i=0
    for Condition in listConditions:
        dictConditions[Condition] = []
        dictConditions[Condition].append(i)
        i+=1
        dictConditions[Condition].append(Conditions.count(Condition))
        dictConditions[Condition].append(0)
    res['Condition'] = dictConditions
    i = 0
    for Subject in listSubjects:
        dictSubjects[Subject] = []
        dictSubjects[Subject].append(i)
        i += 1
        dictSubjects[Subject].append(Subjects.count(Subject))
        dictSubjects[Subject].append(0)
    res['Subject'] = dictSubjects
    i = 0
    for Resource in listResources:
        dictResources[Resource] = []
        dictResources[Resource].append(i)
        i += 1
        dictResources[Resource].append(Resources.count(Resource))
        dictResources[Resource].append(0)
    res['Resource'] = dictResources
    i = 0
    for Action in listActions:
        dictActions[Action] = []
        dictActions[Action].append(i)
        i += 1
        dictActions[Action].append(Actions.count(Action))
        dictActions[Action].append(0)
    res['Action'] = dictActions
    # print(res)
    # print(str(res))
    file = open('Condition_str.txt', 'w')
    file.write(str(res))
    file.close()
    file = open('Condition.txt', 'wb')
    p.dump(res, file)
    file.close()
    return res

def loadDataSet(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    Effects=[]
    Subjects=[]
    Resources=[]
    Actions=[]
    Conditions=[]

    listSubjects = []
    listResources = []
    listActions = []
    listConditions = []

    for line in arrayOLines:
        line = line.strip()#去掉首位空格
        listFromLine = line.split(',')
        Effects.append(listFromLine[0])#append() 方法用于在列表末尾添加新的对象
        Subjects.append(listFromLine[1])
        if (listFromLine[1] in listSubjects)==0:
            listSubjects.append(listFromLine[1])
        Resources.append(listFromLine[2])
        if (listFromLine[2] in listResources)==0:
            listResources.append(listFromLine[2])
        Actions.append(listFromLine[3])
        if (listFromLine[3] in listActions)==0:
            listActions.append(listFromLine[3])
        Conditions.append(listFromLine[4])
        if (listFromLine[4] in listConditions)==0:
            listConditions.append(listFromLine[4])

    return  Effects,Subjects,Resources,Actions,Conditions,listSubjects,listResources,listActions,listConditions

if __name__=='__main__':
    filename='extraction.csv'
    Effects, Subjects, Resources, Actions, Conditions, listSubjects, listResources, listActions, listConditions = loadDataSet(filename)
    train(Effects,Subjects,Resources,Actions,Conditions,listSubjects,listResources,listActions,listConditions)




