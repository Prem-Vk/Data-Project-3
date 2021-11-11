from matplotlib import pyplot as plt
import csv
from collections import Counter

ASEAN = [
    "Brunei Darussalam",
    "Cambodia",
    "Indonesia",
    "Laos",
    "Malaysia",
    "Myanmar",
    "Philippines",
    "Singapore",
    "Thailand",
    "Vietnam",
]

SAARC = [
    "Afghanistan",
    "Bangladesh",
    "Bhutan",
    "India",
    "Maldives",
    "Nepal",
    "Pakistan",
    "Sri Lanka",
]

f = open("SAARC.csv", "w")
writer = csv.writer(f)

ASEAN = [i.lower() for i in ASEAN]
SAARC = [i.lower() for i in SAARC]

with open("population-estimates_csv.csv", "r") as raw_data:
    data_reader = csv.reader(raw_data)
    next(data_reader)

    for line in data_reader:
        if line[0].rstrip().lower() in SAARC:
            writer.writerow(line)

f.close()

# for i in countries:
#     for j in ASEAN:
#         if i.lower().startswith(j.lower()):
#             print(i)
