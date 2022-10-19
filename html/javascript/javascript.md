Javascript is used to provide more interactivity to HTML pages.

You can define script in the HTML code itself or refer the external javascript code.

`<script>` element is used to define javascript statements in HTML code. `src` attribute is used to point to an external script file.

## Internal script

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Hello World!</title>
  </head>
  <body>
      <button type = "button" onclick = "showTime()">Display Time </button>
      <p id="currentTime"></p>
      
      <script type = "text/JavaScript">
          function showTime() {
	          document.getElementById('currentTime').innerHTML = new Date().toUTCString();
          }
      </script>
  </body>
</html>
```
### Try yourself [here](https://onecompiler.com/html/3vw3c49hj)

## External script

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Hello World!</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
      <h1 class="title">Hello World! </h1>
      <p id="currentTime"></p>
      <script src="script.js"></script>
  </body>
</html>
```

### script.js

```js
function showTime() {
	document.getElementById('currentTime').innerHTML = new Date().toUTCString();
}
showTime();
setInterval(function () {
	showTime();
}, 1000);
```
### Try yourself [here](https://onecompiler.com/html)

## Check our [Javascript Tutorial](https://onecompiler.com/tutorials/javascript) for more information.
