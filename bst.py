class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root=Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.left_child==None:
                curr_node.left_child = Node(value)
                curr_node.left_child.parent=curr_node
            else:
                self._insert(value, curr_node.left_child)
        elif value > curr_node.value:
            if curr_node.right_child==None:
                curr_node.right_child = Node(value)
                curr_node.right_child.parent=curr_node
            else:
                self._insert(value, curr_node.right_child)
        else:
            print("Value already present in the tree")

    def find_max(self, curr_node=None):
        if curr_node.right_child:
            return self._findmax(curr_node.right_child)
        else:
            return curr_node.value
        

    def _findmax(self, curr_node):
        if curr_node.right_child is None:
            return curr_node.value

        return self._findmax(curr_node.right_child)
        

    def delete(self, element):
        if self.root != None:
            self._deleter(element, self.root)


    def _deleter(self, element, curr_node):
        if element > curr_node.value:
            if curr_node.right_child:
                curr_node.right_child = self._deleter(element, curr_node.right_child)
        elif element < curr_node.value:
            if curr_node.left_child:
                curr_node.left_child = self._deleter(element, curr_node.left_child)
        else:
            if curr_node.left_child is None and curr_node.right_child is None:
                return None
            if curr_node.left_child is None:
                return curr_node.right_child
            if curr_node.right_child is None:
                return curr_node.left_child
            
            max_val = self.find_max(curr_node.left_child)
            curr_node.value = max_val
            curr_node.left_child = self._deleter(max_val, curr_node.left_child)




    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)
        else:
            print('Tree is empty')

    def _print_tree(self, curr_node):
        if curr_node!=None:
            self._print_tree(curr_node.left_child)
            print(curr_node.value)
            self._print_tree(curr_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, curr_node, curr_height):
        if curr_node == None: return curr_height

        left_height = self._height(curr_node.left_child, curr_height+1)
        right_height = self._height(curr_node.right_child, curr_height+1)
        return max(left_height, right_height)


    def search(self, item):
        if self.root==None:
            return False
        else:
            return self._searcher(self.root, item)    

    def _searcher(self, curr_node, item):
        if curr_node.value != None and  curr_node.value==item:
            print('Found')
        elif item<curr_node.value and curr_node.left_child != None:
            return self._searcher(curr_node.left_child, item)
        elif item>curr_node.value and curr_node.right_child != None:
            return self._searcher(curr_node.right_child, item)
        else:
            print("Not Found")

    def find(self, value):
        if self.root!=None:
            return self._finder(value, self.root)
        else:
            return None

    def _finder(self, item, curr_node):
        if item == curr_node.value:
            return curr_node
        elif item<curr_node.value and curr_node.left_child!=None:
            return self._finder(item, curr_node.left_child)
        elif item>curr_node.value and curr_node.right_child!=None: 
            return self._finder(item, curr_node.right_child)

def fill_tree(tree, num_elements=4, max_int=100):
    from random import randint
    for _ in range(num_elements):
        curr_elem = randint(0, max_int)
        tree.insert(curr_elem)
    return tree

tree = binary_search_tree()
#tree = fill_tree(tree)
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(2000)
tree.delete(6)
tree.print_tree()
