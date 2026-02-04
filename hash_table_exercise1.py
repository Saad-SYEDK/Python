import csv
my_dict =dict()

with open('nyc_weather.csv', mode='r') as f:
    for line in f:
        token = line.split(',')
        my_dict[token[0]] = token[1]

#fetching
print("avg temp in first week of jan")
avg = 0
key = 'Jan i'
for i in range(1,8):
    key = key.replace('i', str(i))
    avg += int(my_dict.get(key))
    key = key.replace(str(i), 'i')
print(avg/7)

print()

print('max temp in first 10 days of jan')
max = 0
for i in range(1,8):
    key = key.replace('i', str(i))
    current = int(my_dict.get(key))
    if max <= current:
        max = current
    key = key.replace(str(i), 'i')
print(max)
    
    