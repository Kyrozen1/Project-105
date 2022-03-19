import csv
import math
import time

with open("data.csv",newline="") as f:
  reader = csv.reader(f)
  file_data = list(reader)

data = file_data[0]
def mean(data):
  n=len(data)
  total = 0
  for x in data:
    total += int(x)
  mean = total/n
  print(str(mean)) 
  return mean

squareList = []
for number in data:
  a = int(number) - mean(data)
  a= a**2
  squareList.append(a)

sum = 0
for i in squareList:
  sum = sum + i

result = sum/(len(data)-1)
standardDiviation = math.sqrt(result)
print(str(standardDiviation))

time.sleep(1000)