import re
import pandas as pd
from datetime import datetime, date
from E001_v2 import Product, Category
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class Customer:

    def __init__(self, name, email, phone, street, city, state, country, type, company):
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

    def emailvalid(self, eml):
        emal = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if re.search(emal, eml):
            return eml
        else:
            msg = "invalid email"
            raise ValueError(msg)

    def phonevalid(self, num1):
        num = r"^[789]\d{9}$"
        if re.search(num, num1):
            return num1
        else:
            msg = "not valid phone number"
            raise ValueError(msg)

    def name1(self, name_check):

        re1 = '^[A-Za-z]*$'
        if re.search(re1, name_check):
            return name_check
        else:
            msg = "not valid name/city/state/country"
            raise ValueError(msg)

    def display(self):
        print("name    : ", self.name)
        print("Email   :", self.email)
        print("Phone   : ", self.phone)
        print("address :", self.street)
        print("city    :", self.city)
        print("States  :", self.state)
        print("country :", self.country)
        print("type    :", self.type)


class order:

    number = 1600
    pdtolist=''

    def __init__(self, date, company, billing, shipping):
        self.number = order.number+1
        order.number += 1
        self.date = self.check(date)
        self.company = company
        if billing.type == 'billing' and shipping.type == 'shipping' and company.type == 'company':
            self.billing = billing
            self.shipping = shipping
            self.company = company
        else:
            print("type check")
        self.order_lines = []
        self.total_amount = 0

    def total(self):
        total_amount = 0
        for i in self.order_lines:
            total_amount = total_amount + i.subtotal
        self.total_amount = total_amount


    def display(self):
        print("number:", self.number)
        print("DATE:", self.date, "Company:", self.company.name)
        print("billing-------------------->")
        self.billing.display()
        print("shipping-------------------->")
        self.shipping.display()
        print("order_lines:")
        temp = pd.DataFrame(i.__dict__ for i in self.order_lines)
        temp.index = temp.index + 1
        temp['order'] = temp['order'].apply(lambda x: x.number)
        temp['product'] = temp['product'].apply(lambda x: x.name)
        print(temp)
        print("total amount:", self.total_amount)
        print()
        self.pdtolist = list(temp['product'])

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

    def __init__(self, order, Product, quantity, price=None):
        self.order = order
        self.product = Product
        self.quantity = int(quantity)
        self.order.order_lines.append(self)
        if price is None:
            self.price = Product.price
        else:
            self.price = price
        self.subtotal = (self.price * self.quantity)
        self.order.total()

    def display(self):
        print("Product: ", self.product.name)
        print("Quantity: ", self.quantity)
        print("Price: ", self.price)
        print("Total: ", self.subtotal)


if __name__ == "__main__":

    Into = Customer("Into", 'into@gmail.com', '9429118530', 'Ayodhya_chock', 'Rajkot', 'Gujarat', 'India', 'company',
                    "")
    Dhara = Customer("Dhara", 'a@gmail.com', '9426519362', 'Madhav_pan', 'Mumbai', 'Gujarat', 'India', 'billing',
                     Into)
    yudiz = Customer("yudiz", 'yudiz@gmail.com', '9926519362', 'Madhav_pan', 'Ahmedabad', 'Gujarat', 'India', 'shipping',
                     Into)
    Dharti = Customer("Dharti", 'dharti@gmail.com', '9826519362', 'Madhav_pan', 'Rajkot', 'Gujarat', 'India', 'contact',
                      '')
    customer_list = [Into, Dhara, yudiz, Dharti]
    for i in customer_list:
        print("---------------------------------")
        i.display()
        print("----------------------------")

    cars = Category("cars")
    mobile = Category("mobile")
    stationary = Category("stationary")

    iphone = Product("iphone", mobile, '140000')
    tatagroup = Product("tatagroup", cars, 1200)
    yundai = Product("yundai", cars, 150000)
    book = Product("book", stationary, 120)
    samsung = Product("samsung", mobile, 25000)
    pen = Product("pen", stationary, 25)
    productlist = [iphone, tatagroup, yundai, book, samsung, pen]

    order1 = order('2022-01-25', Into, Dhara, yudiz)
    orderline1 = Orderline(order1, iphone, 10)
    orderline6 = Orderline(order1, samsung, 10, 100)

    order2 = order('2022-05-02', Into, Dhara, yudiz)
    orderline4 = Orderline(order2, book, 10, 20)
    orderline2 = Orderline(order2, pen, 2, 10)

    order3 = order('2025-09-09', Into, Dhara, yudiz)
    orderline3 = Orderline(order3, yundai, 2, 12000)
    orderline5 = Orderline(order3, tatagroup, 3, 123000)

    order_list = [order1, order2, order3]
    for i in order_list:
        i.display()
    print("----------------------")
    print("sorting based on date ")
    print("---------------")
    pd1 = pd.DataFrame(i.__dict__ for i in order_list)
    pd1['company'] = pd1['company'].apply(lambda x: x.name)
    pd1['billing'] = pd1['billing'].apply(lambda x: x.name)
    pd1['shipping'] = pd1['shipping'].apply(lambda x: x.name)
    pd1.sort_values(by='date', ascending=True, inplace=True)
    pd1.index = pd1.index + 1
    orders_list=[order1.pdtolist, order2.pdtolist, order3.pdtolist]
#   pd1['order_lines'] = pd1['order_lines'].apply(lambda x: x[0].product.name+" ,"+x[1].product.name)
    pd1['order_lines'] = orders_list
    pd12 = pd1.drop('pdtolist', axis=1)
    print(pd12)
    print("-----------------")
    print("current month data:")
    print("----------------")
    pd2 = pd12[pd12['date'].dt.month == date.today().month]
    print(pd2)

    print("---------")
    print("search")
    print("----------------")
    search = (input("enter you want search number"))
#   print(pd12.loc[pd12['number'] == n])
    temp=0
    for i in order_list:
        if str(i.number) == str(search):
            i.display()
            temp = 1
    if temp == 0:
        print("no search number's data is available")

    print("----------------------------")
    print("search product based on name")
    print("--------------------------------------------")
    search_product = input("enter product name:")
    count = 0
    for i in productlist:
        if i.name == search_product:
            for j in order_list:
                for r in j.order_lines:
                    if r.product == i:
                        print("order number", j.number)
                        r.display()
                        count = 1

    if count == 0:
        print("no order is present base on product name")


    def search(lst, target):
        temp = 0
        min = 0
        max = len(lst) - 1
        avg = (min + max) // 2
        while (min < max):
            if (lst[avg].number == target):
                lst[avg].display()
                temp = 1
                break
            elif (lst[avg].number < target):
                return avg + 1 + search(lst[avg + 1:], target)
            else:
                return search(lst[:avg], target)

        if temp == 0:
               print("not available order number ")

    sorted_list = list(sorted(order_list, key=lambda item: item.number))
    order_number = int(input("enter order number"))
    search(sorted_list, order_number)

