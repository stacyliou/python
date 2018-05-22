# Original problem
# https://www.programcreek.com/2014/07/leetcode-lowest-common-ancestor-of-a-binary-tree-java/
# AGPL v3
import os
import sys
from collections import OrderedDict as odict

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def get_path(child, root, path, hash):
    if child == None or root == None:
        return path
# already visited
    if child in hash:
        del path
        path = hash[child]
        return path
# get path at root
    if root not in hash:
        path = path + [root.val]
        hash[root] = path
    else:
        path = hash[root]
# search left branch       
    if root.left:
        path = get_path(child, root.left, path, hash)
# not found in left branch        
    if child.val not in path:
        del path
        path = hash[root]
# search right branch        
    if root.right:
        path = get_path(child, root.right, path, hash)
        if child.val not in path:
            del path
            path = hash[root]
# not found in tree
    if len(path) == 1 and child not in hash:
        del path
        path = []
    return path

def get_lca(node1, node2, top, hash):
    if node1 != None and node2 != None:
        path1 = []
        path1 = get_path(node1, top, path1, hash)
        print(path1)
        path2 = []
        path2 = get_path(node2, top, path2, hash)
        print(path2)
        s1 = odict.fromkeys(path1)
        s2 = odict.fromkeys(path2)
        overlapc = odict.fromkeys(x for x in s2 if x in s1)
        overlap = list(overlapc)
        del path1, path2, s1, s2, overlapc
        if len(overlap) != 0:
            lca = overlap[-1:]
            del overlap
            return lca
    return None
    
def gen_test():  
    tree = Node(26)
    tree.left      = Node(10)
    tree.right     = Node(5)
    tree.left.left  = Node(4)
    tree.left.right  = Node(6)
    tree.left.left.right  = Node(30)
    tree.right.right  = Node(3)
    tree.right.right.left = Node(12)
    tree.right.right.left.left = Node(7)
    tree.right.right.left.right = Node(9)
    return tree

if __name__ == '__main__':
    tree = gen_test()
    thash = {}
    achild = Node(100)
    print('achild = '+str(achild.val))
    bchild = tree.right.right
    print('bchild = '+str(bchild.val))
    lca = get_lca(achild, bchild, tree, thash)
    print(lca)
    del lca
