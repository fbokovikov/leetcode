from queue import Queue
from typing import List, Callable, Dict
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None \
                or p is not None and q is None \
                or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            if abs(left_height - right_height) > 1:
                return False
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is not None and root.right is not None:
            return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
        elif root.left:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + self.minDepth(root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSymmetricPair(root.left, root.right)

    def isSymmetricPair(self, left_root: TreeNode, right_root: TreeNode):
        if not (left_root or right_root):
            return True
        if not (left_root and right_root):
            return False
        if left_root.val != right_root.val:
            return False
        return self.isSymmetricPair(left_root.left, right_root.right) \
               and self.isSymmetricPair(left_root.right, right_root.left)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodes = deque()
        nodes.append(root)
        result = list()
        level_nodes = list()
        while nodes:
            node = nodes.popleft()
            level_nodes.append(node)
            if not nodes and level_nodes:
                result.append([n.val for n in level_nodes])
                for level_node in level_nodes:
                    if level_node.left:
                        nodes.append(level_node.left)
                    if level_node.right:
                        nodes.append(level_node.right)
                level_nodes.clear()
        return result

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        nodes = dict()
        self.addNode(root, 1, nodes)
        levels = nodes.keys()
        result = []
        for level in sorted(levels, reverse=True):
            result.append(nodes[level])
        return result

    def addNode(self, node: TreeNode, level: int, nodes):
        if node is None:
            return
        if level in nodes:
            nodes[level].append(node.val)
        else:
            nodes[level] = [node.val]
        self.addNode(node.left, level + 1, nodes)
        self.addNode(node.right, level + 1, nodes)

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        nodes = deque()
        nodes.append(root)
        zigzag = False
        while len(nodes) > 0:
            cur_level = []
            for idx in range(len(nodes)):
                node = nodes.popleft()
                cur_level.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if not zigzag:
                res.append(cur_level)
            else:
                res.append(list(reversed(cur_level)))
            zigzag = not zigzag
        return res

    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_node(root, None, None)

    def is_valid_node(self, node: TreeNode, lower_limit, upper_limit) -> bool:
        if node is None:
            return True
        if lower_limit is not None and node.val <= lower_limit:
            return False
        if upper_limit is not None and node.val >= upper_limit:
            return False
        return self.is_valid_node(node.left, lower_limit, node.val) \
            and self.is_valid_node(node.right, node.val, upper_limit)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(node: TreeNode):
            if node is None:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)

        res = []
        helper(root)
        return res

    def inorderTraversalNonRecursive(self, root: TreeNode) -> List[int]:
        res, nodes = list(), list()
        cur = root
        while cur is not None or len(nodes) > 0:
            while cur is not None:
                nodes.append(cur)
                cur = cur.left
            cur = nodes.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def helper(node: TreeNode, sum: int, cur_path: List[int]):
            if node is None:
                return
            cur_path.append(node.val)
            if node.val == sum and node.left is None and node.right is None:
                res.append(cur_path)
            helper(node.left, sum - node.val, list(cur_path))
            helper(node.right, sum - node.val, list(cur_path))
        res = []
        helper(root, sum, [])
        return res

    def pathSum3(self, root: TreeNode, sum: int) -> int:
        def helper(node: TreeNode, sum: int):
            if node is None:
                return
            if node.val == sum:
                res[0] += 1
            helper(node.left, sum - node.val)
            helper(node.right, sum - node.val)

        def helper2(node: TreeNode, sum: int):
            if node is None:
                return
            helper(node, sum)
            helper2(node.left, sum)
            helper2(node.right, sum)
        res = [0]
        helper2(root, sum)
        return res[0]

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        invert_root = TreeNode(root.val)
        self.mirror_nodes(root, invert_root)
        return invert_root

    def mirror_nodes(self, root: TreeNode, invert_root: TreeNode):
        if root.left is not None:
            invert_root.right = TreeNode(root.left.val)
            self.mirror_nodes(root.left, invert_root.right)
        if root.right is not None:
            invert_root.left = TreeNode(root.right.val)
            self.mirror_nodes(root.right, invert_root.left)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def helper(node: TreeNode, cur_path: List[int]):
            if node.left is None and node.right is None:
                cur_path_str = "->".join(str(x) for x in cur_path + [node.val])
                res.append(cur_path_str)
            if node.left is not None:
                helper(node.left, cur_path + [node.val])
            if node.right is not None:
                helper(node.right, cur_path + [node.val])
        res = []
        if root is not None:
            helper(root, [])
        return res

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_val = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            left_val = root.left.val
        return left_val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node: TreeNode, cur_sum: int):
            if node is None:
                return
            if node.left is None and node.right is None:
                res[0] += cur_sum + node.val
            cur_sum += node.val
            helper(node.left, cur_sum * 10)
            helper(node.right, cur_sum * 10)

        res = [0]
        helper(root, 0)
        return res[0]

    def numTrees(self, n: int) -> int:
        num_trees = [0] * (n + 1)
        num_trees[0], num_trees[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(0, i):
                num_trees[i] += num_trees[j] * num_trees[i - j - 1]
        return num_trees[n]

    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.constructTrees(1, n)

    def findMode(self, root: TreeNode) -> List[int]:
        nodes_dict = {}

        def dfs(node: TreeNode):
            if node is None:
                return
            if node.val not in nodes_dict:
                nodes_dict[node.val] = 1
            else:
                nodes_dict[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        max_value = 0
        res = []
        dfs(root)
        for node_value in nodes_dict.keys():
            if nodes_dict[node_value] == max_value:
                res.append(node_value)
            if nodes_dict[node_value] > max_value:
                res = [node_value]
                max_value = nodes_dict[node_value]
        return res

    def constructTrees(self, start, end):

        list = []

        """ if start > end then subtree will be  
            empty so returning None in the list """
        if (start > end):
            list.append(None)
            return list

        """ iterating through all values from  
            start to end for constructing 
            left and right subtree recursively """
        for i in range(start, end + 1):

            """ constructing left subtree """
            leftSubtree = self.constructTrees(start, i - 1)

            """ constructing right subtree """
            rightSubtree = self.constructTrees(i + 1, end)

            """ now looping through all left and  
                right subtrees and connecting  
                them to ith root below """
            for j in range(len(leftSubtree)):
                left = leftSubtree[j]
                for k in range(len(rightSubtree)):
                    right = rightSubtree[k]
                    node = TreeNode(i)  # making value i as root
                    node.left = left  # connect left subtree
                    node.right = right  # connect right subtree
                    list.append(node)  # add this tree to list
        return list



def main():
    """
        3
       /\
      1 2
     /\  \
    2 0   3
    """
    p = TreeNode(1)
    p.left = TreeNode(4)
    p.right = TreeNode(5)
    p.left.left = TreeNode(4)
    p.left.left.left = TreeNode(5)
    sol = Solution()
    print(sol.findMode(p))


if __name__ == '__main__':
    main()
