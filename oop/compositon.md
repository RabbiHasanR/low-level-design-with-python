
Composition in Python OOP
Composition is a fundamental concept in object-oriented programming (OOP) that allows you to build complex objects by combining simpler, more focused objects. Composition represents a "has-a" relationship between classes, meaning that one class contains instances of other classes as attributes. This is in contrast to inheritance, where one class is a type of another class (an "is-a" relationship).

Key Concepts of Composition
"Has-a" Relationship: Composition models a "has-a" relationship. For example, a Car has an Engine, and a House has a Door.
Reusability: By composing objects from other objects, you can reuse those components in different contexts, promoting code reuse and modularity.
Encapsulation: Each component class encapsulates its own behavior and data, making the system easier to understand and maintain.
Flexibility: Composition allows you to change or extend parts of an object without affecting other parts, providing greater flexibility than inheritance.
Composition vs. Inheritance
Inheritance is used when classes share a hierarchical relationship (an "is-a" relationship). For example, a Dog is a type of Animal, so it might inherit from an Animal class.
Composition is used when classes are related by a "has-a" relationship. For example, a Car has an Engine, so the Car class might have an Engine object as an attribute.



Composition vs. Inheritance: When to Use Which
Use Composition:

When you want to create complex objects by combining simpler ones.
When you need more flexibility and encapsulation.
When different parts of your class can change independently.
When your class represents a "has-a" relationship.
Use Inheritance:

When you need to model an "is-a" relationship.
When you want to reuse code from a parent class in a child class.
When you want to extend or modify the behavior of an existing class.