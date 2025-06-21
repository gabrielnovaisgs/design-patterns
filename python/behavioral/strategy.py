from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        pass

class MailShipping(ShippingStrategy):
    def calculate(self, price):
        return price + 10
    
class CarrierShipping(ShippingStrategy):
    def calculate(self, price: float) -> float:
        return price + 20
    
class FreeShipping(ShippingStrategy):
    def calculate(self, price: float) -> float:
        return price
    
class OrderItem:
    name: str
    price: float

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
class Order:
    __order_itens: list[OrderItem] 
    __shipping_strategy: ShippingStrategy

    def __init__(self):
        self.__order_itens = []
        self.set_shipping_strategy(MailShipping())
    
    def calculate_total_order(self):
        return self.__shipping_strategy.calculate(self.__calculate_order_price())
    
    def __calculate_order_price(self):
        price = 0
        for item in self.__order_itens:
            price += item.price
        return price

    def show_order(self):
        text = ""
        for item in self.__order_itens:
           text += f'Nome: {item.name} - R$ {item.price}\n'
        return text
    
    def set_shipping_strategy(self, strategy: ShippingStrategy):
        self.__shipping_strategy = strategy
    
    def add_items(self, itens: list[OrderItem]):
        self.__order_itens += itens 

def main():
    order = Order()
    item_1 = OrderItem("Item 1", 100)
    item_2 = OrderItem("Item 2", 300)
    order.add_items([item_1, item_2])

    if(order.calculate_total_order() >= 500):
        order.set_shipping_strategy(FreeShipping())
    else:
        print("""Como você gostaria que seu pedido fosse entregue?:
            1 - Correios
            2 - Empresa XPTO
            """)
        selected = int(input())
        if(selected == 1): order.set_shipping_strategy(MailShipping())
        if(selected == 2): order.set_shipping_strategy(CarrierShipping())

    print(f"""Items comprados:\n{order.show_order()}\nValor total com frete: R$ {order.calculate_total_order()}""")
    

main()



    
