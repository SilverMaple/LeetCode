import time
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeTraversal:
    def __init__(self):
        self.arr = []

    def generate_numbers(self):
        head_node = TreeNode(1)
        head_node.left = TreeNode(2)
        head_node.right = TreeNode(3)
        head_node.left.left = TreeNode(4)
        head_node.left.right = TreeNode(5)
        head_node.right.left = TreeNode(6)
        head_node.right.right = TreeNode(7)
        return head_node

    # 层次遍历
    def layerTraversal(self, root):
        queue = [root]
        arr = []
        while queue:
            node = queue.pop(0)
            if not node:
                continue
            arr.append(node.val)
            queue += [node.left, node.right]
        print(arr)

    # 递归形式先序遍历
    def preOrderTraversalRecursive(self, root):
        if not root:
            return
        self.arr.append(root.val)
        self.preOrderTraversalRecursive(root.left)
        self.preOrderTraversalRecursive(root.right)

    # 递归形式中序遍历
    def inOrderTraversalRecursive(self, root):
        if not root:
            return
        self.inOrderTraversalRecursive(root.left)
        self.arr.append(root.val)
        self.inOrderTraversalRecursive(root.right)

    # 递归形式后序遍历
    def postOrderTraversalRecursive(self, root):
        if not root:
            return
        self.postOrderTraversalRecursive(root.left)
        self.postOrderTraversalRecursive(root.right)
        self.arr.append(root.val)
    
    # 非递归形式先序遍历
    def preOrderTraversal(self, root):
        stack = [root]
        arr = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            arr.append(node.val)
            stack += [node.right, node.left]
        print(arr)

    # 非递归形式中序遍历
    def inOrderTraversal(self, root):
        stack = []
        cur = root
        arr = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            arr.append(node.val)
            cur = node.right
        print(arr)
    
    # 非递归形式后序遍历
    def postOrderTraversal(self, root):
        stack = [root]
        arr = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            arr.append(node.val)
            stack += [node.left, node.right]
        arr.reverse()
        print(arr)

tra = TreeTraversal()
root = tra.generate_numbers()
for f in [tra.preOrderTraversal, tra.preOrderTraversalRecursive,\
        tra.inOrderTraversal, tra.inOrderTraversalRecursive,\
        tra.postOrderTraversal, tra.postOrderTraversalRecursive,\
        tra.layerTraversal]:
    if 'Recursive' in f.__name__:
        tra.arr = []
    print('-'*50)
    print(f.__name__.replace('_', ' ').capitalize())
    start_time = time.time()
    f(root)
    if 'Recursive' in f.__name__:
        print(tra.arr)
    print('cost: ' + str(time.time()-start_time))
