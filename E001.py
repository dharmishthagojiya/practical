class Category:
    code=0
    def __init__(self,name):
        self.name=name
        self.code=Category.code+1
        self.no_of_product=0
        Category.code+=1
    def d(self):
        print("category:",self.name,",Main Code:",self.code)
        print("total no of product:-->",self.no_of_product)
class Product:
    codeofp=0
    def __init__(self,name,Category,price):
        self.name=name
        self.code=Product.codeofp+1
        Product.codeofp+=1
        self.Category=Category.name
        self.price=int(price)
        self.no_of_product=self.code+1
        Category.no_of_product+=1
    def display(self):
        print("Product :",self.name,"code: ",self.code,"category: ",self.Category,"Price: ",self.price)

a1=Category("cars")
a2=Category("mobile")
a3=Category("stationary")
try:
    p1 = [Product("samsung", a2, '140000'),
          Product("tatagroup", a1, 1200),
          Product("yundai", a1, 150000),
          Product("xerox", a3, 120),
          Product("cellotap", a3, 20),
          Product("pen", a3, 23),
          Product("pencil", a3, 10),
          Product("xiomi", a2, 20000),
          Product("chair", a3, 1000),
          Product("redmi", a2, 18000)]
    for x in p1:
        x.display()
    a1.d()
    a2.d()
    a3.d()
    print("sorting based on ascending order")
    x = (sorted(p1, key=lambda x: x.price))
    for i in x:
        i.display()
    print("sorting based on desending order")
    x = (sorted(p1, key=lambda x: x.price, reverse=True))
    for i in x:
        i.display()
    n = int(input("search product based on code"))
    y = [x for x in p1 if x.code == n]
    for i in y:
        i.display()
except Exception  as e:
    print(e)


