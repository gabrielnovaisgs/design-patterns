from abc import ABC, abstractmethod

class Product:
    name: str
    def __init__(self, name: str):
        self.name = name  


class StockObserver(ABC):
    @abstractmethod
    def notify(self, product: Product) -> None:
        pass

class ManagerObserver(StockObserver):
    def notify(self, product) -> None:
        print(f"Gerente, o produto {product.name} esta a baixo da quantidade")

class BuyerTeamObserver(StockObserver):
    def notify(self, product: Product) -> None:
        print(f"Time esta na hora de comprar o produto {product.name}")

class StockSystem():
    products_in_stock: dict[str, int]
    min_stock_quantity = 3
    observers: list[StockObserver]

    def __init__(self) -> None:
        self.observers = []
        self.products_in_stock = {}

    def add_product(self, product: Product, quantity: int):

        if(self.products_in_stock.get(product.name) == None):
            self.products_in_stock[product.name] = 0 
        self.products_in_stock[product.name] += quantity


    def remove_product(self, product: Product, quantity: int):
        if(self.products_in_stock.get(product.name) == None or self.products_in_stock[product.name] < quantity):
            print("Não temos como remover o produto")
            return
        
        self.products_in_stock[product.name] -= quantity

        if(self.products_in_stock[product.name]<= self.min_stock_quantity):
            self.notify_observers(product)

    def add_observers(self, observers: list[StockObserver]):
        self.observers += observers

    def notify_observers(self, product: Product):
        for observer in self.observers:
            observer.notify(product)

def main():
    stock_system = StockSystem()
    stock_system.add_observers([ManagerObserver(), BuyerTeamObserver()])
    
    product_1 = Product("Produto 1")

    stock_system.add_product(product_1, 5)
    stock_system.remove_product(product_1, 4)

main()

    