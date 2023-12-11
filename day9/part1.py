def solution(inp):
    history = [[int(num) for num in line.split()] for line in inp.split('\n')]
    
    def last_datapoints(l):
        end_data = [l[-1]]
        def create_differences(l):
            diff = [] 
        
            for i in range(1, len(l)):    
                diff.append(l[i] - l[i - 1])

            if (all(0 == x for x in diff)):
                return
            
            end_data.append(diff[-1])
            create_differences(diff)

        create_differences(l)
        return end_data

    data = []
    for sensor_data in history:
        data.append(last_datapoints(sensor_data))
    
    sum_extrapolation = 0
    for value in data:
        extrapolation = value[-1]
        for j in list(reversed(value))[1:]:
           extrapolation += j
        sum_extrapolation += extrapolation

    return sum_extrapolation

raw = open('input').read().rstrip()
print(solution(raw))
