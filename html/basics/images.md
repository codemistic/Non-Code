Images enhances the appearance of a web page. They are defined using `<img>` tag. Please note that `<img>` tag contains only attributes, and does not have a closing tag.

```html
<img src="image-url" alt="alternative text" />
```

If a browser cannot able to view an image for some reason, it will display the value of the alt attribute.

You can also specify the width and height of an image.

```html
<img src="roses.jpg" alt="rosegarden" width="500" height="600" />
```
Alternatively, you can also use `style` attribute to mention height and width of an image.

```html
<img src="roses.jpg" alt="rosegarden" style="width:500px;height:600px;" />
```

## How to access the images present in other web page

```html
<img src="url" alt="alt-text" />
```

## How to add a background image

```html
<div style="background-image: url('imagename');">.. </div>
```

* To add background image on a page

```html
<style>
body {
  background-image: url('imagename');
}
</style>
```

## How to add image as a link

```html
<a href="default.asp">
  <img src="imagename" alt="alternative-text" style="width:50px;height:50px;">
</a>
```
