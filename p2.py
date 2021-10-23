from main import p, initial_node
from solution import Solution


solution = Solution()


def aStar(problem):
    frontier = set()
    current = initial_node
    # Add the current node to the frontier
    frontier.add(current)
    solution.num_node_produced = 1
    # While the frontier is not empty
    while frontier:
        # Find the item in the frontier with the lowest F score
        current = min(frontier, key=lambda o: o.F)
        # If it is the item we want, return the solution
        if problem.goal_test(current.state):
            solution.print_goal(current.state)
            path = []
            while current.parent:
                solution.depth += 1
                path.insert(0, current.action)
                current = current.parent
            solution.path = path
            solution.print_solution()
            exit()

        solution.num_node_expanded += 1

        frontier.remove(current)
        for action in problem.actions(current):
            node = current.child_node(problem, current, action)
            # if node is already in the frontier
            if node in frontier:
                for child in frontier:
                    if child == node:
                        if child.F > node.F:
                            frontier.remove(child)
                            frontier.add(node)
                        break

            else:
                solution.num_node_produced += 1
                frontier.add(node)

    return 'failure'


aStar(p)
