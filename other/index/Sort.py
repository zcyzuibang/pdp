from operator import itemgetter

input_file = open('new_extraction.csv')
output_file = open('new_extractionSorted.csv','w')

table = []
#header = input_file.readline() #读取并弹出第一行
for line in input_file:
    line = line.strip()
    col = line.split(',') #每行分隔为列表，好处理列格式
    #print(col)
    col[1] = int(col[1])
    col[2] = int(col[2])
    col[3] = int(col[3])
    col[4] = int(col[4]) #各行没有先strip 末位是\n
    table.append(col) #嵌套列表table[[8,8][*,*],...]

table_sorted = sorted(table, key=itemgetter(1))#先后按列索引1排序

#output_file.write(header + '\t')
for row in table_sorted:                    #遍历读取排序后的嵌套列表
    row = [str(x) for x in row]             #转换为字符串格式，好写入文本
    output_file.write(','.join(row) + '\n')

input_file.close()
output_file.close()