class A():
    def implicit(self):
        print "this is the super class"
class B(A):
    def implicit(self):
        print"This is the derived class"
obj=B()


obj.implicit()
obj.implicit()
