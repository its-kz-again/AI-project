import re
from problem import Problem, Node

n, m = map(int, input().split(' '))

initial = []
rows = []
for i in range(n):
    row = input().split(' ')
    for j, r in enumerate(row):
        l = re.split(r'[a-z]', r)[0]
        cls = re.split(r'[0-9]', r).pop()
        if l.__contains__('#') or cls == '#':
            x = i
            y = j
            rows.append('#')
        else:
            rows.append([int(l), cls])
    initial.append(rows.copy())
    rows.clear()


p = Problem(initial, n, m)
p.sort_classes()
p.find_sample_goal()
p.create_goals()
h = p.heuristic(initial)


initial_node = Node(initial, 0, x, y, None, h, 'start')


