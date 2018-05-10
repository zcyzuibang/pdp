import pickle as p

if __name__=='__main__':
    file = open('dictionary.pkl', 'rb')
    probMat = p.load(file)#载入字典
    file.close()
    file_r=open('extraction.csv','r+')#要数值化的策略集数据
    file_w=open('new_extraction.csv','w+')#保存数值化之后的策略集数据
    for line in file_r.readlines():#按行读取策略集数据
        line = line.strip()  # 去掉首位空白符'\n','\r','\t',' '
        str_temp_old = line#保存策略集原来的一行，即一条策略
        str_temp_new = ''#保存数值化后的字符串
        listFromLine = line.split(',')
        # listFromLine[1]为subject，listFromLine[2]为resources，listFromLine[3]为action，listFromLine[4]为condition

        i=1
        while i<5:#处理每一条策略
            dict={}
            if i==1:#数值化Subject
                dict=probMat['Subject']
                numerical=dict[listFromLine[1]]
                str_temp_new = listFromLine[0] + ',' + str(numerical) + ','
            elif i==2:#数值化Resource
                dict = probMat['Resource']
                numerical = dict[listFromLine[2]]
                str_temp_new += str(numerical) + ','
            elif i==3:#数值化Action
                dict = probMat['Action']
                numerical = dict[listFromLine[3]]
                str_temp_new += str(numerical) + ','
            elif i==4:#数值化Condition
                dict = probMat['Condition']
                numerical = dict[listFromLine[4]]
                str_temp_new += str(numerical) + '\n'
            i+=1
        file_w.writelines(str_temp_new)
    file_r.close()
    file_w.close()

