from abc import ABC, abstractmethod

class OrderState(ABC):

    @abstractmethod
    def pay(self, order: "Order")-> None:
        pass

    @abstractmethod
    def deliver(self, order: "Order") -> None:
        pass
    
    @abstractmethod
    def complete(self, order: "Order") -> None:
        pass

class NewOrderState(OrderState):
    def pay(self, order: "Order") -> None:
        print("Pagamento recebido!")
        order.set_state(PayedOrderState())
    
    def deliver(self, order: "Order") -> None:
        raise Exception("O pedido ainda não foi pago")
    
    def complete(self, order: "Order") -> None:
        raise Exception("O pedido ainda não foi pago")

class PayedOrderState(OrderState):
    def pay(self, order: "Order") -> None:
        raise Exception("O pedido já foi pago")
    
    def deliver(self, order: "Order") -> None:
        print("Pedido saiu para entrega")
        order.set_state(DeliveredOrderState())
    
    def complete(self, order: "Order") -> None:
        raise Exception("O pedido ainda não foi entregue")

class DeliveredOrderState(OrderState):
    def pay(self, order: "Order") -> None:
        raise Exception("O pedido já foi pago")
    
    def deliver(self, order: "Order") -> None:
        raise Exception("Pedido já saiu para entrega")
    
    def complete(self, order: "Order") -> None:
        print("Pedido entregue!")
        order.set_state(CompletedOrderState())

class CompletedOrderState(OrderState):
    def pay(self, order: "Order") -> None:
        raise Exception("O pedido já foi pago")
    
    def deliver(self, order: "Order") -> None:
        raise Exception("Pedido já saiu para entrega")
    
    def complete(self, order: "Order") -> None:
        raise Exception("Pedido já finalizou")

class Order:
    state: OrderState
    
    def __init__(self) -> None:
        self.state = NewOrderState()

    def set_state(self, state: OrderState):
        self.state = state

    
    def pay(self):
        self.state.pay(self)

    def deliver(self):
        self.state.deliver(self)

    def complete(self):
        self.state.complete(self)


def main():
    order = Order()
    order.pay()
    order.deliver()
    order.complete()

main()
