# Example of Abstraction
# Real-Life Scenario: Payment System
# Consider a payment processing system where you might have different payment methods like Credit Card, PayPal, 
# and Bank Transfer. Each of these payment methods can process payments, but the details of how they do it are different. 
# Using abstraction, we can define a common interface for all payment methods.


from abc import ABC, abstractmethod

# abastract class

class PaymentMethod(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        pass


# concrete classess implementing the abstract class

class CreditCardPayment(PaymentMethod):
    
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPalPayment(PaymentMethod):
    
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")
        

class BankTransferPayment(PaymentMethod):
    
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of ${amount}")
        


# example usage

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)
    

payment = CreditCardPayment()
make_payment(payment, 100)

payment = PayPalPayment()
make_payment(payment, 200)

payment = BankTransferPayment()
make_payment(payment, 300)



# Built-in Python Classes that Use Abstraction
# Python’s standard library contains several built-in classes that leverage abstraction. A key example is the collections.abc module, 
# which defines abstract base classes for container types like Iterable, Sequence, Mapping, etc.

# Example: Abstract Base Classes in collections.abc
# Let’s look at how the collections.abc.Sequence abstract base class works. It defines the interface for sequence types (like lists and tuples).


from collections.abc import Sequence

class MyList(Sequence):
    
    def __init__(self, *args) -> None:
        self._data = list(args)
        
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __len__(self) -> int:
        return len(self._data)
    
    
    
# example usage
my_list = MyList(1,2,3,4)
print(len(my_list))
print(my_list[2])