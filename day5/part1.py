def solution(inp):
    sections = [section for section in inp.split('\n\n')]
    maps = [sections.split(':')[1].strip() for sections in sections]
    seeds = maps[0].split()
    maps = [x.split('\n') for x in maps[1:]]
    maps = [[y.split() for y in x] for x in maps]
    mappings = []
    for i in maps:
        map_range = []
        for j in i:
            source = int(j[1])
            destination = int(j[0])
            amount = int(j[2]) - 1
            map_range.append([source, source + amount, destination, amount])
    
        mappings.append(map_range)

    locations = []
    for i in seeds:
        map_input = int(i)
        for j in mappings:
            for k in j:
                if (k[0] < map_input < k[1]):
                    map_input = map_input + -(k[0] - k[2])
                    break
                elif (k[0] == map_input):
                    map_input = k[2]
                    break
                elif (k[1] == map_input):
                    map_input = k[2] + k[3]
                    break

        locations.append(map_input)
                
    return(min(locations))


raw = open('input').read().rstrip()
print(solution(raw))



# Attempt 1
# def solution(inp):
#     sections = [section for section in inp.split('\n\n')]
#     maps = [sections.split(':')[1].strip() for sections in sections]
#     seeds = maps[0].split()
#     maps = [x.split('\n') for x in maps[1:]]
#     maps = [[y.split() for y in x] for x in maps]
#     mappings = []
#     for i in maps:
#         dic = {}
#         for j in i:
#             destination = int(j[0])
#             source = int(j[1])
#             amount = int(j[2])
#             x = list(range(source, source + amount))
#             y = list(range(destination, destination + amount))
#             for i in range(len(x)):
#                 dic[x[i]] = y[i]
# 
#         mappings.append(dic)
# 
#     locations = []
#     for i in seeds:
#         map_input = int(i)
#         for j in range(7):
#             if map_input in mappings[j]:
#                 map_input = mappings[j][map_input]
#             else:
#                 continue
#         locations.append(map_input)
# 
#     return min(locations)
