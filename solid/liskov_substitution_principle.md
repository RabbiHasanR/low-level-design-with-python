
Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.

This means if you have a base class and a derived class, you should be able to use instances of the derived class wherever instances of the base class are expected, without breaking the application.



Liskov Substitution Principle (LSP)
The Liskov Substitution Principle (LSP) is one of the five SOLID principles of object-oriented design. It states that:

"Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program."

In other words, if a class S is a subclass of class T, then objects of type T should be replaceable with objects of type S without altering the desirable properties of the program (e.g., correctness, task performed, etc.). This principle ensures that a subclass can stand in for its parent class without the consumer of the parent class needing to know that a substitution has occurred.

Why LSP is Important
Correctness: Ensures that a subclass maintains the behavior expected from the base class, preserving the correctness of the program.
Interchangeability: Promotes the use of polymorphism, allowing subclasses to be used interchangeably with their base class.
Maintainability: Adhering to LSP makes code easier to maintain and extend, as changes to subclasses do not require changes to the code that uses the base class.



Pros of the Liskov Substitution Principle
Enhanced Correctness: Ensures that the program behaves correctly when substituting subclasses for their parent classes.
Improved Interchangeability: Facilitates the use of polymorphism, allowing different classes to be used interchangeably.
Better Maintainability: Reduces the risk of bugs and issues when extending or modifying a class hierarchy.
Clearer Design: Encourages the design of classes that clearly adhere to their intended responsibilities, leading to more understandable and predictable code.


Cons of the Liskov Substitution Principle
Initial Complexity: Designing systems that adhere to LSP from the start can be more complex and require careful thought about class hierarchies and relationships.
Limited Inheritance: In some cases, LSP can limit the use of inheritance, pushing developers to use composition or interfaces instead, which might lead to a higher number of classes or interfaces.
Overhead in Refactoring: Refactoring an existing codebase to adhere to LSP can be challenging, especially if the violation is deeply embedded in the system. It might require significant changes, including the introduction of new interfaces or abstractions.