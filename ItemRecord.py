"""
each item has a:
- category
- name
- amount sold
- average price
"""

class ItemRecord:
    def __init__ (self, name:str, category: str, price:float, amount_sold:int):
        self.name = name
        self.category = category
        self.price = price
        self.amount_sold = amount_sold

    def getName (self, new_name:str):
        self.name = new_name