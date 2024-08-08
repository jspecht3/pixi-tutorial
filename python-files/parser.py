import csv

theta = []
cos = []
sin = []

with open("data.csv") as file:
    reader = csv.DictReader(file, delimiter = ',')

    for row in reader:
        theta.append( float(row['theta']) )
        cos.append( float(row['cos']) )
        sin.append( float(row['sin']) )
