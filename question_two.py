import csv
from matplotlib import pyplot as plt
import seaborn as sns

country = []
population = []

with open("ASEAN.csv", "r") as raw_data:
    data_reader = csv.reader(raw_data)

    for line in data_reader:
        if line[2] == "2014":
            country.append(line[0])
            population.append(int(float(line[3])))


plt.title("Population of ASEAN countries of year 2014")
sns.barplot(x=country, y=population)
plt.xlabel("Countries")
plt.ylabel("Population")
plt.show()
