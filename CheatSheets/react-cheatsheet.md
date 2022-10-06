# React & JSX Cheatsheet

Overview | |
---------|-|
JSX HTML | `<div>...</div>`
JSX Component | `<Component property={javascript} />`<br>`<Component property='string' />`
JSX Component with Children | `<Component>{children}</Component>`<br>reference: `props.children`
Escaping JavaScript | `{...}`
`require` statements | `const React = require('react');`<br>`const ReactDOM = require('react-dom');`
`npm` modules | `react`, `react-dom`
Render in DOM | `ReactDOM.render(<MyApp />, document.getElementById('root'));`
Functional components | `function MyComponent(props) { return <div>...</div> }`
Base class for class components | `React.Component`
First statement in constructor | `super(props)`
Initializing state | `this.state={...}`
Setting state | `this.setState({...})`
Referring previous state | `this.setState(prevState => ({...}))`<br>`this.setState((prevState, props) => ({...}))`

## Functional Component
```jsx
'use strict';

const React = require('react');

function Greeting(props) {
   return (
      <h1>{props.salutation + ' ' + props.who + '!'}</h1>
   );
}
const world='world';

<Greeting salutation='hello' who={world} />
```

## Class Component with State
```jsx
class MyComponent extends React.Component {
   constructor(props) {
      super(props);
      this.state = {property: 'initial'};
      this.handleClick = this.handleClick.bind(this);
   }
   render() {
      return (
         <div>
            <button onClick={this.handleClick}>Click me!</button>
            <div>{this.state.property}</div>
         </div>
      );
   }
   handleClick() {
      this.setState({property: 'clicked'});
   }
}
```

## Render React Component in DOM
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>React is cool!</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="https://example.com/transformed-with-babel.js"></script>
  </body>
</html>
```
```javascript
'use strict';

const React = require('react');
const ReactDOM = require('react-dom');
const MyCoolApp = require('./my-cool-app.js');

ReactDOM.render(
   <MyCoolApp />,
   document.getElementById('root')
);
```

## Component with Children
```jsx
const borderStyle = {
   border: '1px solid darkcyan',
   boxShadow: '5px 5px 5px gray',
   margin: '10px',
   padding: '5px'
};

function Border(props) {
   return (
      <div style={borderStyle}>
         {props.children}
      </div>
   );
}
```

## HTML vs Web API vs React JSX

Difference | HTML | Web API | React JSX
-----------|------|---------|------------
Names of attributes / properties | lower case | (mostly) camelCase | **camelCase**
Values of attributes / properties | string | expression | expression within `{ }`
Names of event handlers (on...) | lower case | lower case (!) | **camelCase**
Values of event handlers (on...) | JavaScript string | function expr. | function expr. within `{ }`
Event Handlers: prevent default behaviour | n/a | can return `false` | must call `event.preventDefault();` 
HTML Tags | lower case | n/a* | lower case
Custom Tags (Components) | n/a | n/a | start with **capital letter**

*<nbsp>Represented by API objects and interfaces like `Document`, `HTMLDivElement`, ...

### Examples
HTML Attribute | HTML Example | JSX Property | JSX Example
---------------|----------------|--------------|--------------
class | `<div class='fancy'>...</div>` | className* | `<div className='fancy'>...</div>`
onclick | `<button onclick="foo()">...` | onClick* | `<button onClick={foo}>...`<br>`<button onClick={() => foo(param)}>...`
tabindex | `<input tabindex=2 />`| tabIndex | `<input tabIndex={2} />`

*<nbsp>**Note:** `className` is identical to the Web API, while `onClick` is not!<br>
See also on MDN web docs:
[Element](https://developer.mozilla.org/en-US/docs/Web/API/Element),
[HTMLElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement),
[GlobalEventHandlers](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers)

### Special Tags
Tag | HTML behaviour | React behaviour
----|----------------|----------------
`<textarea>` | content defined by children | content defined by `value` attribute
`<select>` and `<option>` | selection defined by presence of `selected` attribute on `<option>` |  selection defined by `value` attribute on `<select>`

## Inline CSS vs React Inline Style

Difference | Inline CSS | React Inline Style
-----------|------------|-------------------
The `style` Attribute / Property | a string enclosed by `"` or `'` | an object eclosed by `{ }`
Name of style properties | lower case with hyphen `-` | camelCase
Value of style properties | CSS expression (textual) | JavaScript expression
Separator | `;` | `,`
Can be merged | no | yes, e.g. with Object.assign()
Can use variables | no | yes

### Examples
CSS Property | CSS Inline Style Example | React Style Property | React Inline Style Example
-------------|--------------------------|----------------------|---------------------------
background-color | `style="background-color: green"` | backgroundColor | `style={{backgroundColor: 'green'}}`
border | `style="border: 1px solid black"` | border | `style={{border: '1px solid black'}}`
border-style,<br>border-width | `style='border-style: solid; border-width: 5'` | borderStyle,<br>borderWidth | `style={{borderStyle: 'solid', borderWidth: 5}}`

## Lifecycle Methods
Lifecycle | Method
----------|-------
Before component gets unmounted | `componentWillUnmount()`
After component got mounted | `componentDidMount()`
Before is updated (receives new state or props) | `componentWillUpdate(nextProps, nextState)`
After component was updated | `componentDidUpdate(prevProps, prevState)`

## Tips & Tricks
<nbsp> | <nbsp> |
-------|--------|
Make `this` available in event handler | in constructor: `this.handleEvent = this.handleEvent.bind(this);`
Use id in loop | `<button onClick={(e) => this.method(id, e)}>...` or<br>`<button onClick={this.method.bind(this, id)}>...`
Conditional rendering: Logical && Operator | `{condition && <SomeComponent>...}`
Conditional rendering: Ternary Operator | `{condition ? (<TrueComponent>...) : (<FalseComponent>...)}`
Prevent component from rendering | return `null` in `render()` method / component function
Prevent navigation | `href="#"`<br>`<a href="#" onClick={...}>...</a>`
Reuse event handler for multiple HTML elements | Assign a custom `name` attribute and evaluate that attribute<br>with `event.target.name` in event handler. See: [React Quick Start](https://reactjs.org/docs/forms.html#handling-multiple-inputs)

## Babel
**Preset:** `react`
### Manual Transformation
```javascript
const babel = require('babel-core');
let transformed = babel.transform(code, {"presets": ["react"]}).code;
```

## CSS for Full Page
```css
html, body, #root {
   margin: 0;
   height: 100%;
   width: 100%;
}
```