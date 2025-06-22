from abc import ABC, abstractmethod

class Command(ABC): #interface
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class Light: #receiver, o executor real do comando
    def turn_on(self):
        print("Luz ligada")

    def turn_off(self):
        print("luz desligada")
 

class TurnLightOff(Command): #ConcreteCommand, o comando a ser executado
    light: Light
    def __init__(self, light: Light) -> None:
        self.light = light
    
    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()    

class TurnLightOn(Command): #ConcreteCommand, o comando a ser executado
    light: Light
    def __init__(self, light: Light) -> None:
        self.light = light
    
    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()    
 

class RemoteController: # invoker, o gatilho que dispara  comando
    buttons: dict[str, Command]
    history: list[Command]

    def __init__(self) -> None:
        self.buttons = dict()
        self.history = list()
    def set_command(self, button: str, command: Command):
        self.buttons[button] = command

    def press(self,button: str):
        command = self.buttons.get(button)
        if command: 
            command.execute()
            self.history.append(command)
        else:
            print("Esse botão ainda não foi configurado")
            
    
    def undo(self):
        try:
            last_command = self.history.pop()
            last_command.undo()
        except:
            print("Não temos mais histórico para desfazer")
            
        


def main():
    remote_controller = RemoteController()
    light = Light()
    command_turn_light_on = TurnLightOn(light)
    command_turn_light_off = TurnLightOff(light)

    remote_controller.set_command("1", command_turn_light_on)
    remote_controller.set_command("2", command_turn_light_off)

    remote_controller.press('1')
    remote_controller.press('2')

    # trocando o comando de off para ligar a luz em tempo de execução
    remote_controller.set_command("2", command_turn_light_on)
    remote_controller.press('2')

    print("desfazendo as alterações")
    # desfazendo a ação feita
    remote_controller.undo()
    remote_controller.undo()
    remote_controller.undo()
    remote_controller.undo()

main()