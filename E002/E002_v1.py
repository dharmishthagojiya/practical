import re
import pandas as pd
from datetime import datetime, date
import E001_v2
from E001_v2 import Product,Category
class Customer:
    def __init__(self, name, email, phone, street, city, state, country, type,company):
        self.name = self.name1(name)
        self.email = self.emailvalid(email)
        self.phone = self.phonevalid(phone)
        self.street = street
        self.city = self.name1(city)
        self.state = self.name1(state)
        self.country = self.name1(country)
        self.company = company
        if type == 'contact' or type == 'billing' or type == 'shipping' or type == 'company':
            self.type = type
        else:
            print("type check")
    def emailvalid(self,eml):
        emal = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if re.search(emal, eml):
            return  eml
        else:
            print("not valid email")
    def phonevalid(self,num1):
        num = '(0|91)?[7-9][0-9]{9}$'
        if re.search(num, num1):
            return num1
        else:
            print("not valid mobile number")

    def name1(self, name_check):

        re1 = '^[A-Za-z]*$'
        if re.search(re1, name_check):
            return name_check
        else:
            print("not valid")
            return False
    def display(self):
        print("name: ", self.name)
        print("Email :" , self.email)
        print("Phone: ", self.phone)
        print("address :",self.street,self.city,self.state,self.country)

class order:
    number=1600
    def __init__(self, date , company, billing, shipping):
        self.number=order.number+1
        order.number+=1
        self.date = self.check(date)
        self.company = company
        if billing.type == 'billing' and shipping.type == 'shipping':
            self.billing = billing
            self.shipping = shipping
        else:
            print("type check")
        self.order_lines=[]
        self.total_amount=0
    def total(self):
        for i in self.order_lines:
            self.total_amount=self.total_amount+i.subtotal
        print(self.total_amount)

    def display(self):
       print("number:", self.number)
       print("DATE:",self.date,"Company:",self.company.name)
       print("billing-------------------->")
       self.billing.display()
       print("shipping-------------------->")
       self.shipping.display()
       print("order_lines:")
       for i in self.order_lines:
           print(i.order.number)
       temp = pd.DataFrame(i.__dict__ for i in self.order_lines)
       temp['order'] = temp['order'].apply(lambda x: x.number)
       temp['product'] = temp['product'].apply(lambda x: x.name)
       print(temp)
       print("total amount:")
       self.total()
       print()
    def check(self, date1):
        try:
            date_obj = datetime.strptime(date1, '%Y-%m-%d')
            if date_obj.date() < date.today():
                print("The date cannot be in the past!")
            else:
                return date_obj
        except Exception as e:
            print(e)


class Orderline:

    def __init__(self, order, Product,quantity):
        self.order = order
        self.product = Product
        self.price = float(Product.price)
        self.quantity = int(quantity)
        self.subtotal = (self.price*self.quantity)
        self.order.order_lines.append(self)
    def display(self):
        print("Product: ", self.product.name)
        print("Quantity: ", self.quantity)
        print("Price: ", self.price)
        print("Total: ", self.subtotal)

if __name__ == "__main__":
    #customer
    Into = Customer("Into", '1into2@gmail.com', '919429118530', 'Ayodhyachock', 'Rajkot', 'Gujarat', 'India', 'company',
                    "")
    Dhara = Customer("Dhara", '.12@gmail.com', '919426519362', 'Madhavpan', 'Rajkot', 'Gujarat', 'India', 'billing',
                     Into)
    yudiz = Customer("yudiz", '.12@gmail.com', '919426519362', 'Madhavpan', 'Rajkot', 'Gujarat', 'India', 'shipping',
                     Into)
    Dharti = Customer("Dharti", '.12@gmail.com', '919426519362', 'Madhavpan', 'Rajkot', 'Gujarat', 'India', 'contact',
                      '')

    cars = Category("cars")
    mobile = Category("mobile")
    stationary = Category("stationary")

    iphone = Product("iphone", mobile, '140000')
    tatgroup = Product("tatagroup", cars, 1200)
    yundai = Product("yundai", cars, 150000)
    book = Product("book", stationary, 120)

    order1 = order('2022-02-25', Into, Dhara, yudiz)
    orderline1 = Orderline(order1, iphone, 10)

    order2 = order('2022-05-02', Into, Dhara, yudiz)
    orderline4 = Orderline(order2, book, 10)
    orderline2 = Orderline(order2, book, 2)

    order3 = order('2025-09-09', Into, Dhara, yudiz)
    orderline3 = Orderline(order3, yundai, 2)

    orderlist=[order1,order2,order3]
    for i in orderlist:
        i.display()
