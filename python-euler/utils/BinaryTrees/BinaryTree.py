from BTNode import *

class BinaryTree(object):
    """
    Implements a binary search tree.
    Space: O(N)
    """

    def __init__(self):
        """
        @return: empty binary tree
        """
        self.root = None
        self.count = 0

    def search(self, data):
        """
        O(log(n))
        @return: node matching search criteria or None if no match
        """
        if self.root is None:
            return None
        else:
            current = self.root
            while True:
                if data == current.data:
                    return current
                elif data < current.data:
                    if current.left is None:
                        return None
                    else:
                        current = current.left
                elif data > current.data:
                    if current.right is None:
                        return None
                    else:
                        current = current.right

    def insert(self, data, NodeType = BTNode):
        """
        O(log(n))
        @return: inserted node
        """
        if self.root is None:
            self.root = NodeType(None, data)
            return self.root
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = NodeType(current, data)
                        self.count += 1
                        return current.left
                    else:
                        current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = NodeType(current, data)
                        self.count += 1
                        return current.right
                    else:
                        current = current.right
                else:
                    return current

    def remove(self, data):
        """
        O(log(n))
        @return: value of removed node or None if nothing removed
        """
        node = self.search(data)
        if node is None:
            return

        children_count = node.children_count()
        parent = node.parent
        if children_count == 0:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            return self.remove_helper(node)
        elif children_count == 1:
            if node.left:
                child = node.left
            else:
                child = node.right
            if parent:
                if parent.left is node:
                    parent.left = child
                else:
                    parent.right = child
            return self.remove_helper(node)
        else:
            successor = self.minimum(node.right)

            if successor.parent is not node:
                successor.parent.left = None
            successor.parent = node.parent

            successor.left = node.left
            node.left.parent = successor
            successor.right = node.right
            node.right.parent = successor

            if node.parent.left is node:
                node.parent.left = successor
            else:
                node.parent.right = successor
            return self.remove_helper(node)

    def minimum(self, node):
        """
        @return: minimum of subtree rooted at node
        """
        if node is None:
            return None
        min_node = node
        while min_node.left:
            min_node = min_node.left
        return min_node

    def maximum(self, node):
        """
        @return: maximum of subtree rooted at node
        """
        if node is None:
            return None
        max_node = node
        while max_node.right:
            max_node = max_node.right
        return max_node

    def size(self):
        """
        @return: number of nodes in tree
        """
        return self.count

    def isEmpty(self):
        """
        @return: True if tree is empty, else false
        """
        return self.count == 0

    def isInternal(self, node):
        """
        @return: True if node is an internal node, else false
        """
        return not self.isExternal(node)

    def isExternal(self, node):
        """
        @return: True if node is an external/leaf node, else false
        """
        return node.left is None and node.right is None

    def isRoot(self, node):
        """
        @return: True if node is root node, else false
        """
        return node is self.root

    # equivalent to preorder
    def print_dfs(self):
        """
        Print a tree using depth first traversal from the given node.
        """
        stack = [self.root]
        while stack:
            node = stack.pop()
            print node.data
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    def print_bfs(self):
        """
        Print a tree using breadth first traversal from the given node.
        """
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print node.data
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def print_inorder(self, node = None):
        """
        Print a tree using inorder traversal from the given node.
        """
        if node is None:
            return
        self.print_inorder(node.left)
        print node.data
        self.print_inorder(node.right)

    # equivalent to dfs
    def print_preorder(self, node):
        """
        Print a tree using preorder traversal from the given node.
        """
        if node is None:
            return
        print node.data
        self.print_preorder(node.left)
        self.print_preorder(node.right)

    def print_postorder(self, node):
        """
        Print a tree using postorder traversal from the given node.
        """
        if node is None:
            return
        self.print_postorder(node.left)
        self.print_postorder(node.right)
        print node.data

    def remove_helper(self, node):
        """
        * Decrement total count of nodes in tree
        * Delete removed node object from memory

        @return: value of deleted node
        """
        self.count -= 1
        ret = node.data
        del node
        return ret

    def out(self, start_node = None):
        """
        @return: string containing visual representation of tree
        """
        if start_node == None:
            start_node = self.root
        space_symbol = " "
        spaces_count = 80
        out_string = ""
        initial_spaces_string  = space_symbol * spaces_count + "\n" 
        if not start_node:
            return "Tree is empty"
        else:
            level = [start_node]
            while (len([i for i in level if (not i is None)])>0):
                level_string = initial_spaces_string
                for i in xrange(len(level)):
                    j = (i+1)* spaces_count / (len(level)+1)
                    level_string = level_string[:j] + (str(level[i]) if level[i] else space_symbol) + level_string[j+1:]
                level_next = []
                for i in level:
                    level_next += ([i.left, i.right] if i else [None, None])
                level = level_next
                out_string += level_string                    
        return out_string