# # decorators


# def deco (abc):
#     def wrap():
#         print("###########welcome#########")
#         print("hello")
#         abc()
#         print("bye")
#     return wrap
# @deco
# def abc(): 
#     print("btech 4th sem")
#     abc()


class abc:
    a=5
    def change(self,n):
        self.a=n
al=abc()
print("before change=",al.a,abc.a)
al.change(10)
print("after change=",al.a)
