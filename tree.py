class TreeNode:
    def __init__(self, data):
        self.data =  data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        paren = self.parent
        while paren:
            level +=1
            paren = paren.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefeix = spaces + '|__' if self. parent else ""
        print(prefeix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("MAC"))
    laptop.add_child(TreeNode("Surface Book"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Vivo"))
    cellphone.add_child(TreeNode("Nokia"))
    
    Tv = TreeNode("Television")
    Tv.add_child(TreeNode("Panasonic"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(Tv)
    return root



r = build_product_tree()
r.print_tree()
    
    
