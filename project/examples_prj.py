import csv
with open('users.csv', 'r') as file:
    reader = csv.reader(file)
    print(reader)
    # for row in reader:
    #     print(row)