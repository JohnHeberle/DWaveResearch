import numpy as np
from math import sqrt
from dwave.cloud import Client
import matplotlib.pyplot as plt
import csv
import time

# Takes the information from the csv file and 
fileName = "dataset_realWorld.csv"
file     = open(fileName, newline='')
reader   = csv.reader(file)

header = next(reader)
data   = [row for row in reader]

x = []
y = []

for d in data:
    x.append(float(d[0]))
    y.append(float(d[1]))

file.close()

start_time = time.time()

p1x = np.percentile(x, 25)
p1y = np.percentile(y, 25)
p2x = np.percentile(x, 75)
p2y = np.percentile(y, 75)

din = [0]*len(x)
dim = [0]*len(x)
h   = [0]*len(x)

for i in range( len(x) ):
    din[i] = sqrt( (x[i]-p1x)**2 + (y[i]-p1y)**2 )
    dim[i] = sqrt( (x[i]-p2x)**2 + (y[i]-p2y)**2 )
    h[i] = din[i] - dim[i]

N = 1
result = []
mid_time = time.time()
# Connect using the default or environment connection information
with Client.from_config() as client:

    solver = client.get_solver()

    for i in range( len(x) ):
        linear = {index: h[index] for index in range(len(h))}
        J      = {key: 0 for key in solver.undirected_edges}

    computation = solver.sample_ising(linear, J, num_reads=N)
    result = computation.samples[0][0:len(x)]

final_time = time.time()
print("--- %s seconds from start ---" % (final_time - start_time))
print("--- %s seconds for QC ---" % (final_time - mid_time))
plt.scatter(x, y, c=result)
plt.show()