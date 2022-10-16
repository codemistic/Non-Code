# ALL ABOUT CONSTRUCTORS.

**In this article we will learn everything about constructor in detail.**
**Pre-requisite is : well understanding of classes and object**.

# Introduction 

1. Constructors is a member function of a class.
   
   **Member function:** A member function is a function which is defined inside a class.It operates on object of the class .
###   ex - class student
###   {
###       private: 
###               int x ,y;
###       public: 
###             void add(int a , int b)
###             {
###                x=a;
###                y=b;
###             }
###   };
###   main()
###   {
###    student s;
###   }

   It has access to all the members of a class for that object. Here add() can access x and y .

2. The name of the constructor is same as class.
   
3. It has no return type .
   
4. A constructor must be an instance member function , i.e, it cannot be static,because a constructor cannot be called without an object . When an object or instance is created it gets automatically called.
   
5. It should always be public.

6. It is implicitly invoked(called) when an object is created.

7. It is used for intialization of variables.

# TYPES OF CONSTRUCTOR

There are three types of constructors.

1. **Default constructors:**  Default constrcutors are those which have no parameters,and are automatically called by the compilers , when an object of a class is created.

If we have made our own default constructor then on creating object our own constructor will call otherwise if no user-defined constructor exists for a class , the compiler implicitly declares a default parameterless constructor **A::A()** , where A->class.

2. **Parameterized constructors:** Parameterized constructor are those contructors which have arguments.

They are not automatically called by the compiler,instead if needed we have to call it.

### Example:
### class student
### {
###   private:
###            int a ,b;
###   public:
###          student(int x , int y)
###          {
###           a=x;
###           b=y;
###          }
### }
### main()
### {
###   student s1(3,4);
### }

where student is the name of the class.
   
3. **Copy constructors:** A copy constructor is a member function that initializes an object using another object of the same class. In other words, a constructor which creates an object by initializing it with an object of the same class, which has been created previously is known as a copy constructor.  

### Example:

### class student
### {
###   private:
###           int a ,b;
   
###   public:
###          // default constructor

###          student()
###          {
###            cout<<"default constructor"<<endl;
###          }

###          // copy constructor

###          student(const student &obj)
###          {
###           cout<<"Copy constructor"<<endl;
###          }

### }
### main()
### {
###   student s1;
###   student s2 = s1;
###   return 0;
### }

## Why it is necessary to pass argument by reference in copy constructor?.

If argument is not passed by reference then it must be passed by value. However if we passed it by value , then s1 value will get copy to obj and since s1 and obj both are objects and s1 value is copied to obj it means one objects value is copying to other object which is nothing but calling of copy constructer again and again ,results in a recursion or infinte calling of copy constructer until compiler runs out of memory.

## Why const is used when passing arguments to the copy constructor?.

Since const is not necessary to be used but reason for passing const reference is, wherever possible so that objects are not accidentally modified.

### Example:

### class student()
### {
###   public:
###           int x;

###           student()
###           {
###            cout<<"default constructor"<<endl;
###            x=5;
###           }
###           student(student &obj)
###          {
###            cout<<"copy constructor"<<endl;
###            obj.x=10;    // accidental modification.
###           }
### }

### main()
### {
###  student s1;
###  student s2 = s1;
###  cout<< s1.x << endl;
### }

output = default constructor.
         copy constructor.


**Notice x value have been accidently modified**.

so if we use const then we are not able to modified the value if we do then it will give an error.

## TYPES OF COPY CONSTRUCTOR.

1. **Default copy constructor:** It is called by the compiler when we haven't made any copy constructor by ourself.

### Example:
### class Student{
###    int id;
  
### public:
###    void fun(int x) { id = x; }
###    void display() { cout << endl << "ID=" << id; }
### };
  
### int main()
### {
###    Student obj1;
###    obj1.fun(10);
###    obj1.display();
  
###    // Implicit Copy Constructor Calling

###    Student obj2(obj1); // or obj2=obj1;
###    obj2.display();
###    return 0;
### }

output -> ID=10.
          ID=10.


### NOTE: When object is created compiler call 2 constructer automatically-> one is default constructor and other is copy constructor.

2. **User Defined Copy Constructor:** It is made by user.

### Example:

### class Student
### {
###    int id;
###    public:
###    void fun(int x)
###    {
###        id=x;    
###    }    
###    Student(){}  //default constructor with empty body
      
###    Student(Student &t)   //copy constructor
###    {
###        id=t.id;
###    }
###    void display()
###    {
###        cout<<endl<<"ID="<<id;
###    }
### };
### int main()
### {
###    Student obj1;
###    obj1.fun(10);
###    obj1.display();
      
###    Student obj2(obj1); //or obj2=obj1;    copy constructor called
###    obj2.display();
###    return 0;
### }

Output:.
ID=10.
ID=10.

### NOTE: If we don’t define our own copy constructor, the C++ compiler creates a default copy constructor for each class which does a member-wise copy between objects. The compiler-created copy constructor works fine in general. We need to define our own copy constructor only if an object has pointers or any runtime allocation of the resource like a file handle, a network connection, etc.

## Differnce between Copy constructor and assignment operator.

The main differnce is copy constructor makes a new memory storage every time it is called while the assignment operator does not make new memory storage.

A copy constructor is called when a new object is created from an existing object, as a copy of the existing object. The assignment operator is called when an already initialized object is assigned a new value from another existing object. 

### Ex - 
### Student s1, s2;
### Student s3 = t1;  
### s2 = s1;          

## Can a copy constructor can be made as private?.

Yes,When we make a copy constructor private in a class, objects of that class become non-copyable. This is particularly useful when our class has pointers or dynamically allocated resources. In such situations, we can either write our own copy constructor or can make it private.

## Why we should make user defined copy constructors when we have pointers or dynamically allocated objects?.

As we know that when we do not make copy constructors , compiler make default copy constructor for us.

But there are certain problems in default copy constructors when we are dealing with 
pointers or dynamically allocated resources.

1. When we have members which dynamically get initialized at run time, the default copy constructor copies this member with the address of dynamically allocated memory and not a real copy of this memory.

Means default copy constructor makes a shallow copy 

ex: obj1 ----> abc <-----obj2.

this shows that both obj1 and obj2 are pointing to the same memory.

1. Since both objects are pointing to same memory , changes in one reflects in another object.

2. Also there can be of dangling pointers i.e , when we delete one of these objects another object still points to the same memory.

# CONSTRUCTORS IN CASE OF INHERITANCE

Th order of calling of constructors in case of inheritance is child to parent, but execution order is from parent to child.

Ex-

### class A
### {
###   public:
###         A(){}

###  };

### class B:public A
### {
###   public:
###           B():A(){}
### }
### void main()
### {
###   B obj;
### }

When an obj of class B is created then it calls default constructor of class B but since class B is derived from class A so B():A() , either we will write this line or if we do not write then compiler will write it . 
This lines means that first class A constructor will be called then class B.

# CONCLUSION 

1. When a class has no constructor then compiler makes 2 constructor:default and copy.

2. If we have made a constructor in a class but that constructor is not copy constructor
 then compiler will not automatically make default constructor but it will still automatically make copy constructor.

3. When we have made copy constructor then compiler will neither make default constructor nor copy constructor automatically.

**This article is contributed by NIKITA GUPTA**.

