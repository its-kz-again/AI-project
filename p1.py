from main import p, initial_node
from solution import Solution

initial_depth = int(input('please input initial depth:'))
solution = Solution()


def recursive_dls(node, problem, limit):
    if problem.goal_test(node.state):
        solution.print_goal(node.state)
        depth = 0
        path = []
        while node.parent:
            depth += 1
            path.insert(0, node.action)
            node = node.parent
        solution.depth = depth
        solution.path = path
        solution.print_solution()
        exit()

    if limit == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False

        solution.num_node_produced += len(problem.actions(node))
        solution.num_node_expanded += 1
        for action in problem.actions(node):
            child = node.child_node(problem, node, action)

            # print(limit)
            # for i in child.state:
            #     print(i)
            # print('---------------------------')

            result = recursive_dls(child, problem, limit - 1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result != 'failure':
                return result
        if cutoff_occurred:
            return 'cutoff'
        else:
            return 'failure'


def dls(problem, limit):
    return recursive_dls(initial_node, problem, limit)


def ids(problem):
    global initial_depth
    depth = initial_depth
    while True:
        result = dls(p, depth)
        if result != 'cutoff':
            return result
        depth += 1


ids(p)

