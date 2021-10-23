from main import initial_node, p
from problem import Node
from solution import Solution

solution = Solution()


def opposite_action(action):
    if action == 'right':
        return 'left'
    elif action == 'left':
        return 'right'
    elif action == 'up':
        return 'down'
    elif action == 'down':
        return 'up'


def find_path(q1, q2):
    path1 = []
    depth1 = 0
    while q1.parent:
        depth1 += 1
        path1.insert(0, q1.action)
        q1 = q1.parent
    path2 = []
    depth2 = 0
    while q2.parent:
        depth2 += 1
        path2.append(opposite_action(q2.action))
        q2 = q2.parent
    return path1 + path2, depth1+depth2


def find_parent(q):
    while q.parent:
        q = q.parent
    return q
      

def bidirectional_search(problem):
    solution.num_node_produced = 1 + len(problem.goals)

    node_forward = initial_node

    # Q in fact is frontier queue
    Q_forward = [node_forward]
    Q_backward = []

    for goals in problem.goals:
        s = goals
        x, y = problem.find_x_and_y(s)
        h = problem.heuristic(s)
        node_backward = Node(s, 0, x, y, None, h, 'end')
        Q_backward.append(node_backward)

    # mark in fact is explored set
    mark_forward = [node_forward.state]
    mark_backward = []
    for goals in problem.goals:
        mark_backward.append(goals)

    while Q_forward and Q_backward:
        x = Q_forward.pop(0)
        if x.state in problem.goals or x.state in list(map(lambda z: z.state, Q_backward)):
            for q in Q_backward:
                if q.state == x.state:
                    solution.path, solution.depth = find_path(x, q)
                    solution.print_goal(find_parent(q).state)
                    solution.print_solution()
                    return 'success'

        solution.num_node_expanded += 1
        for action in problem.actions(x):
            node = x.child_node(problem, x, action)
            state = node.state

            if not mark_forward.__contains__(state):
                solution.num_node_produced += 1
                mark_forward.append(state)
                Q_forward.append(node)

        y = Q_backward.pop(0)
        if y.state == initial_node.state or y.state in list(map(lambda f: f.state, Q_forward)):
            for q in Q_forward:
                if q.state == y.state:
                    solution.path, solution.depth = find_path(q, y)
                    solution.print_goal(find_parent(y).state)
                    solution.print_solution()
                    return 'success'

        solution.num_node_expanded += 1
        for action in problem.actions(y):
            node = y.child_node(problem, y, action)
            state = node.state

            if not mark_backward.__contains__(state):
                solution.num_node_produced += 1
                mark_backward.append(state)
                Q_backward.append(node)

    return 'failure'


print(bidirectional_search(p))
