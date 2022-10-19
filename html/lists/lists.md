HTML Lists allow developers to display a set of data items in lists like numbering, bullet points etc.

Lists can be of below types:

## 1. Ordered Lists

HTML Ordered Lists are used to list items in a numbered list. `<ol>` tag is used to create ordered lists. Numbering starts from 1 and is incremented by one for each successive ordered list element and are tagged with `<li>`.

```html
<ol type = "1"> <!-- Numeric numbering, default case-->
<ol type = "I"> <!-- Uppercase roman numerals-->
<ol type = "i"> <!-- Lowercase roman numerals-->
<ol type = "A"> <!-- Uppercase letters-->
<ol type = "a"> <!-- Lowercase letters-->
```
```html
<!DOCTYPE html>
<html>

   <head>
      <title>Ordered Lists</title>
   </head>

   <body>
      <ol type = "i">
         <li>Sunday</li>
         <li>Monday</li>
         <li>Tuesday</li>
         <li>Wednesday</li>
         <li>Thursday</li>
         <li>Friday</li>
         <li>Saturday</li>
      </ol>
   </body>

</html>
```
### Try yourself [here](https://onecompiler.com/html/3vw2afjye)

## 2. Unordered Lists

Unordered list items doesn't follow any particular order or sequence. `<ul>` tag is used to create unordered lists and each list item is tagged with `<li>`.

`type` attribute is used to specify the type of the bullet. Among the below types, disc is the default one.

```html
<ul type = "disc"> <!-- default case-->
<ul type = "square">
<ul type = "circle">
```
```html
<!DOCTYPE html>
<html>

   <head>
      <title>Unordered Lists</title>
   </head>

   <body>
      <ul type= "circle">
         <li>Sunday</li>
         <li>Monday</li>
         <li>Tuesday</li>
         <li>Wednesday</li>
         <li>Thursday</li>
         <li>Friday</li>
         <li>Saturday</li>
      </ul>
   </body>

</html>
```
### Try yourself [here](https://onecompiler.com/html/3vw2ja34c)

## 3. Definition Lists

HTML Definition list is used to list the entries like in a dictionary or encyclopedia.

* `<dl>` : Start of the definition list
* `<dt>` : Term
* `<dd>` : Term definition
* `</dl>` : End of the definition list

```html
<!DOCTYPE html>
<html>

   <head>
      <title>Definition List</title>
   </head>
	
   <body>
      <dl>
         <dt><b>OL</b></dt>
         <dd>Ordered Lists</dd>
         <dt><b>UL</b></dt>
         <dd>Unordered Lists</dd>
         <dt><b>DL</b></dt>
         <dd>Definition Lists</dd>
      </dl>
   </body>
	
</html>
```

### Try yourself [here](https://onecompiler.com/html/3vw2mr8hh)

