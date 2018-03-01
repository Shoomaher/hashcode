import math
cur_pos = {}

def get_length(p1, p2):
    return math.fabs(p1[0]-p2[0]) + math.fabs(p1[1]-p2[1])

def find_nearest(start):
    to_center = get_length(start, [0,1])
    for i in cur_pos:

cur_pos = {}
left_cars = 0

def get_length(p1, p2):
    pass

def find_nearest(start, finish, start_time):
    to_center = get_length(start, [0,0])
    way = get_length(start, finish)
    time_to_get = {}
    if (left_cars == 0):
        for i in cur_pos.keys():
            time_to_get[i] =  get_length(start, cur_pos[i])

        min_time = time_to_get[0]

    for i in range(cur_pos.keys()):
        if ((get_length(start, cur_pos[i]) + way - start)  < (to_center + way - start_time)):
            pass



