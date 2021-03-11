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

import numpy as np
from collections import defaultdict

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

#________________ reading ________________#

W = get_number() # width of grid
H = get_number() # height of grid

N = get_number() # num of buildings
M = get_number() # num of antennas
R = get_number() # reward for all buildings connected

bls = {} # buildings
ans = {} # antennas

for id in range(N):
    x = get_number()
    y = get_number()
    l = get_number()
    c = get_number()
    b = {'x': x, 'y': y, 'l': l, 'c':c }
    bls[id] = b

for id in range(M):
    r = get_number()
    c = get_number()
    a = { 'r': r, 'c': c }
    ans[id] = a


# print([item[1] for item in bls.items()])
# sort ids of buildings by decreasing connection speed
bls_sorted = [k for k, v in sorted(bls.items(), key = lambda item: -item[1]['c'])]

# sort ids of buildings by decreasing connection speed
ans_sorted = [k for k, v in sorted(ans.items(), key = lambda item: -item[1]['c'])]

# greedily pair antennas with buildings
Mn = min(M, N) # min(len(bls_sorted), len(ans_sorted))
print(Mn)

for i in range(Mn):
    a_id, b_id = ans_sorted[i], bls_sorted[i]
    print(f"{a_id} {bls[b_id]['x']} {bls[b_id]['y']}")
    # x, y = bls[b_id]['x'], bls[b_id]['y']
    # print(f'{a_id} {x} {y}')
