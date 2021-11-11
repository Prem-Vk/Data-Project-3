from matplotlib import pyplot as plt
import csv
import seaborn as sns
import pylint.lint

years = []
population = []

with open("SAARC.csv", "r") as raw_data:
    data_reader = csv.reader(raw_data)

    for line in data_reader:
        if line[0] == "India":
            years.append(int(line[2]))
            population.append(int(float(line[3])))

plt.title("India Population")
sns.barplot(x=years, y=population)
plt.xticks(rotation=90)
plt.xlabel("Years")
plt.ylabel("Population")
plt.show()

pylint_opts = ["question_one.py"]
pylint.lint.Run(pylint_opts)
