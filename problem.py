import math
from copy import deepcopy
from itertools import permutations


class Node:
    def __init__(self, state, g, x, y, parent, h, action):
        self.state = state
        self.parent = parent
        self.G = g
        self.H = h
        self.F = max(g + h, parent.G + parent.H if parent is not None else 0)
        self.x = x
        self.y = y
        self.action = action

    def child_node(self, problem, parent, action):
        p = deepcopy(parent.state)
        s, x, y = problem.result(p, action, self.x, self.y)
        g = parent.G + 1
        h = problem.heuristic(s)
        return Node(s, g, x, y, parent, h, action)

    def __eq__(self, other):
        return other == self.state

    def __hash__(self):
        return hash(self.state.__str__())


class Problem:
    def __init__(self, initial, n, m):
        self.initial_state = initial
        self.n = n
        self.m = m
        self.order_set = {}
        self.goals = []

    # check that the state in argument is goal or no
    def goal_test(self, state):
        if state in self.goals:
            return True
        else:
            return False

    @staticmethod
    def result(state, action, x, y):
        if action == 'left':
            jafar = state[x][y]
            state[x][y] = state[x][y - 1]
            state[x][y - 1] = jafar
            y = y - 1
            return state, x, y
        elif action == 'right':
            jafar = state[x][y]
            state[x][y] = state[x][y + 1]
            state[x][y + 1] = jafar
            y = y + 1
            return state, x, y
        elif action == 'up':
            jafar = state[x][y]
            state[x][y] = state[x - 1][y]
            state[x - 1][y] = jafar
            x = x - 1
            return state, x, y
        else:
            jafar = state[x][y]
            state[x][y] = state[x + 1][y]
            state[x + 1][y] = jafar
            x = x + 1
            return state, x, y

    def actions(self, node):
        x = node.x
        y = node.y
        if x == 0 and y == 0:
            return ['right', 'down']
        elif x == self.n - 1 and y == 0:
            return ['right', 'up']
        elif x == 0 and y == self.m - 1:
            return ['left', 'down']
        elif x == self.n - 1 and y == self.m - 1:
            return ['left', 'up']
        elif x == 0:
            return ['down', 'right', 'left']
        elif y == 0:
            return ['right', 'down', 'up']
        elif x == self.n - 1:
            return ['left', 'right', 'up']
        elif y == self.m - 1:
            return ['left', 'down', 'up']

        return ['left', 'right', 'up', 'down']

    def heuristic(self, state):
        heuristics = []
        for goal in self.goals:
            h = 0
            for x_goal, rows_goal in enumerate(goal):
                for y_goal, r_g in enumerate(rows_goal):
                    for x_state, rows_state in enumerate(state):
                        for y_state, r_s in enumerate(rows_state):
                            if r_s == r_g:
                                h += abs(x_goal - x_state) + abs(y_goal - y_state)

            heuristics.append(h - 1 if h != 0 else 0)

        # print(heuristics)
        # print(min(heuristics))
        return min(heuristics)

    def find_sample_goal(self):
        order_set = self.order_set

        # creat sample goal
        sample = []
        for i in range(self.n):
            row_sample = []
            for row in deepcopy(self.initial_state):
                for r in row:
                    if r.__contains__(order_set[i]):
                        row_sample.append(r)
            row_sample.sort()
            sample.append(row_sample[::-1])

        x = 0
        y = 0
        for index, row in enumerate(sample):
            if len(row) != self.m:
                row.insert(0, '#')
                x = index

        # print(sample)
        return sample, x, y

    def sort_classes(self):
        checking_set = set()
        order_set = {}
        lst = []
        for row in deepcopy(self.initial_state):
            lst.append(list(map(lambda x: x[1] if x != '#' else None, row)))
            for r in row:
                if r != '#':
                    checking_set.add(r[1])

        order_checking_list = []
        for cls in checking_set:
            counts = []
            for l in lst:
                counts.append(l.count(cls))
            maxi = max(counts)
            order_checking_list.append([cls, maxi])

        order_checking_list.sort(key=lambda x: x[1])

        while order_checking_list:
            cls = order_checking_list.pop()[0]
            counts = []
            for l in lst:
                counts.append(l.count(cls))

            in_loop = True
            while in_loop:
                index = counts.index(max(counts))

                if order_set.keys().__contains__(index):
                    counts[index] = -1
                else:
                    order_set[index] = cls
                    in_loop = False

        # print(order_set)
        self.order_set = order_set
        # return order_set

    # create all goals
    def create_goals(self):
        state = self.initial_state
        name_class = self.order_set.values()
        classes = dict()
        for cls in name_class:
            classes[cls] = []

        for rows in state:
            for r in rows:
                if r != '#':
                    classes[r[1]].append(r[0])

        for v in classes.values():
            v.sort()
            v.reverse()

        sample_goal = []
        for k, v in classes.items():
            sample_row = []
            if len(v) != self.m:
                sample_row.append('#')
            for values in v:
                sample_row.append([values, k])
            sample_goal.append(sample_row)

        self.goals = [list(goal) for goal in permutations(sample_goal)]

    @staticmethod
    def find_x_and_y(state):
        for i, row in enumerate(state):
            for j, r in enumerate(row):
                if r == '#':
                    return i, j
