from abc import ABC, abstractmethod
from random import shuffle
from enum import Enum
class Iterator(ABC):
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def has_more(self) -> bool:
        pass

class IterationMode(Enum):
    REVERSE= "reverse"
    RANDOM = "random"

class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self, mode: IterationMode )-> Iterator:
        pass


class ShelfReverseIterator(Iterator):
    shelf: "Shelf"
    current_index: int

    def __init__(self, shelf: "Shelf") -> None:
        self.shelf = shelf
        self.current_index = len(shelf.products)

    def get_next(self):
        
        new_index = self.current_index - 1
        if new_index >= 0:
            self.current_index = new_index
            return self.shelf.products[new_index]
        
    def has_more(self) -> bool:
        return self.current_index > 0

class ShelfRandomIterator(Iterator):
    shelf: "Shelf"
    random_order: list[int]
    current_index: int

    def __init__(self, shelf: "Shelf") -> None:
        self.shelf = shelf
        self.random_order = list(range(0, len(shelf.products)))
        shuffle(self.random_order)
        self.current_index = -1
        

    def get_next(self):
        self.current_index += 1
        if self.current_index < len(self.random_order):
            current_shelf_position = self.random_order[self.current_index] 
            return self.shelf.products[current_shelf_position]

    def has_more(self) -> bool:
        return self.current_index < len(self.random_order) - 1

class Shelf(IterableCollection):
    products: list[str]
    def __init__(self, products: list) -> None:
        self.products = products
    def create_iterator(self, mode: IterationMode) -> Iterator:
        if mode == IterationMode.RANDOM:
            return ShelfRandomIterator(self)
        if mode == IterationMode.REVERSE:
            return ShelfReverseIterator(self)


def main():
    products = ["Produto 1", "produto 2", "produto 3"]

    shelf = Shelf(products)
    shelf_reverse_iterator = shelf.create_iterator(IterationMode.REVERSE)
    shelf_random_iterator = shelf.create_iterator(IterationMode.RANDOM)
    print("""
Reversee iterator""")
    while shelf_reverse_iterator.has_more():
        print(shelf_reverse_iterator.get_next())
    
    print("""
Random iterator""")
    while shelf_random_iterator.has_more():
        print(shelf_random_iterator.get_next())

main()