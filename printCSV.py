import csv

with open('result.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print('Indice'+row[0])
        print('Moeda'+row[1])
        print('Valor'+row[2])