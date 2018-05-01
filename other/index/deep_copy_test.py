import copy
dict = {'a':[1,2,3,4,5],'b':2}
x = copy.deepcopy(dict['a'])
for i in range(5):
    x[i] = 0
print(dict['a'])

