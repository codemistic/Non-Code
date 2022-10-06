# The Difference between Margin and Padding

Margin and Padding, both are really important parts of a web-page and hence of a web developer's life, and we all know how confusing can it be to differentiate between the two at times. We have all been at a place where we wondered how are the two even different? Or ***Where do we use one and where the other?*** 

Worry not this article will help solve all your confusions.

So Margin v/s padding, let's start with the definitions first.

![box-model.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1662816219369/_hqp976WN.png)

As You can see above, 
> Margin is the space between the border and the next element of your design.

Which means margin is the space which starts after the border of your element, and is outwards from the border.

Whereas,

> Padding is the space that's inside the element between the element and the border.

Which means padding is the space inwards of the border.

If it is still not much clear, don't worry we have a more illustrative example coming up.

Look at the code below,

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Example</title>

    <!-- CSS  -->
    <link rel="stylesheet" href="css/stylesheet.css">
</head>
<body>
    <div class="container-1">
        <h1>Hello</h1>
    </div>
    <div class="container-2">
        <h1>Hello, again</h1>
    </div>
</body>
</html>
``` 

This is the basic HTML file which we'll be styling and working with.

If on the above given code we use this CSS,

```
h1 {
    margin: 0px;
}

.container-1 {
    background-color: antiquewhite;
    margin-bottom: 90px;
}

.container-2 {
    background-color: aquamarine;
}
``` 

This is what the result will be.
![Screenshot_20220910_190936.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1662817206818/4Yzp-MCO7.png)

As you can see, since we used margin instead of padding the gap in between the two divs is filled by the body element and hence the gap is white coloured.

If instead of Margin, we'd have used Padding the result would have been something like this,
![Screenshot_20220910_191143.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1662817318440/WU6NoCy8g.png)

```
h1 {
    margin: 0px;
}

.container-1 {
    background-color: antiquewhite;
    padding-bottom: 90px;
}

.container-2 {
    background-color:aquamarine;
}
``` 

This is the CSS code used for achieving the results above. 

As you can see when we used padding the gap was filled not by the body but by the div itself, that is because padding is applied within the border of that element.

I hope that this blog was helpful and has cleared all your doubts about margin and padding, for more such blogs, follow me on [HashNode](https://hashnode.com/@vanshgoel) and [Twitter](https://twitter.com/_VanshGoel_)
