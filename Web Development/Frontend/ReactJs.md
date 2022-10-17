## Why ReactJS?

Problem:
In traditional web application programming, for even a small change in the webpage, the whole page is reloaded. This makes the web pages slower than they should be.

How ReactJS solves this problem: React only updates what’s necessary.

## What is React?
1. React or ReactJS is a JavaScript library.
2. React is not a framework. (unlike Angular, which is more opinionated).
3. React is an open-source project created by Facebook.
4. React is used to build user interfaces (UI) on the front end.
5. React is the view layer of an MVC application (Model View Controller).

## What is DOM?
The Document Object Model (DOM) is a cross-platform and language-independent API that treats an HTML, XHTML, or XML document as a tree structure. The DOM model represents a document with a logical tree.
![DOM](https://miro.medium.com/max/1100/0*O-1QRlFK3uMnEAbu)

## Virtual DOM
React creates an in-memory data structure cache which computes the changes made and then updates the browser. This allows a special feature which enables a programmer to code as if the whole page is going to render on each change whereas the react library only render components that actually change.
One special thing about ReactDOM.render is that it only updates DOM elements that have changed.

Updating the browser’s DOM is a three-step process in React.

1. Whenever anything has changed, the entire UI will be re-rendered in a Virtual DOM representation first.
2. The difference between the previous Virtual DOM representation and the new Virtual DOM will be calculated.
3. The Real DOM will be updated with that difference. This is very much like applying a patch.

## “Create React App” via npm
Prerequisite:

Install **Node.js** and **npm** globally on your machine.

Fortunately, Facebook has created Create React App, an environment that comes pre-configured with everything you need to build a React app. It will create a live development server, use Webpack to automatically compile React, JSX, and ES6, auto-prefix CSS files, and use ESLint to test and warn about mistakes in the code.

To set up create-react-app, run the following code in your terminal, one directory up from where you want the project to live. Make sure you have 5.2 or higher in Node.js.

*npx create-react-app my-app*

Once that finishes installing, move to the newly created directory and start the project.

*cd my-app*
*npm start*

If you look into the project structure, you’ll see a /public and /src directory, along with the regular node_modules, .gitignore, README.md, and package.json.

In /public, our important file is index.html, which is very similar to the static index.html file we made earlier — just a root div. This time, no libraries or scripts are being loaded in. The /src directory will contain all our React code.

To see how the environment automatically compiles and updates your React code, find the line that looks like this in /src/App.js And replace it with any other text. Once you save the file, you’ll notice localhost:3000 compiles and refreshes with the new data.

Go ahead and delete all the files out of the /src directory, and we’ll create our own boilerplate file without any bloat.

## JSX: Javascript + XML
**We use JSX frequently in ReactJS, let us learn more about it.**
**What is JSX?**

JSX stands for JavaScript XML. JSX is not JavaScript nor HTML.
Eg: const element = <h1>Hello World!</h1>
JSX is a XML syntax extension to JavaScript that also comes with the full power of ES6 (ECMAScript 2015).
Just like HTML, JSX tags can have tag names, attributes, and children. If an attribute is wrapped in curly braces, the value is a JavaScript expression.

## Components
1. Components let you split the UI into independent, reusable pieces.
2. Conceptually, components are like javascript functions. They accept arbitrary inputs (called “props”) and return React elements describing what should appear on the screen.
3. The simplest way to define a component is to write a JavaScript function:
