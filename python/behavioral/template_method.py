from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    def process(self):
        self.validate()
        self.pay()
        self.generate_receipt()
        self.notify()

    def validate(self):
        print("Validando o pagamento")
    
    @abstractmethod
    def pay(self):
        pass

    def generate_receipt(self):
        print("Recibo gerado")
    
    def notify(self):
        print("Notificando a todos")

class PixProcessor(PaymentProcessor):
    def pay(self):
        print("Pagamento via PIX")

class BoletoProcessor(PaymentProcessor):
    def pay(self):
        print("Pagamento via boleto")

def main():
    pix_processor = PixProcessor()
    pix_processor.process()

    boleto_processor = BoletoProcessor()
    boleto_processor.process()

main()