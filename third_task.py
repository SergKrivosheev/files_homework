with open('1.txt', 'r', encoding='utf-8') as f:
    file_1 = f.readlines()

with open('2.txt', 'r', encoding='utf-8') as f:
    file_2 = f.readlines()

with open('3.txt', 'r', encoding='utf-8') as f:
    file_3 = f.readlines()

dict1 = {'1.txt': file_1, '2.txt': file_2, '3.txt': file_3}
sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get, reverse=True)

for w in sorted_keys:
    sorted_dict[w] = dict1[w]

with open('result.txt', 'w', encoding='cp1251') as f:
    for element in sorted_dict:
        f.write(element + '\n')
        f.write(str(len(sorted_dict[element])) + '\n')
        for line in sorted_dict[element]:
            f.write(line)
        f.write('\n')