import csv

def read_csv(path):
   # Tu código aquí 👇
  with open(path, 'r') as csvfile:
   reader = csv.reader(csvfile, delimiter=',')
   header = next(reader)
   total = 0 
   for row in reader:
      #print (row[1])
      total += int(row[1])
   return total

response = read_csv('./app/data.csv')
print(response)