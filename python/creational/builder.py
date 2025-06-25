from abc import ABC, abstractmethod
from enum import Enum
from copy import copy
class SandwichTypes(Enum):
    BASIC=1
    VEGAN=2

class ISandwich(ABC): #builder

    @abstractmethod
    def get_bread(self, bread: str) -> "ISandwich":
        pass

    @abstractmethod
    def get_meat(self, meat: str) -> "ISandwich":
        pass
    @abstractmethod
    def get_sauce(self, sauce: str) -> "ISandwich":
        pass

    @abstractmethod
    def reset(self):
        pass
    @abstractmethod
    def build(self):
        pass
    

class SandwichBuilder(ISandwich): #
    _sandwich: "Sandwich" 

    def __init__(self) -> None:
        self.reset()

    def get_bread(self, bread: str)-> ISandwich:
        self._sandwich.bread = bread
        return self
    
    def get_meat(self, meat: str)-> ISandwich:
        self._sandwich.meat = meat
        return self

    def get_sauce(self, sauce: str)-> "ISandwich":
        self._sandwich.sauce = sauce
        return self
    
    def reset(self) -> "Sandwich":
        self._sandwich = Sandwich()
        return self._sandwich
    
    def build(self):
        new_sandwich = copy(self._sandwich )
        self.reset()
        return new_sandwich 


class Sandwich():
    bread: str
    meat: str
    sauce: str
    def __init__(self, bread: str = "", meat: str = "", sauce: str= ""):
        self.bread = bread
        self.meat = meat
        self.sauce = sauce
    def __str__(self) -> str:
            return f"""

Sandwich: 
bread: {self.bread}
meat: {self.meat}
sauce: {self.sauce}"""

class RestaurantDirector(): #director
    builder: ISandwich
    def __init__(self, builder: ISandwich) -> None:
        self.builder = builder
    
    def make(self, type: SandwichTypes):

        if type == SandwichTypes.BASIC:
            self.builder.get_bread("Pão").get_meat("Carne").get_sauce("Molho")
        
        if type == SandwichTypes.VEGAN:
            self.builder.get_bread("Pão Vegano")
            self.builder.get_meat("Carne Vegana")
            self.builder.get_sauce("Molho Vegano")
         

        return self.builder.build()
    
    def change_buider(self, builder: ISandwich):
        self.builder = builder

def main():
    builder = SandwichBuilder()
    restaurant_director = RestaurantDirector(builder)
    
    basic_sandwich = restaurant_director.make(SandwichTypes.BASIC)
    print(basic_sandwich)
    
    vegan_sandwich = restaurant_director.make(SandwichTypes.VEGAN)
    print(vegan_sandwich)

    mixed_sandwich = SandwichBuilder().get_bread("Pão Misto").get_meat("Carne mista").get_sauce("Molho misto").build()
    print(mixed_sandwich)
main()
