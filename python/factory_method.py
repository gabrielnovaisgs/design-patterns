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

class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Message: {message} was send by email") 

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Message: {message} was send by sms") 

class PushNotification(Notification):
    def send(self, message: str):
        print(f"Message: {message} was send by push")

class GeneralNotification(Notification):
    def send(self, message: str):
        print(f"Message: {message} was send by General")  

class NotificationFactory:
    @classmethod
    def create(cls, notificationType: NotificationType) -> Notification:
        if(notificationType == NotificationType.EMAIL):
            return EmailNotification()
        
        elif(notificationType == NotificationType.SMS):
            return SMSNotification()
        
        elif(notificationType == NotificationType.PUSH):
            return PushNotification()
    
        return GeneralNotification()

def main():
    print("Digite  sua mensgem: ")             
    message = input()

    print("""Como gostaria de envia-la?
        1 - email
        2 - sms
        3 - push""")

    sender = NotificationType(int(input()))

    notification = NotificationFactory.create(sender)
    notification.send(message)

main()