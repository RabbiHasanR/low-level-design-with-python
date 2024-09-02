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



# Example that Violates SRP
# Let's consider a real-world example of a Book class that violates the Single Responsibility Principle. 
# This class is responsible for multiple concerns: managing book data, formatting the book content, and handling file operations.


class Book:
    
    def __init__(self, title, author, content) -> None:
        self.title = title
        self.author = author
        self.content = content
        
        
    def get_content(self):
        return self.content
    
    def format_as_html(self):
        return f"<html><head><title>{self.title}</title></head><body>{self.content}</body></html>"
    
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.format_as_html)
            

# Problems with the Above Example
# Multiple Responsibilities:
# Managing Book Data: The class is responsible for storing and managing the book's data (title, author, content).
# Formatting Content: The class handles formatting the book's content as HTML.
# File Operations: The class is responsible for saving the book's content to a file.
# If the requirements change (e.g., changing the format to Markdown instead of HTML or saving to a database instead of a file), 
# multiple parts of the class need to be modified, violating SRP.

# Refactoring to Adhere to SRP
# To adhere to the Single Responsibility Principle, we can refactor the Book class by separating these responsibilities into different classes.

class Book:
    def __init__(self, title, author, content) -> None:
        self.title = title
        self.author = author
        self.content = content
        
    
    def get_content(self):
        return self.content
    

class HtmlFormater:
    
    def format(self, book):
        return f"<html><head><title>{book.title}</title></head><body>{book.content}</body></html>"


class FileManager:
    
    def save_to_file(self, content, filename):
        with open(filename, 'w') as file:
            file.write(content)
            


# usage

book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Content of the book")

formater = HtmlFormater()
formatted_content = formater.format(book)

file_manager = FileManager()
file_manager.save_to_file(formatted_content, 'gatsby.html')