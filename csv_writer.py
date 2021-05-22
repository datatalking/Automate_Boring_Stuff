#%%

import csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# output is 21 because (4) words + (3) commas + carriage return
#%%

outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
#%%

outputWriter.writerow([1, 2, 3,141592, 4])
#%%

outputFile.close()
#%%


