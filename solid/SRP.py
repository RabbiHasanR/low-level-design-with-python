# Code Example:
# Imagine you have a class called UserManager that handles user authentication, user profile management, and email notifications.

class UserManager:
    def authenticate_user(self, username, password):
        # authentication logic
        pass
    

    def update_user_prodile(self, username, password):
        # profile update logic
        pass
    
    def send_email_notification(self, username, password):
        # email sending logic
        pass
    

# This class violates the SRP because it has multiple responsibilities: authentication, profile management, and email notifications.

# If you need to change the way user authentication is handled, you might inadvertently affect the email notification logic, or vice versa.

# To adhere to the SRP, we can split this class into three separate classes, each with a single responsibility:

class UserAuthenticator:
    def authenticate_user(self, username, password):
        # authentication logic
        pass

class UserProfileManager:
    def update_user_prodile(self, username, password):
        # profile update logic
        pass
    
class EmailNotifier:
    def send_email_notification(self, username, password):
        # email sending logic
        pass
    

# Now, each class has a single, well-defined responsibility. 
# Changes to user authentication won't affect the email notification logic, and vice versa, improving maintainability and reducing the risk of unintended side effects.
    