import csv
from matplotlib import pyplot as plt
import seaborn as sns
from collections import Counter

countries = []
population = {}
all_data = []
years = [str(i) for i in range(2004, 2015)]

with open("ASEAN.csv", "r") as raw_data:
    data_reader = csv.reader(raw_data)

    for line in data_reader:
        if line[2] in years:
            all_data.append(line)

for country in all_data:
    if country[0] in countries:
        pass
    else:
        countries.append(country[0])

population = Counter(countries)
population = dict((i, []) for i in countries)
print(population)

for country in countries:
    for data in all_data:
        if country == data[0]:
            population[country].append(int(float(data[3])))

barwidth = 0.07
r1 = [i for i in range(1, 12)]
r2 = [x + barwidth for x in r1]
r3 = [x + barwidth for x in r2]
r4 = [x + barwidth for x in r3]
r5 = [x + barwidth for x in r4]
r6 = [x + barwidth for x in r5]
r7 = [x + barwidth for x in r6]
r8 = [x + barwidth for x in r7]


plt.bar(
    r1, population[countries[0]], width=barwidth, edgecolor="white", label=countries[0]
)
plt.bar(
    r2, population[countries[1]], width=barwidth, edgecolor="white", label=countries[1]
)
plt.bar(
    r3, population[countries[2]], width=barwidth, edgecolor="white", label=countries[2]
)
plt.bar(
    r4, population[countries[3]], width=barwidth, edgecolor="white", label=countries[3]
)
plt.bar(
    r5, population[countries[4]], width=barwidth, edgecolor="white", label=countries[4]
)
plt.bar(
    r6, population[countries[5]], width=barwidth, edgecolor="white", label=countries[5]
)
plt.bar(
    r7, population[countries[6]], width=barwidth, edgecolor="white", label=countries[6]
)
plt.bar(
    r8, population[countries[7]], width=barwidth, edgecolor="white", label=countries[7]
)
plt.legend()
plt.xticks([r + barwidth for r in range(1, 12)], [str(i) for i in range(2004, 2015)])
# plt.yticks([0, 5000, 10000, 20000, 40000, 80000, 160000, 260000])
plt.show()
