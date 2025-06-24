from abc import ABC, abstractmethod
from copy import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self)-> "Prototype":
        pass

    @abstractmethod
    def show(self):
        pass
class BtnDefault(Prototype):
    name: str
    icon: str

    def __init__(self, text: str, icon: str) -> None:
        self.name = text
        self.icon = icon
    
    def clone(self) -> Prototype:
        return copy(self)
    
    def show(self):
        print(f"name: {self.name} - icon: {self.icon}")


def main():
    btn_1 = BtnDefault("Botão 1", "😊")
    btn_1.show()
    btn_2 = btn_1.clone()
    btn_2.show()

main()