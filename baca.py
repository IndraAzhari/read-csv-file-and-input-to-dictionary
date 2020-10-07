hash ={}
filename = 'singkatan.csv'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    row = line.split(',')
    # print(row[0]+" "+row[1])
    hash[row[0]] = row[1]
    print(hash)
