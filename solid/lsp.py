# Code Example:
# Let's consider a scenario where we have a base class Vehicle and two derived classes Car and Bicycle.

# Without following the LSP, the code might look like this:


class Vehicle:
    
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print('Starting the car engine...')
        


class Bicyle(Vehicle):
    def start_engine(self):
        # this doesn't make sense for a bicycle
        pass
    


# In this example, the Bicycle class violates the LSP because it provides an implementation for the start_engine method, which doesn't make sense for a bicycle.
# If we try to substitute a Bicycle instance where a Vehicle instance is expected, it might lead to unexpected behavior or errors.

# To adhere to the LSP, we can restructure the code as follows:

class Vehicle:
    
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print('Starting the car engine...')
        


class Bicycle(Vehicle):
    def start(self):
        print("Pedaling the bicycle")
        

# Here, we've replaced the start_engine method with a more general start method in the base class Vehicle. 
# The Car class implements the start method to start the engine, while the Bicycle class implements the start method to indicate that the rider is pedaling.

# Now, instances of Car and Bicycle can be safely substituted for instances of Vehicle without any unexpected behavior or errors.
