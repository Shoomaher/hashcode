"""
Google Hashcode online qualification 2k17
"""
from collections import OrderedDict
import numpy as np

#DATA_FILE = open('./kittens.in', 'r')
#DATA_FILE = open('./data.in', 'r')
DATA_FILE = open('./trending_today.in', 'r')
#DATA_FILE = open('./videos.in', 'r')
#DATA_FILE = open('./small_test.in', 'r')
params_str = DATA_FILE.readline()
videos_str = DATA_FILE.readline()
videos_list__ = videos_str[:-1].split(" ")
videos_list = [int(i) for i in videos_list__]
videos_sizes = dict(zip(range(len(videos_list)), videos_list))
params_list__ = params_str[:-1].split(" ")
params_list = [int(i) for i in params_list__]

keys_list = ['V', 'E', 'R', 'C', 'X']
params = dict(zip(keys_list, params_list))

endpoints = dict.fromkeys(range(params['E']))

for i in range(params['E']):
    line = DATA_FILE.readline()[:-1].split(" ")
    endpoints[i] = dict(dcenter_lat=int(line[0]), vid_requests={}, cache_lat={})
    for a in range(int(line[1])):
        line = DATA_FILE.readline()[:-1].split(" ")
        if len(line) == 3:
            break
        endpoints[i]['cache_lat'][int(line[0])] = int(line[1])

for i in range(params['V']):
    line = DATA_FILE.readline()[:-1].split(" ")
    endpoints[int(line[1])]['vid_requests'][int(line[0])] = int(line[2])

videos_rate = np.empty(shape=(params['V'], params['E']))
videos_rate[:] = np.NaN

for e in endpoints.keys():
    for v in endpoints[e]['vid_requests'].keys():
        videos_rate.itemset((v, e), endpoints[e]['vid_requests'][v])

vid_rate = dict.fromkeys(range(params['V']))
for vid in range(params['V']):
    rate = 0
    for end in range(params['E']):
        if np.isnan(videos_rate[vid, end]):
            continue
        rate += videos_rate[vid, end]
    vid_rate[vid] = int(rate)

vid_rate = dict(OrderedDict(sorted(vid_rate.items(), key=lambda t: t[1], reverse = True)))
#Рейтинг видео по количеству запросов (не знаю, зачем делал)

for e in range(params['E']):
    #Сортируем словарь с запросами видео по видеороликам с наибольшим количество запросов
    endpoints[e]['vid_requests'] = dict(OrderedDict(sorted(endpoints[e]['vid_requests'].items(), key = lambda t: t[1], reverse = True)))
    #Тоже самое, но с кэш-серверами
    endpoints[e]['cache_lat'] = dict(OrderedDict(sorted(endpoints[e]['cache_lat'].items(), key = lambda t: t[1])))

caches = dict.fromkeys(range(params['C']))
for i in range(params['C']):
    caches[i] = dict(videos=[], size_left=params['X'])
    #Кэш-сервера: массив с номерами хранимых видео и оставшийся размер

left_in_dc = {k: [] for k in range(params['E'])}
# [endpoint] = n_video Какие видео оставим в дата-центре
#и от каких endpoint'ов будут к ним идти запросы

for e in range(params['E']):
    f = 0
    for vid in range(len(endpoints[e]['vid_requests'])):
        for server in list(endpoints[e]['cache_lat']):
            if endpoints[e]['cache_lat'][server] > endpoints[e]['dcenter_lat']:
                #Если задержка к кэшу больше, чем задержка
                #к дата-центру (массив уже отсортирован)
                if vid not in left_in_dc[e]:
                    left_in_dc[e].append(vid)
                    break

            if caches[server]['size_left'] > videos_sizes[vid]: #Если есть место под видео, то...
                if vid not in left_in_dc[e]:
                    caches[server]['videos'].append(vid)
                    caches[server]['size_left'] -= videos_sizes[vid]
                    brea
        for server in list(endpoints[e]['cache_lat']):
            if vid in caches[server]['videos']:
                f = 1
                break

        if (vid not in left_in_dc[e] and f != 1):
            #Если так видео никуда не распределили
            #и до этого не решили оставить его в дата-центре, оставляем
            left_in_dc[e].append(vid)

#Пытаемся раскинуть оставшиеся (авось, что получится):
for e in range(params['E']):
    if left_in_dc[e]:
        for vid in left_in_dc[e]:
            for server in list(endpoints[e]['cache_lat']):
                if endpoints[e]['cache_lat'][server] < endpoints[e]['dcenter_lat']:
                    if caches[server]['size_left'] > videos_sizes[vid]:
                        print("Получилось!")
                        caches[server]['videos'].append(vid)
                        caches[server]['size_left'] -= videos_sizes[vid]
                        left_in_dc[e].remove(vid)
                        break

#Честно говоря, уже не помню, зачем я это пилил. Безумно хочу спать
'''
print("Caches:")
print(caches)

print("Left in data center:")
for e in range(params['E']):
    if left_in_dc[e]:
        print(left_in_dc[e])
'''

result_file = open('./result.out', 'w')
result_file.write("{}\n".format(len(caches.keys())))
for i in caches.keys():
    result_file.write(str(i))
    for a in caches[i]['videos']:
        result_file.write(" " + str(a))
    result_file.write("\n")

result_file.close()
