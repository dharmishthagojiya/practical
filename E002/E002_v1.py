import re
from datetime import datetime, date
'''Create a new class named "Customer" with below members. 
"name","email","phone","street","city","state","country","company","type".
"type" must be from "company,contact,billing,shipping".
"company" must be a Customer object which is the parent object.
Apply Multiple possible validation for phone number and email
Does not allowed number in name,city,state and country
'''
class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company, type):
        self.name = self.name1(name)
        self.email = email
        emal = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.search(emal, self.email):
            print("valid email id", self.email)
        else:
            print("not valid email")
        self.phone = phone
        num = '(0|91)?[7-9][0-9]{9}'
        if re.search(num, self.phone):
            print("valid phone number", self.phone)
        else:
            print("not valid")
        self.street = street
        self.city = self.name1(city)
        self.state = self.name1(state)
        self.country = self.name1(country)
        self.company = company
        self.type = type

    def name1(self, name_check):

        re1 = '^[A-Za-z]*$'
        if re.search(re1, name_check):
            print("valid")
            return True
        else:
            print("not valid")
            return False
'''
Create a new class named "Order" with members "number","date",
 "company", "billing", "shipping", "total_amount","order_lines".
"company", "billing", "shipping" are objects of Customer.
"date" must be today or the future. Does not allow past date.
"total_amount" auto calculated based on different products inside order.
"order_lines" is list of objects of "OrderLine"
'''
class order:
    def __init__(self, number, date , company, billing, shipping):
        self.number = number
        self.date = self.check(date)
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.total_amount = 0
        self.order_lines = 0

    def check(self, date1):
        try:
            date_obj = datetime.strptime(date1, '%Y-%m-%d')
            if date_obj.date() < date.today():
                print("The date cannot be in the past!")
            else:
                return date_obj
        except Exception as e:
            print(e)
'''create a new class named "OrderLine" with members 
"order", "product", "quantity", "price", "subtotal".
"order" is the object of Order.
"subtotal" is auto calculated based on quantity and price.
'''
class Orderline:
    def __init__(self, order, product, price):
        self.order = order
        self.product = product
        self.price = price
        self.quantity = 0
        self.subtotal = 0




a = Customer("Dhara", 'abc@gmail.com', '919426519362', 'Madhavpan', 'Rajkot', 'Gujrat', 'India', '1into2', 'a')
objorder = order(10, '2015-02-01', 'company', 'billing', 'shiping')
objorderline = Orderline(objorder,10,10000)
