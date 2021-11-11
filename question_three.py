import csv
from matplotlib import pyplot as plt
import seaborn as sns

yearwise_population = {}

with open("SAARC.csv", "r") as raw_data:
    data_reader = csv.reader(raw_data)

    for line in data_reader:
        if yearwise_population.get(line[2], "NA") == "NA":
            yearwise_population[line[2]] = int(float(line[3]))
        else:
            yearwise_population[line[2]] += int(float(line[3]))

plt.title("Population of SAARC countries")
sns.barplot(x=list(yearwise_population.keys()), y=list(yearwise_population.values()))
plt.xlabel("Years")
plt.ylabel("Population")
plt.show()
