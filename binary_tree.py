from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def deserialize_pre_order(arr):
    def build_tree(q):
        if not q:
            return None
        val = q.popleft()
        if val == -1:
            return None
        root = Node(val)
        root.left = build_tree(q)
        root.right = build_tree(q)
        return root
    return build_tree(deque(arr))

def serialize_pre_order(root, A):
    if not root:
        A.append(-1)
        return
    A.append(root.val)
    serialize_pre_order(root.left, A)
    serialize_pre_order(root.right, A)


if __name__ == '__main__':
    pre_order_arr = [1, 2, 4, -1, -1, -1, 3, -1, -1]
    root = deserialize_pre_order(pre_order_arr)
    A = []
    serialize_pre_order(root, A)
    print(A == pre_order_arr)
