import queue
import sys


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printInOrderTraversal(root):
    printInOrderTraversalH(root)
    print()


def printInOrderTraversalH(root):
    if root is None:
        return
    printInOrderTraversalH(root.left)
    print(root.val, end=" ")
    printInOrderTraversalH(root.right)
    return


def printPostOrderTraversal(root):
    printPostOrderTraversalH(root)
    print()


def printPostOrderTraversalH(root):
    if root is None:
        return
    printPostOrderTraversalH(root.left)
    printPostOrderTraversalH(root.right)
    print(root.val, end=" ")
    return


def printPreOrderTraversal(root):
    printPreOrderTraversalH(root)
    print()


def printPreOrderTraversalH(root):
    if root is None:
        return
    print(root.val, end=" ")
    printPreOrderTraversalH(root.left)
    printPreOrderTraversalH(root.right)
    return


def takeLevelWiseTreeInput():
    x = list(map(int, sys.stdin.readline().strip().split()))
    root = BinaryTreeNode(x[0])
    q = queue.Queue()
    q.put(root)
    i = 0
    while not (q.empty()):
        r = q.get()
        left_child = x[i + 1]
        i += 1
        right_child = x[i + 1]
        i += 1
        if left_child != -1:
            r.left = BinaryTreeNode(left_child)
            q.put(r.left)
        else:
            pass
        if right_child != -1:
            r.right = BinaryTreeNode(right_child)
            q.put(r.right)
        else:
            pass
    return root


def printTreeLevelWise(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    q.put("\n")
    while not q.empty():
        x = q.get()
        if x is None:
            break
        if x == "\n":
            q.put("\n")
            print()
            continue
        print(x.val, end=" ")
        q.put(x.left)
        q.put(x.right)
    print()
    return None


def LCA(root, p, q):
    return LCAH(root, p, q)


def LCAH(root, p, q):
    if root is None:
        return

    if root == p or root == q:
        return root

    sal = LCAH(root.left, p, q)
    sar = LCAH(root.right, p, q)

    if sal and sar:
        return root
    if sal is not None:
        return sal
    else:
        return sar


root = takeLevelWiseTreeInput()
printTreeLevelWise(root)
printPreOrderTraversal(root)
printPostOrderTraversal(root)
printInOrderTraversal(root)

LCA(root, root.left.left, root.left.right)
