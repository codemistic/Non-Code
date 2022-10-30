C++ is a partial OOP language, though it supports Classes, objects, inheritance, encapsulation, abstraction, and polymorphism. As creation of class is optional and you can use global variables which violates encapsulation and you can use friend function in C++ which can access private and protected members of other classes, and hence C++ is not a pure OOP language.

## What is OOP

Object Oriented programming is a methodology based on objects instead of functions and procedures. OOP provides liberty to users to create objects as they want and create methods to handle the objects created. 

## OOP concepts

## 1. Classes and objects

Object is a basic unit in OOP, and is an instance of the class.

Class is the blueprint of an object, which is also referred as user-defined data type with variables and functions.

### How to create a Class

`class` keyword is required to create a class.

### Example

```c
class mobile {
    public:    // access specifier which specifies that accessibility of class members 
    string name; // string variable (attribute)
    int cost; // int variable (attribute)
}; // unlike fucntions class should always end with a semicolon 

```
### How to create a Object

```c
mobile m1;
```
### How to define methods in a class

You can define methods in class in two ways

1. Declare and define inside the class

```c
class mobile {
    public:    // access specifier which specifies that accessibility of class members 
    string name; // string variable (attribute)
    int cost; // int variable (attribute)
    void hello(){//method declaration and definition inside the class
        cout<<"Hello world!!";
    }
};

```
2. Declare inside the class and define it outside

```c
class mobile {
    public:    // access specifier which specifies that accessibility of class members 
    string name; // string variable (attribute)
    int cost; // int variable (attribute)
    void hello(); //method declaration
};

void mobile::hello(){ //method definition
    cout<<"Hello world!!";
}
```
## Constructors :
A constructor is a special type of member function which is called automatically when an object is created.
Example :
```
class  Mobile {
  public:
    // creating a constructor
    Mobile() {
      // code
    }
};
```
## Types of Constructors :

There are three types of Constructors :
### 1. Deafault Constructors :
A constructor with no parameters are called Deafault Constructors. The parameters will be supplied at the time of compilation.

```
class  Mobile {

  public:
     int price;
    // creating a default constructor
    Mobile()// see no parameters has been passed while creating default constuctors
    {
      price = 300;
    }
};
int main()
{
  Mobile m;// Mobile is the class-name and m is an object
  cout<<"$"<<m.price;// output will be the price i.e, $300;
  return 0;
}
```
### 2. Parameterized Contructors :
Constructors with parameters used for data members. Let us see it with an example and it will be much more clearer.
```
class  Mobile {

  public:
     int price;
    // creating a parameterized constructor
    Mobile(int p)//see parameter p (integer) has been passed while creating default constuctors
    {
      price = p;
    }
};
int main()
{
  Mobile m(400);// passing 400 as the parameter
  cout<<"$"<<m.price;// output will be the price i.e, $400;
  return 0;
}
```
### 3. Copy Constuctors :
When one object of class initialize the other object it takes reference to an object of the same class as a argument.
So, the copy constructor in copy data of one object to another.
```
class  Mobile {

  public:
     int price;
    // creating a copy constructor
    //Initializing with parameterized constructor
    Mobile(int p)
    {
      price = p;
    }
    Mobile(Mobile &obj)
    {
        price = obj.price;
    }
};
int main()
{
  Mobile m1(400);// passing 400 as the parameter
  Mobile m2 = m1;//Copying data of object m1 to another object m2
  
  cout<<"$"<<m1.price<<endl;// output will be the price of m1 i.e, $400;
  cout<<"$"<<m2.price<<endl;// output will be same as m1 i.e, $400;
  return 0;
}
```
## 2. Encapsulation

Encapsulation is a mechanism to protect private hidden from other users. It wraps the data and methods as a single bundle. `private` is the keyword used to declare the variables or methods as private.  You can make public `set` and `get` methods to access private variables.

## 3. Abstraction

Data abstraction is a technique which provides only the required data to be visible or accessible to outside world. For example, making a call on a mobile. the logic behind making the call is not visible to others but it provides an abstract details of just call button to outside world.

## 4. Inheritance

Inheritance is a process of acquiring parent properties and behaviour by a child automatically. Hence you can either reuse or extend parent properties or behaviour in the child class. The main advantage of inheritance is code reusability.

### Type of Inheritance
* Single inheritance
    When a child inherits properties from a single parent

* Multiple inheritance
    When a child inherits its properties from two or more parents.

* Hierarchical inheritance
    When multiple children inherit properties from a parent

* Multilevel inheritance
    When a parent properties are inherited by a child which again get interited by another child. For example, B is inherited from A and C is inherited from B. 

    A -> B -> C
* Hybrid inheritance
    Hybrid inheritance is a combination or two or more inheritance types.

## 5. Polymorphism

Polymorphism gives the meaning many forms, usually it occurs when multiple classes are present and have been inherited.

Consider an example of installing an application in your mobile, where your base class is `Mobile` and method is `installation()` and its derived classes could be installApp1, installApp2, installApp3 etc which will have its own implementation but installation method can be common which can be inherited from its base class.

