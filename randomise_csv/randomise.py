# Simple helper script to randomly alter a single-column CSV file.

import csv
import random

originalCSV = open('inventory_ids.csv', newline='')
randomisedCSV = open('inventory_ids_randomised.csv', 'w', newline='')

originalReader = csv.reader(originalCSV)
originalList = list(originalReader)
randomisedWriter = csv.writer(randomisedCSV)

for row in originalList:
  randomisedWriter.writerow(random.choice(originalList))