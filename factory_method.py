from abc import ABC, abstractmethod
from enum import Enum

class NotificationType(Enum):
    EMAIL = 1
    SMS = 2
    PUSH = 3

class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

class EmailNotifiction(Notification):
    def send(self, message: str):
        print(f"Message: {message} was send by email") 

class SMSNotifiction(Notification):
    def send(self, message: str):
        print(f"Message: {message} was send by sms") 

class PushNotifiction(Notification):
    def send(self, message: str):
        print(f"Message: {message} was send by push")

class GeneralNotifiction(Notification):
    def send(self, message: str):
        print(f"Message: {message} was send by General")  

class NotificationFactory:
    @classmethod
    def create(cls, notificationType: int) -> Notification:
        if(notificationType == NotificationType.EMAIL.value):
            return EmailNotifiction()
        
        elif(notificationType == NotificationType.SMS.value):
            return SMSNotifiction()
        
        elif(notificationType == NotificationType.PUSH.value):
            return PushNotifiction()
    
        return GeneralNotifiction()

def main():
    print("Digite  sua mensgem: ")             
    message = input()

    print("""Como gostaria de envia-la?
        1 - email
        2 - sms
        3 - push""")

    sender = int(input())

    notification = NotificationFactory.create(sender)
    notification.send(message)

main()