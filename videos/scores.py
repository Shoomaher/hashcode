import argparse
from tqdm import tqdm

def win(inputfile):
    for en in inputfile['endpoints']:
        for con in en['connections']:
            con['lat'] = en['data_lat'] - con['lat']
    return inputfile

def read_file(path):
    with open(path, 'r') as reader:


        count_videos, count_endpoints, count_requests, count_caches, storage_cache = [int(i) for i in reader.readline().split(" ")]

        video_sizes = [int(i) for i in reader.readline().split(" ")]
        endpoints = []
        for eid in tqdm(range(count_endpoints), desc="Reading endpoints"):
            data_lat, connected_caches = [int (i) for i in reader.readline().split(" ")]
            connections = []

            for cnumb in range(connected_caches):
                number_cache, lat_cache = [int (i) for i in reader.readline().split(" ")]
                connections.append({'id':number_cache, 'lat': lat_cache})

            endpoints.append({'id': eid, 'data_lat': data_lat, 'connections': connections, 'requests':[]})


        for rid in tqdm(range(count_requests), desc="Reading requests"):
            number_video, eid, requests = [int(i) for i in reader.readline().split(" ")]
            endpoints[eid]['requests'].append({'number_video': number_video, 'count_requests': requests})

        return {
            'count_videos': count_videos,
            'count_endpoints': count_endpoints,
            'count_requests': count_requests,
            'count_caches': count_caches,
            'storage_cache': storage_cache,
            'video_sizes': video_sizes,
            'endpoints': endpoints
        }

parser = argparse.ArgumentParser()

parser.add_argument("input", help="input file")
parser.add_argument("output", help="output file")
args = parser.parse_args()

inputfile = read_file(args.input)
inputfile= win(inputfile)
with open(args.output, 'r') as reader:
    count_caches = int(reader.readline())
    caches = []
    for i in tqdm(range(count_caches), desc='read output'):
        line = reader.readline().split(" ")
        id = int(line[0])
        videos = []
        line.remove(line[0])
        for v in line:
            videos.append(int(v))
        caches.append({'id': id, 'videos': videos})

    score = 0
    print(inputfile)
    for end in tqdm(inputfile['endpoints'], desc='counting scores'):
        for req in end['requests']:
            variants = []
            variants.append(0)
            for c in caches:
                for v in c['videos']:
                    if v == req['number_video']:
                        for con in end['connections']:
                            if con['id'] == c['id']:
                                variants.append(con['lat']*req['count_requests'])
            variants.sort(reverse=1)
            score+=variants[0]
    print("Scores: ", score)
