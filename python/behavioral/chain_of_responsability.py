from abc import ABC, abstractmethod
class Handler(ABC): # Interface Handler
    handler: "Handler | None"

    @abstractmethod
    def set_next_handler(self, handler: "Handler") -> None:
        pass

    @abstractmethod
    def handle(self, request: dict):
        pass

    @abstractmethod
    def next_handler(self, request: dict):
        pass

class BaseHandler(Handler): #Base handler
    handler: "Handler | None"
    def __init__(self) -> None:
        self.handler = None

    def set_next_handler(self, handler: "Handler") -> None:
        self.handler = handler

    def next_handler(self, request: dict):
        if self.handler is None:
            print("Ultimo handler executado")
            return
        self.handler.handle(request)

class EmailValidator(BaseHandler): #Concrete handler
    def handle(self, request: dict):
        print(f"checando o email: {request['email']}")
        if request["email"] != "":
            print("email confirmado")
            self.next_handler(request)
        else:
            print("Erro na valiadação do email")

class PasswordValidator(BaseHandler): #Concrete handler
    def handle(self, request: dict):
        print(f"checando a senha:")
        if request["password"] is not None and len(request["password"]) >= 8:
            print("senha confirmada")
            self.next_handler(request)
        else:
            print("Erro na valiadação da senha")
class UserValidator(BaseHandler): #Concrete handler
    def handle(self, request: dict):
        print(f"checando o usuario:")
        if request["user"] != "":
            print("usuario confirmado")
            self.next_handler(request)
        else:
            print("Erro na valiadação do usuario")

class main(): #Esse seria o meu client
    email_validator = EmailValidator()
    password_validator = PasswordValidator()
    user_validator = UserValidator()

    password_validator.set_next_handler(user_validator)
    email_validator.set_next_handler(password_validator)
    # email -> password -> user

    request = {
        "email": "email@email",
        "password": "SenhaSecreta",
        "user": "John Doe"
    }

    email_validator.handle(request)

main()
