Links are hyperlinks present in the web page.

```html
<a href="url">text to appear on link</a>
```
* `target` attribute specifies where to open the link document. For example, open in a new tab.

```html
<a href="url" target="_blank">text to appear on link</a>
```
* **_self** : Default. Opens the link document in the same window or tab
* **_blank** : Opens the link document in a new window or tab
* **_parent** : Opens the link document in the parent frame
* **_top** : Opens the link document in the full body of the window.

## How to create Button as a Link

There are many ways to create a button which acts like a link

* ### Using forms

```html
<form action="https://google.com">
    <input type="submit" value="Google Home page" />
</form>
```
* ### Using formaction attribute

```html
<form>
  <button formaction="https://google.com">Google Home Page</button>
</form>
```
* ### Using Bootstrap CSS library

```html
<a href="https://google.com" class="btn btn-primary">Google Home page</a>
```
* ### Using Javascript

```html
<input type="button" onclick="location.href='https://google.com';" value="Google Home page  " />
```

```html
<button onclick="location.href='https://google.com'" type="button"> Google Home Page</button>
```

