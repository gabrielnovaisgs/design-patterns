from abc import ABC, abstractmethod
from copy import copy
class IMemento(ABC): 
    @abstractmethod
    def get_state(self) -> dict[str,str]:
        pass

class IOriginator(ABC):
    @abstractmethod
    def save(self) -> IMemento:
        pass

    @abstractmethod
    def restore(self, memento: IMemento) -> None:
        pass

class Memento(IMemento): #Concrete Memento, apenas um snapshot
    
    def __init__(self, state: dict[str,str]) -> None:
        self.state = state

    def get_state(self) -> dict[str,str]:
        return self.state

class TextEditor(IOriginator): #originator
    _state: dict[str, str]


    def __init__(self) -> None:
        self._state = dict()
    
    def add_text(self, text:str):
        self._state["text"] =  text

    def save(self)-> IMemento:
        return Memento(copy(self._state))

    def restore(self, memento: IMemento):
        self._state = memento.get_state()
        

    def show_text(self):
        print(f"text: {self._state.get("text")}")



class TextHistory(): #CareTaker
    _history: list[IMemento]
    _originator: TextEditor

    def __init__(self, originator: TextEditor) -> None:
        self._originator = originator
        self._history = []

    def undo(self):
        memento = self._history.pop()
        self._originator.restore(memento)

    def backup(self):
        memento = self._originator.save()
        self._history.append(memento)
        print("Estado salvo")

def main():
    editor = TextEditor()
    history = TextHistory(editor)

    editor.add_text("Texto 1")
    editor.show_text()
    history.backup()

    editor.add_text("Texto 2")
    editor.show_text()
    history.backup()

    editor.add_text("Texto 3")
    editor.show_text()

    print("Undo 1:")
    history.undo()
    editor.show_text()

    print("Undo 2:")
    history.undo()
    editor.show_text()

main()

    