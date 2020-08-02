from .tree_node import TreeNode


def generateTrees(n: int):
    if not n:
        return []
    return recursiveTrees([_ + 1 for _ in range(n)])


def recursiveTrees(numsList):
    """recursively calculates all possible binary trees given a list
    of values. Solutions traverse towards the base case where rT
    call catches an empty list; at this point, the left and right
    sides of each tree are combined for all possible permutations,
    adopted to the node they were called upon, and that node is added
    to the return list. This process continues back upwards until
    the origincal call is achieved. """
    if not numsList:
        return [None]
    uniqueSubTrees = []
    for num in range(len(numsList)):
        for right in recursiveTrees(numsList[num+1:]):
            for left in recursiveTrees(numsList[:num]):
                node = TreeNode(val=numsList[num])
                node.left, node.right = left, right
                uniqueSubTrees.append(node)
    return uniqueSubTrees
