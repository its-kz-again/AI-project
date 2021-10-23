class Solution:
    def __init__(self):
        self.depth = 0
        self.path = []
        self.num_node_produced = 0
        self.num_node_expanded = 0

    @staticmethod
    def print_goal(state):
        print('----------------------------')
        print('goal :')
        print()
        for row in state:
            for r in row:
                if r != '#':
                    print(str(r[0])+r[1], end=' ')
                else:
                    print('#', end=' ')
            print()
        print('----------------------------')

    def print_solution(self):
        print('depth :', self.depth)
        print('path :', end=' ')
        if not len(self.path):
            print()
        for p in self.path:
            print(p)
        print('number of produced node :', self.num_node_produced)
        print('number of expanded node :', self.num_node_expanded)
        print('----------------------------')
