from datetime import datetime, date
class Team:
    def __init__(self, name, city, fee, number):
        self.name = name
        self.city = city
        self.fee = fee
        self.number = number
        self.fee_amount = 10000
        self.created = datetime.now()
        self.registered = date.today()

    def set_name(self, name):
        self.name = name
    def set_city(self,city):
        self.city = city
    def set_fee(self,fee):
        self.fee = fee
    def set_number(self,number):
        self.number = number
    def set_fee_amount(self, fee_amount):
        self.fee_amount = fee_amount

    def get_name(self):
        return self.name
    def get_city(self):
        return self.city
    def get_fee(self):
        return self.fee
    def get_number(self):
        return self.number
    def get_fee_amount(self):
        return self.fee_amount

