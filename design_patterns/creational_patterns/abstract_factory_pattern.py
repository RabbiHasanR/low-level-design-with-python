# Real-World Examples of Abstract Factory Pattern
# 1. Example: GUI Toolkit (Cross-Platform UI Components)
# Imagine you are developing a cross-platform GUI application that needs to create UI components like buttons and checkboxes. 
# Depending on the platform (e.g., Windows, macOS, Linux), the appearance and behavior of these components will vary. 
# The Abstract Factory pattern can be used to create a suite of related UI components for each platform.


from abc import ABC, abstractmethod

# abstract product interface
class Button(ABC):
    
    @abstractmethod
    def render(self):
        pass


class CheckBox(ABC):
    @abstractmethod
    def render(self):
        pass
    
    
# concreate product for windows
class WindowButton(Button):
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size

    def render(self):
        return f"Rendering a {self.size} Windows Button in {self.color} color"

class WindowCheckbox(CheckBox):
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size

    def render(self):
        return f"Rendering a {self.size} Windows Checkbox in {self.color} color"
    


# concreate product for mac

class MacButton(Button):
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size

    def render(self):
        return f"Rendering a {self.size} macOS Button in {self.color} color"
    
class MacCheckbox(CheckBox):
    
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size

    def render(self):
        return f"Rendering a {self.size} macOS Checkbox in {self.color} color"
    


# abstract factory interface

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self, color: str, size: str) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self, color: str, size: str) -> CheckBox:
        pass
    

# concreate factories

class WindowFactory(GUIFactory):
    def create_button(self, color: str, size: str) -> Button:
        return WindowButton(color, size)

    def create_checkbox(self, color: str, size: str) -> CheckBox:
        return WindowCheckbox(color, size)
    
class MacFactory(GUIFactory):
    def create_button(self, color: str, size: str) -> Button:
        return MacButton(color, size)

    def create_checkbox(self, color: str, size: str) -> CheckBox:
        return MacCheckbox(color, size)
    
    


# factory provider with parameters

class GUIFactoryProvider:
    
    @staticmethod
    def get_factory(platform_type: str) -> GUIFactory:
        if platform_type == 'window':
            return WindowFactory()
        elif platform_type == 'mac':
            return MacFactory()
        
        else:
            raise ValueError(f"Unknown platform type: {platform_type}")
        
# client code

def client_code(factory: GUIFactory, button_color: str, button_size: str, checkbox_color: str, checkbox_size: str):
    button = factory.create_button(button_color, button_size)
    checkbox = factory.create_checkbox(checkbox_color, checkbox_size)
    print(button.render())
    print(checkbox.render())
    
    

# usage
factory = GUIFactoryProvider.get_factory('window')
client_code(factory, "red", "large", "blue", "small")
# Output:
# Rendering a large Windows Button in red color
# Rendering a small Windows Checkbox in blue color
    
factory = GUIFactoryProvider.get_factory("mac")
client_code(factory, "green", "medium", "yellow", "large")
# Output:
# Rendering a medium macOS Button in green color
# Rendering a large macOS Checkbox in yellow color



# 2. Example: Vehicle Manufacturing (Family of Parts)
# Consider a vehicle manufacturing system where different types of vehicles (e.g., cars, motorcycles) 
# require different families of parts (e.g., engines, tires). 
# The Abstract Factory pattern can be used to create compatible parts for each vehicle type.

# abstract product interface
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class Tire(ABC):
    @abstractmethod
    def roll(self):
        pass
    


# concreate products for cars

class CarEngine(Engine):
    def start(self):
        return "Car Engine starting"
    
class CarTire(Tire):
    def roll(self):
        return 'Car Tire Rolling'
    

# concreate products for motorcycle
class MotorCycleEngine(Engine):
    def start(self):
        return "Motorcycle engine starting"

class MotorCycleTire(Tire):
    def roll(self):
        return "Motorcycle tire rolling"
    

# abstract factory interface
class VehicleFactory(ABC):
    @abstractmethod
    def create_engine(self):
        pass
    
    @abstractmethod
    def create_tire(self):
        pass
    


# concrete factories

class CarFactory(VehicleFactory):
    def create_engine(self):
        return CarEngine()
    def create_tire(self):
        return CarTire()
    
class MotorCycleFactory(VehicleFactory):
    def create_engine(self):
        return MotorCycleEngine()
    def create_tire(self):
        return MotorCycleTire()
    
    

# factory provider with parameter

class VehicleFactoryProvider:
    
    @staticmethod
    def get_vehicle_factory(vehicle_type: str) -> VehicleFactory:
        if vehicle_type == 'car':
            return CarFactory()
        elif vehicle_type == 'motorcycle':
            return MotorCycleFactory()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
        

# client code

def client_code(factory: VehicleFactory):
    engine = factory.create_engine()
    tire = factory.create_tire()
    
    print(engine.start())
    print(tire.roll())
    


# usage
factory = VehicleFactoryProvider.get_vehicle_factory('car')
client_code(factory)
# Output:
# Car Engine starting
# Car Tire Rolling
    
factory = VehicleFactoryProvider.get_vehicle_factory('motorcycle')
client_code(factory)
# Output:
# Motorcyelc Engine starting
# Motorcyelc Tire Rolling