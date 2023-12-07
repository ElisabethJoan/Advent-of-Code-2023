def solution(inp):
    sections = [section for section in inp.split('\n\n')]
    seeds = [int(seed) for seed in sections[0].strip().split(": ")[1].split()]
    mappings = []
    for section in sections[1::]:
        raw_mappings = section.split(':')[1].strip().split('\n')
        mappings.append([[int(y) for y in x.split()] for x in raw_mappings])

    locations = []
    for i in range(0, len(seeds), 2):
        seed_ranges = [[seeds[i], seeds[i + 1] + seeds[i]]]
        mapped_inputs = []
        for mmap in mappings:
            while seed_ranges:
                start_seed, end_seed = seed_ranges.pop()
                for destination, start_source, length in mmap:
                    end_source = start_source + length
                    offset = destination - start_source
                    if end_source <= start_seed or end_seed <= start_source:
                        continue
                    if start_seed < start_source:
                        seed_ranges.append([start_seed, start_source])
                        start_seed = start_source
                    if end_source < end_seed:
                        seed_ranges.append([end_source, end_seed])
                        end_seed = end_source
                    mapped_inputs.append([start_seed + offset, end_seed + offset])
                    break
                else:
                    mapped_inputs.append([start_seed, end_seed])
            seed_ranges = mapped_inputs
            mapped_inputs = []
        locations.extend([location[0] for location in seed_ranges])

    return min(locations)

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
#         map_range = []
#         for j in i:
#             source = int(j[1])
#             destination = int(j[0])
#             amount = int(j[2]) - 1
#             map_range.append([source, source + amount, destination, amount])
#     
#         mappings.append(map_range)
# 
#     seed_seed_ranges = []
#     for i in range(0, len(seeds), 2):
#         seed_seed_ranges.extend(list(range(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]))))
#     print(seed_seed_ranges)
# 
#     locations = []
#     for i in seed_seed_ranges:
#         map_input = int(i)
#         for j in mappings:
#             for k in j:
#                 if (k[0] < map_input < k[1]):
#                     map_input = map_input + -(k[0] - k[2])
#                     break
#                 elif (k[0] == map_input):
#                     map_input = k[2]
#                     break
#                 elif (k[1] == map_input):
#                     map_input = k[2] + k[3]
#                     break
# 
#         locations.append(map_input)
#                 
#     return(min(locations))


# Attempt 2
# def solution(inp):
#     sections = [section for section in inp.split('\n\n')]
#     maps = [sections.split(':')[1].strip() for sections in sections]
#     seeds = maps[0].split()
#     maps = [x.split('\n') for x in maps[1:]]
#     maps = [[y.split() for y in x] for x in maps]
#     mappings = []
#     for i in maps:
#         map_range = []
#         for j in i:
#             source = int(j[1])
#             destination = int(j[0])
#             amount = int(j[2]) - 1
#             map_range.append([source, source + amount, destination, amount])
#     
#         mappings.append(map_range)
#     
#     locations = []
#     for l in range(0, len(seeds), 2):
#         for i in range(int(seeds[l]), int(seeds[l]) + int(seeds[l + 1])):
#             map_input = int(i)
#             for j in mappings:
#                 for k in j:
#                     if (k[0] < map_input < k[1]):
#                         map_input = map_input + -(k[0] - k[2])
#                         break
#                     elif (k[0] == map_input):
#                         map_input = k[2]
#                         break
#                     elif (k[1] == map_input):
#                         map_input = k[2] + k[3]
#                         break
# 
#             locations.append(map_input)
#                 
#     return(min(locations))
