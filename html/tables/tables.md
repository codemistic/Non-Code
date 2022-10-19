HTML tables allows the developer to arrange data into rows and columns.

`<table>` tag is used to create a table and `<tr>` tag is used to create table rows and `<td>` tag is used to create data cells.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Table</title>
  </head>
  <body>
      <table border = "1">
         <tr>
            <td>Row 1, Col 1</td>
            <td>Row 1, Col 2</td>
            <td>Row 1, Col 3</td>
         </tr>
         
         <tr>
            <td>Row 2, Col 1</td>
            <td>Row 2, Col 2</td>
            <td>Row 2, Col 3</td>
         </tr>
         
         <tr>
            <td>Row 3, Col 1</td>
            <td>Row 3, Col 2</td>
            <td>Row 3, Col 3</td>
         </tr>
      </table>
  </body>
</html>
```
### Try yourself [here](https://onecompiler.com/html/3vvxwgzab)


You can also define table headings using `<th>` tag.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Table example</title>
  </head>
  <body>
      <table border = "3" width = "300" height = "150" cellpadding = "5" cellspacing = "5">
      <caption>Country and it's official language</caption>
         <tr>
            <th>Country</th>
            <th>Capital</th>
         </tr>
         <tr>
            <td>Russia</td>
            <td>Russian</td>
         </tr>
         <tr>
            <td>US</td>
            <td colspan = "2">English</td>
         </tr>
         <tr>
            <td>UK</td>
            <td>English</td>
         </tr>
         <tr>
            <td>Japan</td>
            <td>Japanese</td>
         </tr>
         <tr>
            <td>India</td>
            <td>Hindi</td>
         </tr>
         <tr>
            <td>France</td>
            <td>French</td>
         </tr>
      </table>
  </body>
</html>
```
### Try yourself [here](https://onecompiler.com/html/3vvy3su9r)

## Table attributes

* ### Cellpadding and Cellspacing

The two attributes are used to to adjust the white space in your table cells. 
    * ***cellspacing attribute:*** Used to define the space between table cells
    * ***cellpadding attribute:*** Used to define the distance between cell borders and the content within a cell.

* ### Colspan and Rowspan

These two attributes are used to merge cells if required.
    * ***colspan attribute:*** Used to merge two or more columns into a single column. 
    * ***rowspan attribute:*** Used to merge two or more rows into a single row.

* ### Border

Border attribute is used to put a border across all the cells of a table.

* ### Height and Width

Table's width and height can be set in terms of pixels or in terms of percentage of available screen area using height and width attributes.

* ### Caption 

You can set caption to the table using `caption` attribute.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Table example</title>
  </head>
  <body>
      <table border = "3" width = "300" height = "150" cellpadding = "5" cellspacing = "5">
      <caption>Country and it's official language</caption>
         <tr>
            <th>Country</th>
            <th>Capital</th>
         </tr>
         <tr>
            <td>Russia</td>
            <td>Russian</td>
         </tr>
         <tr>
            <td>US</td>
            <td rowspan = "2">English</td> <!-- Notice we are merging two rows here-->
         </tr>
         <tr>
            <td>UK</td>
         </tr>
         <tr>
            <td>Japan</td>
            <td>Japanese</td>
         </tr>
         <tr>
            <td>India</td>
            <td>Hindi</td>
         </tr>
         <tr>
            <td>France</td>
            <td>French</td>
         </tr>
      </table>
  </body>
</html>

```

### Try yourself [here](https://onecompiler.com/html/3vvydg4eh)