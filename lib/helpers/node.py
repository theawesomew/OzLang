
class Node ():

    def __init__ (self, node):
        self.children = {}
        for child in node.children:
            self.children[child.data] = child

    def __getattr__(self, __name: str):
        return self.children[__name]