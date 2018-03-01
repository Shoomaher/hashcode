import copy as cp


def collected(slice): #Проверяем, собран ли кусок
    M = 0
    T = 0
    size = 0
    for i in range(len(slice)):
        for j in range(len(slice[i])):
            size+=1
            if slice[i][j] == 'M':
                M+=1
            elif slice[i][j] == 'T':
                T+=1

    if (M >= params['L'] and T >= params['L'] and size < params['H']):
        return True
    else:
        return False

def mark_slice(position, slice): #Помечаем участок пиццы как вырезанный кусок
    slice_num+=1
    for i in range(len(slice)):
        for j in range(len(slice[i])):
            marked_slices[position['y'] + i][position['x'] + j] = slice_num

def add(direction, positon, slice): #Добавляем ячейку к куску
    height = len(slice)
    width = len(slice[0])
    if direction == 'r':
        for i in range(height):
            slice[i].append(pizza[positon['x']+1])
    elif direction == 'd':
        for i in range(width):
            slice[i].append(pizza[positon['y']+1])

    return slice

def check(direction, positon, slice): #Проверяем, стоит ли добавлять ячейку
    need = {'M' : params['L'], 'T' : params['L']} #Считаем, скок осталось (можно вынести
    for i in range(len(slice)):                   #в отдельную функцию)
        for j in range(len(slice[i])):
            if slice[i][j] == 'M':
                need['M'] -=1
            elif slice[i][j] == 'T':
                need['T'] -=1

    print(slice)

    if direction == 'r': #Добавить следующим if'ом проверку размера получаемого куска
        if (need['M'] > 0 and pizza[positon['x']+1] == 'M'):
            return True
        if (need['T'] > 0 and pizza[positon['x']+1] == 'T'):
            return True
    if direction == 'd':
        if (need['M'] > 0 and pizza[positon['y']+1] == 'M'):
            return True
        if (need['T'] > 0 and pizza[positon['y']+1] == 'T'):
            return True

def is_clear(cell):
    if marked_slices[cell['x']][cell['y']] == '*':
        return True
    else:
        return False


def main():
    slice = [[]]
    #slice.append([].append(0))
    for i in range(params['R']):
        for j in range(params['C']):
            if (collected(slice)):
                mark_slice({'x' : j, 'y' : i}, slice)
                print("marked {} slice".format(slice_num))
                if(is_clear(cell = {'x' : j, 'y' : i})):
                    print("processing [{},{}]".format(j,i))
                    #slice[0][0] = pizza[j][i]
                    slice.append(pizza[i][j])
            else:
                if (check('r', {'x' : j, 'y' : i}, slice)):
                    add('r', {'x' : j, 'y' : i}, slice)
                else:
                    add('r', {'x' : j, 'y' : i}, slice)






data_file = open("./small.in", "r")
params_str = data_file.readline()
params_list = params_str[:-1].split(" ")
params_list = [int(i) for i in params_list]
params_desc_list = ['R', 'C', 'L', 'H']
params = dict(zip(params_desc_list, params_list))

pizza = []

for i in range(params['R']):
    pizza.append(list(data_file.readline()[:-1]))

marked_slices = cp.deepcopy(pizza)
for i in range(params['R']):
    for j in range(params['C']):
        marked_slices[i][j] = '*'

slice_num = 0 #Номер размечаемого куска

print(pizza)
print(marked_slices)
main()

print(marked_slices)

