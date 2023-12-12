pipes = {
        'L': ((0, -1), (1, 0)),
        'J': ((0, -1), (-1, 0)),
        '7': ((0, 1), (-1, 0)),
        'F': ((0, 1), (1, 0)),
        '|': ((0, 1), (0, -1)),
        '-': ((-1, 0), (1, 0))
    }

def solution(inp):
    lines = [line for line in inp.split('\n')]
    grid = {}
    start = None
    for y, row in enumerate(lines):
        for x, symbol in enumerate(row):
            grid[(x, y)] = symbol
            if (symbol == 'S'):
                start = (x, y)

    start_symbol = find_start_pipe(start, grid)
    grid[start] = start_symbol

    current_pipe = add_tuples(start, pipes[grid[start]][0])
    prev_pipe = start
    path_grid = [current_pipe]
    while (current_pipe != start):
        for connection in pipes[grid[current_pipe]]:
            if (add_tuples(current_pipe, connection) != prev_pipe):
                prev_pipe = current_pipe
                current_pipe = add_tuples(current_pipe, connection)
                break
        
        path_grid.append(current_pipe)

    interior = 0
    intersections = 0
    for index, coordinate in enumerate(grid):
        y = index % len(lines[0])
        if (y == 0):
            intersections = 0

        if (coordinate in path_grid):
            if ((0, -1) in pipes[grid[coordinate]]):
                intersections += 1 
            continue
        if (intersections % 2 != 0):
            interior += 1 

    return interior


def find_start_pipe(coordinates, grid):
    directions = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0),
        ]

    connections = []
    for direction in directions:
        start_neighbour = add_tuples(coordinates, direction)
        if (start_neighbour in grid and grid[start_neighbour] in pipes):
            for connection in pipes[grid[start_neighbour]]:
                if (add_tuples(start_neighbour, connection) == coordinates):
                    connections.append(direction)

    for pipe, valid_connections in pipes.items():
        if (tuple(connections) == valid_connections or tuple(reversed(connections)) == valid_connections):
            return pipe

def add_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

raw = open('input').read().rstrip()
print(solution(raw))


# Convex Hull Shenaniganery
#     hull = []
#     l = leftmost(path_grid)
#     leftMost = path_grid[l]
#     currentVertex = leftMost
#     hull.append(currentVertex)
#     nextVertex = path_grid[1]
#     index = 2
#     nextIndex = -1
#     while True:
#         c0 = currentVertex
#         c1 = nextVertex
# 
#         checking = path_grid[index]
#         c2 = checking
# 
#         crossProduct = det(currentVertex, nextVertex, checking)
#         if crossProduct < 0:
#             nextVertex = checking
#             nextIndex = index
#         index += 1
#         if index == len(path_grid):
#             if nextVertex == leftMost:
#                 break
#             index = 0
#             hull.append(nextVertex)
#             currentVertex = nextVertex
#             nextVertex = leftMost
# 
#     points = list(grid.keys())
#     inside = []
#     for point in points:
#         if (checkInside(hull, len(hull), point)):
#             inside.append(point)
#     
#     unique = list(set(inside) - set(path_grid))
#     plt.scatter(*zip(*unique))
#     plt.scatter(*zip(*hull))
#     plt.show()
#     return len(unique)
# 
# def onLine(l1, p):
#     # Check whether p is on the line or not
#     if (
#         p[0] <= max(l1[0][0], l1[1][0])
#         and p[0] >= min(l1[0][0], l1[1][0])
#         and (p[1] <= max(l1[0][1], l1[1][1]) and p[1] >= min(l1[0][1], l1[1][1]))
#     ):
#         return True
#     return False
#  
# def direction(a, b, c):
#     val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
#     if val == 0:
#         # Collinear
#         return 0
#     elif val < 0:
#         # Anti-clockwise direction
#         return 2
#     # Clockwise direction
#     return 1
#  
# def isIntersect(l1, l2):
#     # Four direction for two lines and points of other line
#     dir1 = direction(l1[0], l1[1], l2[0])
#     dir2 = direction(l1[0], l1[1], l2[1])
#     dir3 = direction(l2[0], l2[1], l1[0])
#     dir4 = direction(l2[0], l2[1], l1[1])
#  
#     # When intersecting
#     if dir1 != dir2 and dir3 != dir4:
#         return True
#  
#     # When p2 of line2 are on the line1
#     if dir1 == 0 and onLine(l1, l2[0]):
#         return True
#  
#     # When p1 of line2 are on the line1
#     if dir2 == 0 and onLine(l1, l2[1]):
#         return True
#  
#     # When p2 of line1 are on the line2
#     if dir3 == 0 and onLine(l2, l1[0]):
#         return True
#  
#     # When p1 of line1 are on the line2
#     if dir4 == 0 and onLine(l2, l1[1]):
#         return True
#  
#     return False
#  
# def checkInside(poly, n, p):
#     # When polygon has less than 3 edge, it is not polygon
#     if n < 3:
#         return False
#  
#     # Create a point at infinity, y is same as point p
#     exline = (p, (9999, p[1]))
#     count = 0
#     i = 0
#     while True:
#         # Forming a line from two consecutive points of poly
#         side = (poly[i], poly[(i + 1) % n])
#         if isIntersect(side, exline):
#             # If side is intersects ex
#             if (direction(side[0], p, side[1]) == 0):
#                 return onLine(side, p);
#             count += 1
#          
#         i = (i + 1) % n;
#         if i == 0:
#             break
#  
#     # When count is odd
#     return count & 1;
# 
# def leftmost(points):
#     minim = 0
#     for i in range(1,len(points)):
#         if points[i][0] < points[minim][0]:
#             minim = i
#         elif points[i][0] == points[minim][0]:
#             if points[i][1] > points[minim][1]:
#                 minim = i
#     return minim
# 
# def det(p1, p2, p3):
#     return (p2[0] - p1[0]) * (p3[1] - p1[1]) \
#         -(p2[1] - p1[1]) * (p3[0] - p1[0])
# 
