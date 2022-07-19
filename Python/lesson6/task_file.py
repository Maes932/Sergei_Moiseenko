import matplotlib.pyplot as plt
import json

with open('E:\\Users\\Сергей\\Desktop\\ratings.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]
    columns = data[27].split(' ')
    data_1 = [line.split(' ') for line in data[28:278]]
    data_2 = [line.split(' ') for line in data[28:278]]
    
Rank = [float(data_1[2]) for data_1 in data_1]
Title = [data_1[3] for data_1 in data_1]
Years = [data_2[-1] for data_2 in data_2]

years = [years.replace('(', ' ').replace(')', ' ').strip() for years in Years]
years_1 = []
for i in years:
    if i.isdigit():
        years_1.append(int(i))
    else:
        i = i.replace('/', ' ').replace('I', ' ').replace(' ', ' ').strip()
        years_1.append(int(i))        
  
with open('years.txt', 'w') as fh:
    json.dump(years, fh, indent=' ')
with open('ratings films.txt', 'w') as fh:
    json.dump(Rank, fh, indent=' ')
with open('top250.txt', 'w') as fh:
    json.dump(Title, fh, indent=' ') 
           
   
            



