class Parent(object):
    def altered(self):
        print("parent altered!")

class Child(Parent):

    def altered(self):
        print("child before parent altered")
        super(Child, self).altered()
        print("child after parent altered!")

dad = Parent()
child = Child()

dad.altered()
child.altered()