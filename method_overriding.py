class A:

    def show(self):
        print('in A show')

class B(A):

    def show(self):
        print('in B show')

al = B()
al.show()