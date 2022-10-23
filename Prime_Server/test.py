#!/usr/bin/python3
class Item:
    def __init__(self,name:str,price:float,qty=0):
        assert price >= 0, f"Price {price} is not greater than zero"
        assert qty >= 0, f"Quantiy {qty} is not greater than zero"
        

        self.name = name
        self.price = price
        self.qty = qty
        

    def calc_tot_price(self):
        return self.price*self.qty

item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)
item3 = Item("Desktop",1500,7)


