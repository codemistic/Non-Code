# Web Development HTML 101

# Introduction to HTML

## Topic: HTML Introduction

---

### Notes

- Foundation of all websites
- Hyper Text Markup Language
- Heading tags go from `<h1>`to `<h6>` and as the number increases the size of the text decreases; It requires an opening and a closing tag.
- For learning about any element search (**mdn /w3 schools** <language> <element>) or go to [**devdocs.io**](https://devdocs.io/)
- The line break tag  `<br>` adds some space between any two elements; It does not require a closing tag (is a self-closing tag)

## Topic: The Anatomy of an HTML Tag

---

### Notes

- `<hr size=”3”>` → red one is the **element** and the green one is the **attribute**
- attribute comes after the main element and is separated by a single space
- `<hr>` attributes → align; colour; no shade; sign; width
- for a comment in HTML we use `<!— kdsjfklds jldsls —>`
- for aligning the text to the center we use the element `center>` `</center >`

## Topic: What is HTML Boiler Plate

---

### Notes

- index.html is the name that devs give to their home page
- To create any website you need to write boilerplate code in  VS code use `<!+enter>`
- utf-8 is the standard encoding that we use with HTML 5 because it includes all the international symbols, every single symbol that is there in the Unicode character set.
- To add emojis or any kind of letter go to [Unicode Table](https://unicode-table.com/en/)
- `<meta charset="utf-8">` This gives your website maximum chance of getting rendered correctly when opened in any part of the world

## Topic: How to Structure Text in HTML

---

### Notes

- Always Indent your code cause it makes it easier for anyone to review it.
- For italicizing your text you can use `<i>` or `<em>` but there is a subtle difference between the two
- `<em>` Emphasis tag represents stress emphasis on its content. Whereas the `<i>` italicize tag represents text that is set out from the normal prose
- Emphasis tag just provides more information to the browser.
- Similarly, to bold a text we should use `<strong>` rather than `<b>`
- The `<strong>` tag says that this word has strong importance therefore it must be bolded rather than merely saying that this text should be styled so that it looks darker that the rest of the text.

## Topic: HTML lists

---

### Notes

- There are two types of lists: Ordered lists and Unordered lists
- Ordered list `<ol>` → Numbered
- Unordered list`<ul>` → Bulleted

## Topic: HTML Image Element, Links and Anchor Tags

---

### Notes

- `<img src="images/profpic.png" alt="Rachit's Profile Picture" height="150">`
- Image Element; Link of the Image; Text if image not loaded; Size of the Image
- **Image Element** can fetch images from the **web** as well as the **computer** (in case of computer you have to specify the path of the image if it is in a different folder than the HTML file). If you want to upload an image for the link do it on [Photo Bucket](http://www.photobucket.com)
- `<a href="https://www.instagram.com/gardenestic/">Gardening</a>`
- Anchor element; ——————Link——————; Name of the link
- Anchor Element creates a hyperlink to web pages, files, email addresses, locations on the same page, or anything else a URL can address.

## Topic: HTML Tables

---

### Notes

- `<table>` `</table>` → Table Element
- `<tr>` `</tr>` → Creates a Table Row
- `<td>`  `</td>` → Creates a Cell/Column
- `<thead>` `</thead>` → Header
- `<tbody>`  `</tbody>` → Body
- `<tfoot>`  `</tfoot>` → Footer
- `<tr>` Text remains normal   `<th>` Text gets bold

### Format

```html
<table>
<thead>
    S.No.
</thead>
<thead>
   Name
</thead>
<thead>
    Number
</thead>
<tr>
    <td>1.</td>
    <td>rachit</td>
    <td>9584258725</td>
</tr>
</table>
```

## Topic: HTML Forms

---

### Notes

- Through forms you can take user input
- `<form> </form>`
- `<label> </label>`
- `<input type="text">`

(forms in detail in java script)

---

<aside>
💡 To learn more about HTML you can head over [here](https://developer.mozilla.org/en-US/docs/Web/HTML).

</aside>