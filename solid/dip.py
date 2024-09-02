# Code Example:
# Let's consider a example where we have a EmailService class that sends emails using a specific email provider (e.g., Gmail).


class GmailClient:
    
    def send_email(self, recipient, subject, body):
        pass
    

class EmailSrvice:
    
    def __init__(self) -> None:
        self.gmail_client = GmailClient()
        
    
    def sen_email(self, recipient, subject, body):
        self.gmail_client.send_email(recipient, subject, body)


# In this example, the EmailService class directly depends on the GmailClient class, a low-level module that implements the details of sending emails using the Gmail API.

# This violates the DIP because the high-level EmailService module is tightly coupled to the low-level GmailClient module.


# To adhere to the DIP, we can introduce an abstraction (interface) for email clients:

class EmailClient:
    
    def send_email(self, recipient, subject, body):
        raise NotImplementedError
    

class GmailClient(EmailClient):
    
    def send_email(self, recipient, subject, body):
        pass
    

class OutLookClient(EmailClient):
    def send_email(self, recipient, subject, body):
        pass
    

class EmailService:
    
    def __init__(self, email_client) -> None:
        self.email_client = email_client
        
        
    def send_email(self, recipient, subject, body):
        self.email_client.send_email(recipient, subject, body)
        

#usage
email_client = GmailClient()
email_service = EmailService(email_client)
email_service.send_email("recipient@example.com", "Subject", "Email Body")

# Now, the EmailService class depends on the EmailClient abstraction, and 
# the low-level email client implementations (GmailClient and OutlookClient) depend on the abstraction.

# This follows the DIP, resulting in a more flexible and extensible design.



# Violating the Dependency Inversion Principle
# Let's consider an example where a UserService class directly depends on a UserRepository class for accessing user data. 
# This violates DIP because the UserService is tightly coupled to the UserRepository, making it difficult to replace or mock the repository in tests.

# Code That Violates DIP


class UserRepository:
    def get_user(self, user_id):
        # Logic to retrieve user from database
        return {"id": user_id, "name": "John Doe"}

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_name(self, user_id):
        user = self.user_repository.get_user(user_id)
        return user["name"]

# Usage
service = UserService()
print(service.get_user_name(1))  # Output: John Doe



# Refactoring to Adhere to the Dependency Inversion Principle
# To adhere to DIP, we can introduce an abstraction (an interface or abstract class) that both the UserService and 
# UserRepository depend on. This decouples the service from the specific implementation of the repository.

# Code That Adheres to DIP



from abc import ABC, abstractmethod

# Abstract repository interface
class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_user(self, user_id):
        pass

# Concrete implementation of the repository
class UserRepository(UserRepositoryInterface):
    def get_user(self, user_id):
        # Logic to retrieve user from database
        return {"id": user_id, "name": "John Doe"}

# Service class that depends on the abstraction
class UserService:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def get_user_name(self, user_id):
        user = self.user_repository.get_user(user_id)
        return user["name"]

# Usage
repository = UserRepository()
service = UserService(repository)
print(service.get_user_name(1))  # Output: John Doe

