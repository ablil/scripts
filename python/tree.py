#!/usr/bin/env python3

class Tree:
    '''
    Define some algorithms related to Tree data structure
    '''

    def __init__(self, data = None):
        self.data = data
        self.right_child = None
        self.left_child = None

    def __repr__(self):
        res = 'Data: {}'.format(self.data)

        if self.right_child :
            res += '\nRight child: {}'.format(self.right_child.data)
        else:
            res += '\nRight child: None'

        if self.left_child :
            res += '\nLeft child: {}'.format(self.left_child.data)
        else:
            res += '\nLeft child: None'

        return res

    def insert(self, obj):
        # The element to be insert should be of type Tree

        if self.data == None:
            return

        if self.data < obj.data :
            if self.right_child == None:
                self.right_child = obj
            else:
                self.right_child.insert(obj)
        else:
            if self.left_child == None:
                self.left_child = obj
            else:
                self.left_child.insert(obj)

    def inorder(self):
        if self is None:
            return
        else:
            if self.left_child is not None:
                self.left_child.inorder()

            print("Data: {}".format(self.data))

            if self.right_child is not None:
                self.right_child.inorder()

    def preorder(self):
        if self is None:
            return
        else:
            print("Data: {}".format(self.data))

            if self.left_child is not None:
                self.left_child.preorder()

            if self.right_child is not None:
                self.right_child.preorder()

    def postorder(self):
        if self is None:
            return
        else:
            if self.left_child is not None:
                self.left_child.postorder()

            if self.right_child is not None:
                self.right_child.postorder()

            print("Data: {}".format(self.data))
