import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, dataList):
        self.data = max(dataList,key=lambda x:x[1])

        self.left = None
        self.right = None
        leftList = list(filter(lambda x:x[0] < self.data[0], dataList))
        rightList = list(filter(lambda x:x[0] > self.data[0], dataList))

        if leftList != []:
            self.left = Tree(leftList)

        if rightList != []:
            self.right = Tree(rightList)

def fix(node, postList,preList):
    postList.append(node.data)
    if node.left is not None:
        fix(node.left, postList, preList)
    
    if node.right is not None:
        fix(node.right, postList, preList)
    
    preList.append(node.data)


def solution(nodeinfo):
    answer = []
    root = Tree(nodeinfo)
    postList = []
    preList = []

    fix(root, postList, preList)
    answer.append(list(map(lambda x: nodeinfo.index(x)+1, postList)))
    answer.append(list(map(lambda x: nodeinfo.index(x)+1, preList)))
    return answer

a = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(a))