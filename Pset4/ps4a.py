# Problem Set 4A
# Name:Mohammad Toloeei
# Collaborators:No One

from tree import Node  # Imports the Node object used to construct trees

# Part A0: Data representation

# initialize
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))),
             Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)),
             Node(14, Node(12), Node(21, Node(20), Node(26))))


def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    if tree is not None:
        left_child = tree.get_left_child()
        right_child = tree.get_right_child()
        # The Node is leaf
        if left_child is None and right_child is None:
            return 0
    # The Node is not leaf
        # save the right and left child heghit subtree
        stree_right = find_tree_height(tree.get_right_child())
        stree_left = find_tree_height(tree.get_left_child())
        if left_child is not None and right_child is not None:
            return max(stree_left, stree_right) + 1
        elif right_child is not None:
            return stree_right + 1
        # left_child is not None
        else:
            return stree_left + 1


def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    if tree is not None:
        left_child = tree.get_left_child()
        right_child = tree.get_right_child()
        # The Node is leaf
        if left_child is None and right_child is None:
            return True
        # The Node is not leaf
            # save the right and left child subtree
        stree_right = tree.get_right_child()
        stree_left = tree.get_left_child()
        if left_child is not None and right_child is not None:
            # boolian for right and left child is heap or not
            is_heap_right_child = is_heap(stree_right, compare_func)
            is_heap_left_child = is_heap(stree_left, compare_func)
            if is_heap_left_child and is_heap_right_child:
                # children are ok , now it's parent time
                lchild_value = stree_left.get_value()
                rchild_value = stree_right.get_value()
                pvalue = tree.get_value()
                return compare_func(lchild_value, pvalue) and compare_func(rchild_value, pvalue)
            else:
                return False
        elif left_child is not None:
            is_heap_left_child = is_heap(stree_left, compare_func)
            if is_heap_left_child:
                lchild_value = stree_left.get_value()
                pvalue = tree.get_value()
                return compare_func(lchild_value, pvalue)
            else:
                return False
        else:
            # right_child is Not None
            is_heap_right_child = is_heap(stree_right, compare_func)
            if is_heap_right_child:
                rchild_value = stree_right.get_value()
                pvalue = tree.get_value()
                return compare_func(rchild_value, pvalue)
            else:
                return False

# max heap comparator


def compare_func(child_value, parent_value):
    if child_value < parent_value:
        return True
    return False


if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
