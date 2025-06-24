from abc import ABC, abstractmethod

class IMediator(ABC):
    @abstractmethod
    def notify(self, sender: "BaseForm", event: str) -> None:
        pass


class BaseForm:
    mediator: IMediator
    def set_mediator(self, mediator: IMediator) -> None:
        self.mediator = mediator

class InputCPF(BaseForm):
    def get_input_value(self) -> str:    
        return "999-777-777-14"
    

    
class BtnValidateCPF(BaseForm):
    def on_click(self):
        self.mediator.notify(self, "validate_cpf")

class FormMediator(IMediator):
    def __init__(self, btn_validate_cpf: BtnValidateCPF, input_cpf: InputCPF) -> None:
        self.btn_validate_cpf = btn_validate_cpf
        self.input_cpf = input_cpf

    def notify(self, sender: BaseForm, event: str) -> None:
        if event == "validate_cpf":
            self.validate_cpf()

    def validate_cpf(self):
        if self.input_cpf.get_input_value() == "999-777-777-14":
            print("Valido")
        else:
            print("inválido")
       

def main():
    input_cpf = InputCPF()
    btn_validate = BtnValidateCPF()
    form_mediator = FormMediator(btn_validate, input_cpf)

    btn_validate.set_mediator(form_mediator)
    input_cpf.set_mediator(form_mediator)

    btn_validate.on_click()
main()