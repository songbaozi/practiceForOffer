# print("哈哈，很开心，我们的笔记本又可以用了，真的很开心，能够愉快的敲代码了，我很开心，试了一下，感觉很爽，这个笔记本花费了我6000多元,我要好好利用这个笔记本")

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def findPath(self,root):
        onepath = ''
        ret = []
        self.dfs(root,onepath,ret)
        return ret


    def dfs(self,root,onepath,ret):
        if not root:
            return
        if not root.left and not root.right:
            ret.append(onepath + str(root.val))

        else:
            self.dfs(root.left,onepath+str(root.val)+'->',ret)
            self.dfs(root.right,onepath+str(root.val)+'->',ret)


root = TreeNode(10)
node5 = TreeNode(5);node12 = TreeNode(12)
node7 = TreeNode(7);node4 = TreeNode(4)
root.left = node5;root.right = node12
node5.left = node7;node5.right = node4

s = Solution()
ret = s.findPath(root)
print(ret)