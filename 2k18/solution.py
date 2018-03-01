import math
cur_pos = {}

def get_length(p1, p2):
    return math.fabs(p1[0]-p2[0]) + math.fabs(p1[1]-p2[1])

def find_nearest(start):
    to_center = get_length(start, [0,1])
    for i in cur_pos:

