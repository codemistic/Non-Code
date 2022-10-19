Forms are used to collect user input and then the input is to sent to the server for processing. 

`<form>` element is used to define a form.

```html
<form>
<!--form elements like input select etc-->
</form>
```

Mostly commonly used form attributes

| Attribute | Description |
|----|----|
| action | specify the action how backend script ready to process the data sent.|
| method | GET or POST method to be used to upload data |
| target | Specify the target window or frame like _blank, _parent etc. |
| enctype | specify how the browser encodes the data, for example: **application/x-www-form-urlencoded** |

# Form element - `<input>`

`<input>` element defines what kind of input like text fields, drop-down menus, checkboxes, radio buttons, submit buttons etc.

Some of the most commonly used form controls using `<input>` element.
 
|Type |	Description|
|----|----|
|`<input type="text">` | To define a single-line text input field|
|`<input type="password">` | To define a single-line password input field|
|`<input type="radio">`| To define a radio button |
|`<input type="submit">`| To define a submit button |
|`<input type = "checkbox">`| To define a checkbox |
| `<input type = "file">`| To define a file upload box|


## 1. Text and password input controls

```html
<!DOCTYPE html>
<html>

   <head>
      <title>Text and Password Form Controls</title>
   </head>
	
   <body>
      <form >
         ID : <input type = "text" name = "user-id" /> <br> <!-- Single line text input-->
         Password: <input type = "password" name = "password" /> <br> <!-- Single line password input-->
      </form>
   </body>
	
</html>
```
### Try yourself [here](https://onecompiler.com/html/3vw38t6hu)

## 2. Multi-line text input

Consider you want to give input in more than one line like Address, you can do as shown below:

```html

<!DOCTYPE html>
<html>

   <head>
      <title>Form controls</title>
   </head>
	
   <body>
      <form>
         Address :
         <textarea rows = "6" cols = "70" name = "address">
            Provide your Address here..
         </textarea>
      </form>
   </body>
	
</html>
```
### Try yourself [here](https://onecompiler.com/html/3vw394pwd)

## 3. Radio button form control

```html
<!DOCTYPE html>
<html>

   <head>
      <title>Radio Box Form Control Example</title>
   </head>

   <body>
      <form>
         <input type = "radio" name = "sex" value = "Male"> Male
         <input type = "radio" name = "sex" value = "Female"> Female
         <input type = "radio" name = "sex" value = "unknown"> Rather, not say
      </form>
   </body>

</html>
```
### Try yourself [here](https://onecompiler.com/html/3vw3a9d4g)

## 4. Check box form control

```html
<!DOCTYPE html>
<html>

   <head>
      <title>Checkbox Form Control</title>
   </head>
	
   <body>
      <form>
         <input type = "checkbox" name = "html" value = "on"> HTML
         <input type = "checkbox" name = "javascript" value = "on"> Javascript
         <input type = "checkbox" name = "nodejs" value = "on"> Node JS
         <input type = "checkbox" name = "reactjs" value = "on"> React JS
      </form>
   </body>
	
</html>
```
### Try yourself [here](https://onecompiler.com/html/3vw3b3dr7)



# Form element - `<select>`

`<select>` element is used to define a drop-down menu.

```html
<!DOCTYPE html>
<html>

   <head>
      <title>Select Form Element</title>
   </head>
	
   <body>
      <form>
         <select name = "languages">
            <option value = "english">English</option>
            <option value = "french">French</option>
            <option value = "hindi">Hindi</option>
            <option value = "italian">Italian</option>
            <option value = "japanese">Japanese</option>
         </select>
      </form>
   </body>
	
</html>
```
### Try yourself [here](https://onecompiler.com/html/3vw3b9hrz)

