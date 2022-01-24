class A:
    clsvar1="im a A styudent"
    def __init__(self):
        self.var1="i'm in class a construct"
        self.clsvar1="class a"
        self.special="special"
class B(A):
    clsvar1="IM a B student"
    def __init__(self):

        self.var1="i'm in class b constructor"
        self.clsvar1="class b"
        super().__init__()
        print(super().clsvar1)

a=A()
b=B()
print(b.special,b.var1,b.clsvar1)