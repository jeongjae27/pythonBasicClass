import csv

with open('차량관리.csv','w') as file:
    csv_maker = csv.writer(file,delimiter=",")
    csv_maker.writerow([1,'08RU1234','2020-10-20.14:00'])
    csv_maker.writerow([2,'08RU1234','2020-10-20.14:00'])
    csv_maker.writerow([3,'08RU1234','2020-10-20.14:00'])

print('차량관리.csv created')
