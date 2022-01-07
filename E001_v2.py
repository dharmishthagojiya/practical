from treelib import Node, Tree
import pandas as pd
class Category:
    code = 0

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.code = Category.code+1
        self.no_of_product = 0
        Category.code += 1
        self.product = []
        self.display_name = self.name
        self.display_name1()

    def d(self):
        print("category  :", self.name, ",Code :", self.code)
        print(self.display_name)
        print("no of product:-->", self.no_of_product)
        if self.no_of_product != 0:
            print("Name of all products:")
            for i in self.product:
                print(i.name)
        print()

    def display_name1(self):
        count = self
        while (count.parent != None):
               self.display_name = f'{count.parent.name} > {self.display_name}'
               count=count.parent


class Product:

    codeofp = 0

    def __init__(self, name, category, price,):
        self.name = name
        self.code = Product.codeofp+1
        Product.codeofp += 1
        self.category = category.name
        self.price = int(price)
        self.no_of_product = self.code+1
        category.no_of_product += 1
        category.product.append(self)
        self.stock_at_location={}
    def display(self):
        print("Product :", self.name, "code: ", self.code, "category: ", self.category, "Price: ", self.price)

def main():

    # parent objects
    vehicale = Category("vehicale")
    device = Category("device")
    things = Category("things")
    cloths  = Category("cloths")
    # child objects
    a1 = Category("cars", vehicale)
    a2 = Category("mobile", device)
    a3 = Category("stationary", things)
    # child of child
    c1 = Category("petrol", a1)
    c2 = Category("samsung", a2)
    c3 = Category("book", a3)
  #  c4 = Category("b",c3)
    listofc = [vehicale, device, things,cloths, a1, a2, a3, c1, c2, c3]

    p1 = [Product("iphone", a2, '140000'),
          Product("tatagroup", a1, 1200),
          Product("yundai", a1, 150000),
          Product("xerox", a3, 120),
          Product("cellotap", a3, 20),
          Product("pen", a3, 23),
          Product("maruti", a1, 10),
          Product("xiomi", a2, 20000),
          Product("chair", a3, 1000),
          Product("redmi", a2, 18000),
          Product("saree",cloths, 2000),
          Product("shirt",cloths, 200),
          Product("cap",cloths, 100),
          Product("bike",vehicale, 25000),
          Product("Laptop",device, 55000),
          Product("home furniture",things, 120000)
          ]
    print("list of category")
    for x in listofc:
        x.d()
    for x in p1:
        x.display()

    tree=Tree()
    #static tree creation
    '''
    tree.create_node("category", "category")
    tree.create_node("v1ehicle","vehicle", parent="category")
    tree.create_node("device", "device", parent="category")
    tree.create_node("things", "things", parent="category")
    tree.create_node("cloths", "cloths", parent="category")
    tree.create_node("mobile", "mobile", parent="device")
    tree.create_node("cars", "cars", parent="vehicle")
    tree.create_node("stationary", "stationary", parent="things")
    tree.create_node("petrol", "petrol", parent="cars")
    tree.create_node("samsung", "samsung", parent="mobile")
    tree.create_node("book", "book", parent="stationary")
    tree.create_node("shirt", "shirt",parent="cloths")
    tree.create_node("saree", "saree", parent="cloths")
    tree.create_node("tatagroup", "tatagroup", parent="cars")

    tree.show()
    '''
    #manual tree creation
    tree.create_node("Product Category", 0)

    for i in listofc:
        tree.create_node(i.name, i.name, parent=0)
        if i.parent is not None:
            tree.move_node(i.name, i.parent.name)
        for c in i.product:
            tree.create_node(c.name, c.name, parent=i.name)

    tree.show()
    print("sorting based on ascending order")
    x = (sorted(p1, key=lambda r: r.price))
    for i in x:
        i.display()
    print("sorting based on desending order")
    x = (sorted(p1, key=lambda r: r.price, reverse=True))
    for i in x:
        i.display()
    n = int(input("search product based on code"))
    y = [x for x in p1 if x.code == n]
    for i in y:
        i.display()
if __name__ == "__main__":
    main()

