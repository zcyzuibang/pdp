import pickle as p

if __name__=='__main__':
    file = open('Condition.txt', 'rb')
    probMat = p.load(file)
    file.close()
    file_r=open('extraction.csv','r+')
    file_w=open('new_extraction.csv','w+')
    for line in file_r.readlines():
        line = line.strip()  # 去掉首位空白符'\n','\r','\t',' '
        str_temp_old = line
        str_temp_new = ''
        listFromLine = line.split(',')
        i=1
        while i<5:
            list_temp = []
            dict={}
            if i==1:
                dict=probMat['Subject']
                list_temp=dict[listFromLine[1]]
                str_temp_new = listFromLine[0] + ',' + str(list_temp[0]) +','
            elif i==2:
                dict = probMat['Resource']
                list_temp = dict[listFromLine[2]]
                listFromLine[2] = list_temp[0]
                str_temp_new += str(list_temp[0])+','
            elif i==3:
                dict = probMat['Action']
                list_temp = dict[listFromLine[3]]
                str_temp_new += str(list_temp[0]) + ','
            elif i==4:
                dict = probMat['Condition']
                list_temp = dict[listFromLine[4]]
                str_temp_new += str(list_temp[0]) +'\n'
            i+=1
        file_w.writelines(str_temp_new)
    file_r.close()
    file_w.close()

