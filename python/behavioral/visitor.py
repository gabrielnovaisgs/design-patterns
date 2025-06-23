from abc import ABC, abstractmethod

class Visitable(ABC):
    @abstractmethod
    def accept(self, visitor: "IVisitor"):
        pass

class PhysicalProduct(Visitable): # concrete visitable
    name:str
    weight: float

    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight

    def accept(self, visitor: "IVisitor"):
        visitor.visit_physical(self)

class DigitalProduct(Visitable): # Concrete visitable
    name: str
    size_in_mb: int


    def __init__(self, name: str, size_in_mb: int) -> None:
        self.name = name
        self.size_in_mb = size_in_mb
    
    def accept(self, visitor: "IVisitor"):
        visitor.visit_digital(self)
    


class IVisitor(ABC):
    @abstractmethod
    @abstractmethod
    def visit_physical(self, product: PhysicalProduct): pass

    @abstractmethod
    def visit_digital(self, product: DigitalProduct): pass


class NFePrinter(IVisitor):# Concrete visitor
    def visit_digital(self, product: DigitalProduct):
        print(f"Imprimindo nota fiscal para o {product.name}")
    
    def visit_physical(self, product: PhysicalProduct):
        print(f"Imprimindo nota fiscal para o {product.name}")


class DeliverCalculator(IVisitor):
    def visit_digital(self, product: DigitalProduct):
        print(f"Custo do frete é 0")       
    def visit_physical(self, product: PhysicalProduct):
        print(f"custo do frete é R${product.weight * 2}") 

def main():
    digial_product = DigitalProduct("Produto digital", 1024)
    physical_product = PhysicalProduct("Produto fisico", 55.5)
    nfe_printer = NFePrinter()
    
    physical_product.accept(nfe_printer)
    digial_product.accept(nfe_printer)
    
    deliver_calculator = DeliverCalculator()
    physical_product.accept(deliver_calculator)
    digial_product.accept(deliver_calculator)
    

main()
