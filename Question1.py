from collections import deque

def bfs_maze(start, target, maze):
    rows = len(maze)
    cols = len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        x, y = current

        if current == target:
            return path + [current]

        visited.add(current)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 1 <= nx <= rows and 1 <= ny <= cols and maze[nx - 1][ny - 1] == 1 and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [current]))

    return None

######################## Start #########################

file = input('파일의 경로를 입력하세요(FTW_input.txt) : ')

with open(file, 'r') as file:
    start = 0
    question_list = []
    for line in file:
        if start == 0:
        #if start != 100:
            values = line.strip().split(',')
            values = [int(x) for x in values]
            
            tmp_l = []
            for x in range(0, len(values), 2):
                tmp = [values[x], values[x+1]]
                tmp_l.append(tmp)
    
            node_list = tmp_l
            start += 1
            #print(node_list)  
            
        else:
            values = line.strip().split('. ')[1:]
            values = values[0].strip().split(',')
            values = [int(x) for x in values]
            
            tmp_l = []
            for x in range(0, len(values), 2):
                tmp = (values[x], values[x+1])
                tmp_l.append(tmp)
    
            globals()[f'q{start}'] = tmp_l
            question_list.append(globals()[f'q{start}'])
    
            #print(globals()[f'q{start}']) 
            start += 1
        

maze = [[0] * max([max(x) for x in node_list]) for _ in range(max([max(x) for x in node_list]))]
obstacles = node_list

for obstacle in obstacles:
    x, y = obstacle
    maze[x - 1][y - 1] = 1

write_file = open('FTW_output.txt', 'w')

for idx, question in enumerate(question_list):
    start = question[0]
    target = question[1]
    path = bfs_maze(start, target, maze)
    if path:
        write_file.write(f"{idx+1}. {','.join([','.join(map(str, x)) for x in path])}\n")
    else:
        write_file.write(f"{idx+1}. NONE\n")

write_file.close()
