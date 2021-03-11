################################################################
# Team              : we need theraPy
# Competiion        : Reply Challenge 2021
# Date created      : 20210311
################################################################

"""
usage of program:
    python template.py << foo.txt
result:
    foo_output.txt  (contains the best possible answer)
"""

#________________ imports ________________#
import sys
import matplotlib.pyplot as plt

#________________ parsing ________________#
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


#________________ functions ________________#

def manhattan(x0, y0, x1, y1):
    return abs(x1-x0) + abs(y1-y0);

#________________ reading ________________#

W = get_number() # width of grid
H = get_number() # height of grid

N = get_number() # num of buildings
M = get_number() # num of antennas
R = get_number() # reward for all buildings connected

B = {} # buildings
A = {} # antennas

for id in range(N):
    x = get_number()
    y = get_number()
    l = get_number()
    c = get_number()
    b = {'x': x, 'y': y, 'l': l, 'c':c }
    B[id] = b

for id in range(M):
    r = get_number()
    c = get_number()
    a = { 'r': r, 'c': c }
    A[id] = a

# latencies of buildings
fig, ax = plt.subplots()
hist_list = [v['l'] for _, v in B.items()]
plt.hist(hist_list, 50, range=[0, 100])  # 50 bars
ax.set(title=f'latencies of buildings (50 bars)', ylabel='number of buildings', xlabel='buckets')
plt.savefig(f'dataset_analysis/latencies_buildings_50bars.png')
plt.close(fig)

# connection speed of buildings
fig, ax = plt.subplots()
hist_list = [v['c'] for _, v in B.items()]
plt.hist(hist_list, 50, range=[0, 100])  # 50 bars
ax.set(title=f'connection speeds of buildings (50 bars)', ylabel='number of buildings', xlabel='buckets')
plt.savefig(f'dataset_analysis/connection_speeds_buildings_50bars.png')
plt.close(fig)

# ranges of antennas
fig, ax = plt.subplots()
hist_list = [v['r'] for _, v in A.items()]
plt.hist(hist_list, 50, range=[0, 6000])  # 50 bars
ax.set(title=f'ranges of antennas (50 bars)', ylabel='number of antennas', xlabel='buckets')
plt.savefig(f'dataset_analysis/ranges_antennas_50bars.png')
plt.close(fig)


# connection speed of antennas
fig, ax = plt.subplots()
hist_list = [v['c'] for _, v in A.items()]
plt.hist(hist_list, 50, range=[0, 10000])
ax.set(title=f'connection speed of antennas (50 bars)', ylabel='number of antennas', xlabel='buckets')
plt.savefig(f'dataset_analysis/connection_speeds_antennas_50bars.png')
plt.close(fig)


#________________#

# latencies of buildings
fig, ax = plt.subplots()
hist_list = [v['l'] for _, v in B.items()]
plt.hist(hist_list, 50)  # 50 bars
ax.set(title=f'latencies of buildings (50 bars)', ylabel='number of buildings', xlabel='buckets')
plt.savefig(f'dataset_analysis/latencies_buildings_auto.png')
plt.close(fig)

# connection speed of buildings
fig, ax = plt.subplots()
hist_list = [v['c'] for _, v in B.items()]
plt.hist(hist_list, 50)  # 50 bars
ax.set(title=f'connection speeds of buildings (50 bars)', ylabel='number of buildings', xlabel='buckets')
plt.savefig(f'dataset_analysis/connection_speeds_buildings_auto.png')
plt.close(fig)

# ranges of antennas
fig, ax = plt.subplots()
hist_list = [v['r'] for _, v in A.items()]
plt.hist(hist_list, 50)  # 50 bars
ax.set(title=f'ranges of antennas (50 bars)', ylabel='number of antennas', xlabel='buckets')
plt.savefig(f'dataset_analysis/ranges_antennas_auto.png')
plt.close(fig)


# connection speed of antennas
fig, ax = plt.subplots()
hist_list = [v['c'] for _, v in A.items()]
plt.hist(hist_list, 50)
ax.set(title=f'connection speed of antennas (50 bars)', ylabel='number of antennas', xlabel='buckets')
plt.savefig(f'dataset_analysis/connection_speeds_antennas_auto.png')
plt.close(fig)
