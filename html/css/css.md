CSS(Cascading Style Sheets) is used to style the web pages the way you want. CSS provides various style properties like background color, border-color etc., to style webpages.

You can apply CSS to HTML document in three ways:

## 1. Inline CSS

`style` attribute is used to define CSS properties at each HTML element. You can define multiple properties at once seperated by `;`.

```html
<h1 style = "color:blue; font-size:40px; font-style: italic;"> One Compiler </h1>
```

## 2. Internal CSS

You can define CSS properties using `<style>` tag in `<head>` section. You can use internal CSS to apply styles for a single web page.

```html
<!DOCTYPE html>
<html>
<head>
<style>
body {background-color: pink;}
h1   {color: red;}
h2    {color: green; font-size : 40px; font-style: italic;}
</style>
</head>
<body>

<h1>Heading 1</h1>
<h2>Heading 2</h2>

</body>
</html>
```
### Try yourself [here](https://onecompiler.com/html/3vw2r72yb)


## 3. External CSS

Using external css, you can define all CSS properties in a separate .css file and refer it in HTML file using `<link>` tag. This is usually preferred when you have multiple html pages with same css styling. 

### HTML file
```html
<!DOCTYPE html>
<html>
  <head>
    <title>External CSS example</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
      <h1>Heading 1</h1>
      <h2>Heading 2</h2>
  </body>
</html>
```

### CSS file(styles.css)

```css
body {background-color: pink;}
h1   {color: red;}
h2    {color: green; font-size : 40px;font-style: italic;}

.title {
	color: #5C6AC4;
}
```
### Try yourself [here](https://onecompiler.com/html/3vw363ba7)