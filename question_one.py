from matplotlib import pyplot as plt
import csv

with open('population-estimates_csv','r') as raw_data:
    data_reader = csv.reader(raw_data)
    
    for line in data_reader:
        print(line)