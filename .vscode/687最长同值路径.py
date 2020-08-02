class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        self.getMax(root)
        return self.res

    def getMax(self, root):
        if root == None:
            return 0
        left = self.getMax(root.left)
        right = self.getMax(root.right)
        l = r = 0
        if root.left != None and root.left.val == root.val:
            l = left + 1
        if root.right != None and root.right.val == root.val:
            r = right + 1
        self.res = max(self.res, l + r)
        return max(l, r)
