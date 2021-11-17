import csv

file = 'nomes.csv'


def getTitle():
    csvFile = open(file)
    reader = csv.reader(csvFile, delimiter=',')
    nomes1 = []
    for line in reader:
        nomes1.append((line[-1]))
    return nomes1


nomes1 = getTitle()
# print(nomes1)
# for i in nomes:
# print("oi")
