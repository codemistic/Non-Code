---
title: Javascript-Cheatsheet
description: beginner friendly javascript tips
---
#  JAVASCRIPT CHEAT-SHEET

## what is Javascript

`A programming Language which  performs logic operation and calculation similar to other language but different because of following reasons:-` 

####  - DOM manipulation

A tree like structure of html which can be manipulated through javascript

#### - HTML and CSS just create websites all the movements and interaction is done by js

#### - also called Scripting language 

#### - Add functionality to the HTML

### To add Javascript program into an HTML document

Add **Script Tag** in body of the HTML document 

> Javascript programs run in the console section of the website

### Syntax to print 

`console.log("hello world")`

### Variables

Temporary memorary location to store data

To create a variable in JavaScript, use the ***let*** keyword.

**SYNTAX :** let variableName;

> It doesn't need any datatype to define a variable name that's why It is called ***Loosely typed language.***

### Constant Variable 

A variavle whose value can't be changed.

### Data Types

#### 1. Number 
let num = 123;

#### 2. String
let num = "user";

#### 3. Bigint
let num = 10n;

#### 4. undefined
let num;
console.log(num) //undefined

#### 5. null
let num = null;
It’s just a special value which represents “nothing”, “empty” or “value unknown

#### 6. Boolean
let num = True;

#### 7. Symbol
The purpose of symbols is to create unique property keys that are guaranteed not to clash with keys from other code

### Operators

#### Increment and Decrement

**A++ :** Postfix increment operator-

**A-- :** Postfix decrement operator.

**++A :** Prefix increment operator.

**--A :** Prefix decrement operator.

#### Relational

**< :**  Less than operator.

**> :**  Greater than operator.

**<= :** Less than or equal operator.

**>= :** Greater than or equal operator.

#### Equality 

**== :**  Equality operator.

**!= :**  Inequality operator.

**=== :** Strict equality operator.

**!== :** Strict inequality operator.

####  Logical 

**&& :** Logicl AND.

**|| :**Logical OR.

#### Ternary 

**? : -** condition ? expressionIfTrue : expressionIfFalse

### Loops

### While 
An entry control loop , it checks condition at entry time

**SYNTAX :** 
while(condition)

### Do while
An exit control loop , it checks condition at exit time

**SYNTAX :** 
do
{
    statements
}
while(condition)

### If...else
**if** to specify a block of code to be executed, if a specified condition is true
**else** to specify a block of code to be executed, if the same condition is false
**else if** to specify a new condition to test, if the first condition is false

**SYNTAX :** 
if (condition)
  statement1
else
  statement2

 ### Switch Statement
Switch statements is used to select one of many code blocks to be executed.

**SYNTAX :** 
 switch(expression) {
 case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
}
> ***Switch*** is used for changing values and ***if...else*** is used for range of values

### For 
For statement creates a loop with 3 optional expressions:
**SYNTAX :** 
for (expression 1; expression 2; expression 3) {
  // code block to be executed
}
Expression 1 is executed (one time) before the execution of the code block.

Expression 2 defines the condition for executing the code block.

Expression 3 is executed (every time) after the code block has been executed.

### Functions

A set of instructions or a block of code that performs the task.
It leads to reusability of code and provide structure to code
Anything inside the function will only be executed when it is called.

**SYNTAX :** 
function functionName();

## functions for user interaction
- **Alert :**
This one we’ve seen already. It shows a message and waits for the user to press “OK”.

**SYNTAX :** 
alert("Hello");

- **Prompt :**
The function prompt accepts two arguments:

**SYNTAX :** 
result = prompt(title, [default]);

- **Confirm**
The function confirm shows a modal window with a question and two buttons: OK and Cancel.
The result is true if OK is pressed and false otherwise

**SYNTAX :** 
result = confirm(question);

### Arrays
- Collection of elements of same type.
- Store multiple values at one place.

**SYNTAX :** 
let variablenme = ["","",""];

**To Access Arrays:**
variableName[indexNumber];

## DOM Manipulation

DOM stands for Document Object Model. It is a programming interface that allows us to create, change, or remove elements from a website document. DOM manipulation is when you use JavaScript to add, remove, and modify elements of a website

### Event Handling
Intraction with the webpage by clicking on the webpage or moving the cursor.And after interaction the change happen is called **Events**

``By which we perform these events or interactions like buttons or any key structure they are called ***Event Handlers***``

``And behind all these event handler the code written for that event and event handlers are called ***Event Listeners***``

> To access the elements on the webpage or in the HTML codes we use ***Document***

## Dom Properties

### To change HTML properties

#### document.getElementById(id)
If an element has the id attribute, we can get the element using this method and change its properties

#### document.getElementByClassName(class)
If an element has the class attribute, we can get the element using this method and change its properties

#### document.getElementByTagName(class)
If an element is in the tag, we can get the element using this method and change its properties

#### document.queryselector()
To select a first  element of the CSS selector

#### document.querySelectorAll
All elements inside element matching the given CSS selector are selected.

#### document.innertext/innerhtml 
To make changes inside the HTML code

### To change styling 

#### document.getElementById(id).style.backgroundColor="";
To change backgroundcolor

#### document.getElementById(id).style.color="";
To change Textcolor

#### document.getElementById(id).style.width="";
To change width 

> and so on... we can change the styling

### To change attributes of CSS

#### document.setAttribute() 
method sets a new value to an attribute

#### document.getElementById(id).setAttribute.("href","url")="";
To change the link

#### document.getElementById(id).setAttribute.("src","url")="";
To change the image 

#### document.getElementById(id).setAttribute.("type","text")="";
To change Input(of html code input) type 

#### document.getElementById(id).placeholder="text";
To change the value of placeholder

### Mouse events

**mousedown/mouseup :**
Mouse button is clicked/released over an element.

**mouseover/mouseout :**
Mouse pointer comes over/out from an element.

**mousemove :**
Every mouse move over an element triggers that event.

**onclick :**
Triggers after mousedown and then mouseup over the same element if the left mouse button was used.

**dblclick :**
Triggers after two clicks on the same element within a short timeframe. Rarely used nowadays.






















