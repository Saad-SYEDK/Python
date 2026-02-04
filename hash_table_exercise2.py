my_dict = dict()

with open('poem.txt', 'r') as file:
    for line in file:
        token = line.split(' ')
        for i in token:
            i = i.replace('\n', '')
            if my_dict.get(i) is None:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

for i in my_dict:
    print(i)

    