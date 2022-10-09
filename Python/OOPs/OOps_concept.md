# OBJECT ORIENTED PROGRAMMING 

- `object belongs to user defined class `
- `Classes` : blueprint to create object 
    - Objects 
    - Attributes 
    - Methods 
- eg : 
    - "Classroom" - `class `
    - Students -` object` 
    - roll numbers, marks  - `attributes `
    - listen(), study(), play() - `method`
    - 

 
- Creating an object in a class is called `instantiation` 

## Constructors and methods
- to construct the object according to the blueprint 
- ```py
        def __init__(self,a,b): #constructor definition
            #statements and attributes assignment
            self.variable_a = a
            self.variable_b = b
    ```
- there are a few magic methods 
```py
    def __str__(self):
        return "string to be printed "
    print(object_name) # the object will be put through the str method 
    def __add__(self,other):
        #statements 
        return "the added formatted {}".format(sum)
    print(object_1+object_2)
```
## Inheritance 

## Method overriding 
- look for the method in its own class first and then to the parent class 



