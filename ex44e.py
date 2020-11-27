class Other(object):

    def override(self):
        print("parent override")

    def implicit(self):
        print("parent implicit")

    def altered(self):
        print("parent altered")

class Child(object):

    def __init__(self):
        self.Other = Other()

    def implicit(self):
        self.Other.implicit()
    
    def override(self):
        print("child override")
    
    def altered(self):
        print("child , before other altered")
        self.Other.altered()
        print("child ,after other altered")

son = Child()

son.implicit()
son.override()
son.altered()
