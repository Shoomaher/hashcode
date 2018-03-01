def readfile(input):
    with open(input, 'r') as reader:
        rows, cols, vehicles, col_rides, bonus, steps = [int (i) for i in reader.readline().split(' ')]
        rides = []
        for i in range(col_rides):
            rowstart, colstart, rowend, colend, erlstart, latestfinish = [int (i) for i in reader.readline().split(' ')]
            rides.append({'start': {'rowstart': rowstart, 'colstart': colstart}, 'end': {'rowend' :rowend, 'colend': colend}, 'erlstart':erlstart, 'latestfinish':latestfinish})
        return {'rows': rows, 'cols': cols, 'vehicles': vehicles, 'col_rides': col_rides, 'bonus':bonus, 'steps': steps, 'rides':rides}



def writefile(output):
    with open(output, 'w') as writer:
        writer.write("Tested")

