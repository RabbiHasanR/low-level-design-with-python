Encapsulation: A fundamental OOP concept that involves bundling data and methods within a class and restricting access to some of the class's components.
Public Attributes: Accessible from anywhere.
Protected Attributes: Indicated by a single underscore _; intended for internal use but still accessible outside.
Private Attributes: Indicated by a double underscore __; access is restricted, and Python applies name mangling to make direct access harder.
Encapsulation in Practice: Use private attributes to protect sensitive data and provide public methods to access and modify that data if needed.
Encapsulation helps ensure that an object’s internal state cannot be directly accessed or modified from outside the class, which helps maintain data integrity and prevents unintended side effects.