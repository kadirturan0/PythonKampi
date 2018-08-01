import csv

file_path = "data.csv"

with open(file_path) as f:
    satirlar = csv.reader(f, deliiter=",")
    for row in satirlar