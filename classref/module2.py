
class parent:
    def __init__(self):
        self.name='dhara'
        self._age=20
        self.__college="atmiya"
    def display(self):
        print("name",self.name)
        print("age",self._age)
        print("college",self.__college)
class child(parent):
    def __init__(self):
        self.child1="child1"
    def display1(self):
        print("child class",self.child1)
        print("parent object",self.name)
        print("parent 1 object",self._age)

if __name__ == "__main__":
    obj = parent()
    #print(obj.name)
    #print(obj._age)
    #print(obj.__college)
    print(obj._parent__college)
    # print(obj.__college)
    #obj.display()


