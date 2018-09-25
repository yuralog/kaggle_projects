import pandas as pd
from collections import Counter
print('Введите путь к файлу в котором искать дубли c названием файла или название файла, если он находится в той же папке')
way = input()
df = pd.read_csv(way ,sep=';', encoding ='windows-1251')
data=df.fillna('')
print('Введите количестко колонок')
columsN = int(input())

colums =[]
name = ""
for i in range(1, columsN+1):
        print('Введите название',  i, 'столбца')
        k = input()
        name = name + k
        colums.append(k)
data[name] = data[colums[0]]
for i in range(1, len(colums)):
    data[name] = data[name] + data[colums[i]]
val_count = data[name].value_counts()
filter_val = val_count[(val_count> 1) & (val_count.index != '')].index
filter_data = data[data[name].isin(filter_val)]
result=filter_data.drop(columns = [name])
result.to_csv('result.csv', index=False)