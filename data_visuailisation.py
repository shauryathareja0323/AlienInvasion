import matplotlib.pyplot as plt
import pandas as pd
import csv

df=pd.read_csv("scores.csv")

file_path = "scores.csv"

print(df.describe())

names = []
scores = []

with open(file_path, 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader)
  for row in reader:
    names.append(row[0])
    scores.append(int(row[1]))

plt.bar(names, scores)

plt.xlabel("Names")
plt.ylabel("Scores")
plt.title("Scores of Students")

plt.xticks(rotation=45)

plt.show()
