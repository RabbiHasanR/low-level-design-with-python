Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.



Problem
Imagine that you’re creating a logistics management application. The first version of your app can only handle transportation by trucks, so the bulk of your code lives inside the Truck class.

After a while, your app becomes pretty popular. Each day you receive dozens of requests from sea transportation companies to incorporate sea logistics into the app.
Great news, right? But how about the code? At present, most of your code is coupled to the Truck class. Adding Ships into the app would require making changes to the entire codebase. Moreover, if later you decide to add another type of transportation to the app, you will probably need to make all of these changes again.

As a result, you will end up with pretty nasty code, riddled with conditionals that switch the app’s behavior depending on the class of transportation objects.


What is the Factory Method Pattern?
The Factory Method Pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. The primary idea is to define an interface for object creation but let the subclasses decide which class to instantiate. This pattern promotes loose coupling by reducing the dependency on concrete classes.

Key Characteristics of the Factory Method Pattern
Encapsulation of Object Creation: The pattern encapsulates the object creation process, making it easier to manage and extend.
Promotes Code Reusability: By separating the object creation code from the main logic, the pattern promotes reusability.
Reduces Dependency: It reduces the dependency on specific concrete classes, making the code more flexible and easier to modify.


Pros of Factory Method Pattern
Encapsulation of Object Creation: The pattern encapsulates the creation logic, making the code easier to manage and extend.
Promotes Flexibility: It allows the code to be flexible, enabling new products to be added without modifying existing code.
Loose Coupling: The pattern reduces dependencies on specific classes, leading to better decoupling.
Improved Code Maintainability: It makes the codebase easier to maintain and modify as the application evolves.


Cons of Factory Method Pattern
Increased Complexity: The pattern can add complexity to the codebase, especially if not needed. It introduces additional classes and interfaces.
Requires More Boilerplate Code: Implementing the pattern requires creating multiple classes and interfaces, which can lead to more boilerplate code.
Overhead in Simple Scenarios: In simpler scenarios where a single constructor is sufficient, the Factory Method pattern may add unnecessary overhead.