# Example: Interface for a Payment System
# Let's consider a real-life example of a payment system. 
# Different payment methods (e.g., credit card, PayPal, bank transfer) should adhere to a common interface, which might define a method called process_payment().

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(PaymentMethod):
    
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransferPayment(PaymentMethod):
    
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of ${amount}")


def make_payment(payment_method: PaymentMethod, amount):
    payment_method.process_payment(amount)

# Example usage
credit_payment = CreditCardPayment()
make_payment(credit_payment, 100)  # Output: Processing credit card payment of $100

paypal_payment = PayPalPayment()
make_payment(paypal_payment, 200)  # Output: Processing PayPal payment of $200

bank_payment = BankTransferPayment()
make_payment(bank_payment, 300)  # Output: Processing bank transfer payment of $300




# Built-In Example: collections.abc Module
# Python’s collections.abc module provides several abstract base classes that can be seen as interfaces. 
# These abstract base classes define methods that must be implemented by concrete classes that inherit from them.

# Example: collections.abc.Sequence
# The collections.abc.Sequence class is an abstract base class that defines the interface for sequence types (like lists, tuples, etc.). 
# Any class that inherits from Sequence must implement certain methods, such as __getitem__() and __len__().

# Here’s an example of how you might implement a custom sequence class using this interface:

from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self, *args):
        self._data = list(args)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __len__(self):
        return len(self._data)

# Example usage
my_list = MyList(1, 2, 3, 4)
print(len(my_list))  # Output: 4
print(my_list[2])    # Output: 3

