import csv

with open("files/weather.csv") as f:
     li = list(csv.reader(f))[1:]

city = input("Enter a City Name: ")
for r in li:
    if r[0] == city:
        print(r[1])
