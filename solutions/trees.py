from queue import Queue
from typing import List, Callable
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

    def numTrees(self, n: int) -> int:
        pass


def main():
    """
        3
       /\
      -1 20
     /\  \
    -2 0   30
    """
    p = TreeNode(3)
    p.left = TreeNode(-1)
    p.right = TreeNode(20)
    p.left.left = TreeNode(-2)
    p.left.right = TreeNode(0)
    p.right.right = TreeNode(30)
    sol = Solution()
    print(sol.pathSum(p, 0))


if __name__ == '__main__':
    main()
