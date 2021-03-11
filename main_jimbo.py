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

#________________ classes ________________#

# claass used to represent an Animal
class Animal:

    # initialise
    def __init__(self, name, sound, num_legs=4):
        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    # says a sound
    def says(self):
        print("Miaou!")

#________________ functions ________________#

def func(l):
    """
    What does it do
    :type l: [[ints]], list of rankings
    :rtype: [ints], rank aggregation
    """
    return

#________________ reading ________________#

N = get_number() # lines to be read
M = get_number() # listings of coins
