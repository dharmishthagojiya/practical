import E001_v2
import pandas as pd
from E001_v2 import Product,Category
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

class Location:
    code_l=1200
    def __init__(self,name):
        self.name=name
        self.code=Location.code_l+1
        Location.code_l+=1
    def display1(self):
        print("location name:", self.name, "code", self.code)


class Movement:

    def __init__(self,from_location,to_location,product,quantity):
        self.from_location=from_location
        self.to_location=to_location
        self.product=product
        self.quantity=quantity
        self.display=''
        try:
            if self.product.stock_at_location[self.from_location] >= self.quantity:  # 40 >=20
                qun = self.product.stock_at_location[self.from_location] - self.quantity  # 40-20=20
                self.product.stock_at_location.update({self.from_location: qun})  # {jamnager,20}
                if self.to_location in self.product.stock_at_location:  # {ahmedabad}it check location is available or not
                    qun1 = self.product.stock_at_location[self.to_location] + self.quantity  # 10+20
                    self.product.stock_at_location.update({self.to_location: qun1})  # {ahmedabad,30}
                    # print(self.product.name,"stock added")
                else:
                    # if not available location it add both location and quantity
                    self.product.stock_at_location.update({self.to_location: self.quantity})
                # print(self.product.name,"done movement")
                self.display = f'product quantity :{self.quantity} from {self.from_location.name} to {self.to_location.name}'

            else:
                print(f"quantity no: {self.quantity} of {self.product.name} not available {self.from_location.name}")
        except Exception:
            print("no location for that product\n")
            #print("no stock available")

    @staticmethod
    def movements_by_product(product):
        flag = 0
        for item in listofm:
            if item.product.name == product.name:
                flag = 1
                print(item.display)

        if flag == 0:
            print("No movements yet.....")

if __name__ == "__main__":
    rajkot = Location("RAJKOT")
    jamnagar = Location("jamnagar")
    ahmedabad = Location("ahmedabad")
    mumbai = Location("mumbai")
    listofl = [rajkot, jamnagar, ahmedabad, mumbai]
    for i in listofl:
        i.display1()

    device = Category("device")

    mobile = Product("mobile", device, 12000,{rajkot: 30, jamnagar: 40, mumbai: 10})
    laptop = Product("laptop", device, 230000,{rajkot: 10, jamnagar: 10, ahmedabad: 10})
    tablet = Product("tablet", device, 1000,{ jamnagar: 40, ahmedabad: 40, mumbai: 10})
    television = Product("television", device, 35000,{rajkot: 30, ahmedabad: 90, mumbai: 10})
    watch = Product("smart watch", device, 4000,{rajkot: 2, jamnagar: 100, ahmedabad: 10, mumbai: 100})

    listofprodcut = [mobile, laptop, tablet, television, watch]

    for i in listofprodcut:
        print(i.name)  # print name of product
        for key in i.stock_at_location:  # print dictionary of location name,quantity value
            print(f'{key.name} - {i.stock_at_location[key]}')
        print()
    #df = pd.DataFrame(t.__dict__ for t in listofprodcut)
    #df['category'] = df['category'].apply(lambda x: x.name)
    #df['stock_at_location'] = df['stock_at_location'].apply(lambda x: x.product)
    #print(df)

    movement1 = Movement(jamnagar, ahmedabad, watch, 50)
    movement2 = Movement(rajkot, ahmedabad, mobile, 20)
    movement3 = Movement(rajkot, jamnagar, television, 20)
    movement4 = Movement( jamnagar,ahmedabad, tablet, 10)
    movement5=Movement(jamnagar,rajkot,television,30)

    listofm = [movement1, movement2, movement3, movement4,movement5]

    for i in listofprodcut:
        print(i.name)  # product name
        Movement.movements_by_product(i)  # movement of product
        print()
    print("\n")
    print("==========")
    print("new stock at location")
    for i in listofprodcut:
        i.display()
        print('Location: ',end='')
        for key in i.stock_at_location:
            print(f'{key.name} - {i.stock_at_location[key]}', end='  ')
        print('\n')
    print("product list by location")
    for i in listofl:
        print(i.name)
        for p in listofprodcut:
            if i in p.stock_at_location:
                print(f'{p.name} - {p.stock_at_location[i]}')
        print()






