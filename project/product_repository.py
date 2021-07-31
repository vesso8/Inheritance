from project.food import Food
from project.drink import Drink

class ProductRepository:
    def __init__(self):
        self.products = []
    def add(self, product):
        self.products.append(product)
    def find(self, product_name):
        filtered_products = [p for p in self.products if p.name == product_name]
        if filtered_products:
            return filtered_products[0]
    def remove(self, product_name):
        filtered_products = [p for p in self.products if p.name == product_name]
        if filtered_products:
            current_product = filtered_products[0]
            self.products.remove(current_product)
    def __repr__(self):
        return '\n'.join([f"{products.name}: {products.quantity}" for products in self.products])
