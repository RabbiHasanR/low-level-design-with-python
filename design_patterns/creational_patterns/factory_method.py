# Real-World Examples of Factory Method Pattern
# 1. Example: Document Creation
# Imagine a scenario where you have a system that needs to create different types of documents, such as WordDocument and PDFDocument. 
# You can use the Factory Method pattern to encapsulate the creation logic.


from abc import ABC, abstractmethod

# product interface

class Document(ABC):
    
    @abstractmethod
    def create(self):
        pass
    

# concreate products

class WordDocument(Document):
    
    def create(self):
        return "Word document created"

class PdfDocument(Document):
    def create(self):
        return "Pdf document created"
    

# creator interface

class Application(ABC):
    
    @abstractmethod
    def create_document(self) -> Document:
        pass
    
    def new_document(self):
        document = self.create_document()
        return document.create()
    

# Concreate creators
class WordApplication(Application):
    
    def create_document(self) -> Document:
        return WordDocument()
    
class PdfApplication(Application):
    
    def create_document(self) -> Document:
        return PdfDocument()
    


# factory method for create object

class ApplicationFactory:
    
    @staticmethod
    def get_application(application_type: str) -> Application:
        if application_type == 'word':
            return WordApplication()
        
        elif application_type == 'pdf':
            return PdfApplication()
        else:
            raise ValueError(f"Unknown logistics type: {application_type}")
    
# usage

application_type = 'word'
application = ApplicationFactory.get_application(application_type=application_type)
print(application.new_document())  # Output: Word document created

application_type = 'pdf'
application = ApplicationFactory.get_application(application_type=application_type)
print(application.new_document()) # Output: PDF document created


# In this example:

# Product Interface (Document): Represents the common interface for all documents.
# Concrete Products (WordDocument, PDFDocument): Implement the Document interface.
# Creator Interface (Application): Defines the factory method create_document() that returns a Document.
# Concrete Creators (WordApplication, PDFApplication): Implement the create_document() method to return specific document types.


# 2. Example: Transport System
# Consider a logistics application that needs to create different modes of transport, such as Truck or Ship. 
# Using the Factory Method pattern, you can abstract the transport creation logic.

# product interface
class Transport(ABC):
    
    @abstractmethod
    def deliver(self):
        pass

# concreate product
class Truck(Transport):
    
    def deliver(self):
        return "Delivery by land in a truck"


class Ship(Transport):
    
    def deliver(self):
        return "Delivery by sea in a ship"




# creator interface

class Logistics(ABC):
    
    @abstractmethod
    def _create_transport(self) -> Transport:
        pass
    
    
    def plan_delivery(self):
        transport = self._create_transport()    
        
        return transport.deliver()
    


# concrete creators

class RoadLogistics(Logistics):
    
    def _create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    
    def _create_transport(self) -> Transport:
        return Ship()
    
    

# Factory class mehtod with parameters

class LogisticsFactory:
    
    @staticmethod
    def get_logistics(logistics_type: str) -> Logistics:
        
        if logistics_type == 'road':
            return RoadLogistics()
        elif logistics_type == 'sea':
            return SeaLogistics()
        else:
            raise ValueError(f"Unknown logistics type: {logistics_type}")
        

# usage
logistics_type = 'road'

logistics = LogisticsFactory.get_logistics(logistics_type=logistics_type)
print(logistics.plan_delivery()) # Output: Deliver by land in a truck

logistics_type = 'sea'

logistics = LogisticsFactory.get_logistics(logistics_type=logistics_type)

print(logistics.plan_delivery()) # Output: Deliver by sea in a ship
    

# Explanation:
# Transport Interface: Represents the common interface for all types of transport.
# Concrete Products (Truck, Ship): Implement the Transport interface.
# Logistics Interface: Defines the create_transport() method, which is a factory method that subclasses will implement to create specific types of transport.
# Concrete Creators (RoadLogistics, SeaLogistics): Implement the create_transport() method to return specific transport types.
# LogisticsFactory Class: Contains a static method get_logistics() that accepts a logistics_type parameter and returns the appropriate Logistics subclass instance based on that parameter.

