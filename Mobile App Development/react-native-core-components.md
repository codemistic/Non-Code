# React Native Core Components

## Table of Contents

- [React Native Core Components](#react-native-core-components)
  - [Table of Contents](#table-of-contents)
    - [1. Core Components](#1-core-components)
    - [2. Core VS Native Components](#2-core-vs-native-components)
    - [3. How to import components in React Native ?](#3-how-to-import-components-in-react-native-)
  - [I. View](#i-view)
  - [II. Text](#ii-text)
  - [III. Image](#iii-image)
  - [IV. ScrollView](#iv-scrollview)
  - [V. Button](#v-button)
  - [VI. TextInput](#vi-textinput)

**_React Native_** is an open-source UI software framework created by Meta Platforms, Inc. It is used to develop applications for Android, Android TV, iOS, macOS, tvOS, Web, Windows and UWP by enabling developers to use the React framework along with native platform capabilities.

This **_React Native Core Components Article_** provides a quick overview of all the Core Components that React Native offers and their syntax. It might not cover every edge case, so if you need more information about any of these components, refer to the official [React Native Docs](https://reactnative.dev/)

### 1. Core Components

---

Core components are ready-to-use components available from React Native, which include :

(a) View
(b) Text
(c) Image
(d) ScrollView
(e) Button
(f) TextInput

### 2. Core VS Native Components

---

Each **_core component_** is implemented using its respective **_native component_** counterpart. Since native components are platform-specific, they could look different when rendered on different platforms; therefore the core components provide a layer of abstraction in order to make development of native apps easier and faster.

### 3. How to import components in React Native ?

---

You can import core components into your Expo project from the **_react-native_** package as below :

```
import { View, Text } from 'react-native';
```

Now Let us dive deeper into the core components.

## I. View

---

The **_\<View>_** component is a generic **“visible”** container without any semantic meaning or noticeable performance impact, best translated as **_\<div>_** from web.

**Example**

```
function App() {
  return (
    {/* Base layout structure */}
    <View style={{ flex: 1 }}>
      {/* Simple background color */}
      <View style={{ padding: 8, color: 'red' }}>
        <Text>Text with background color</Text>
      </View>
      {/* Space layout structure */}
      <View style={{ margin: 16 }} />
    </View>
  );
}
```

## II. Text

---

The **_\<Text>_** component is the only way to display text in React Native. These components can be nested to inherit and modify styling.

**Example**

```
<Text style={{ height: 40, borderWidth: 1 }}>
  Here's some text!
</Text>
```

## III. Image

---

The **_\<Image>_** component is an optimized way to render images from various sources, including remote HTTP access, local assets imported with _`require`_, and base64 encoded strings.

**Example**

```
<Image source={require('./local/asset.jpg')} />

<Image source={{ uri: 'https://docs.expo.io/static/images/header/sdk.svg' }} />

<Image source={{ uri: 'data:image/png;base64,<base64-string>=' }} />
```

## IV. ScrollView

---

The **_\<ScrollView>_** component is a generic **“visible”** container with scrolling, but it’s less performant than **_\<View>_**, making it less suitable for simple styling and short lines of text.

**Example**

```
function App() {
  return (
    <ScrollView>
      <Text style={{ margin: 16 }}>Scroll here to see more!</Text>
      <View style={{ marginTop: 1024 }} />
      <Text style={{ margin: 16 }}>Made you look!</Text>
    </ScrollView>
  );
}
```

## V. Button

---

A basic button component that should render nicely on any platform. Supports a minimal level of customization. However it is to be noted that if this button doesn't look right for your app, you can build your own button using TouchableOpacity or TouchableWithoutFeedback. For inspiration, look at the source code for this button component. Or, take a look at the wide variety of button components built by the community.

**Example**

```
<Button
  onPress={onPressLearnMore}
  title="Learn More"
  color="#841584"
  accessibilityLabel="Learn more about this purple button"
/>
```

## VI. TextInput

---

The **_\<TextInput>_** component can capture alphanumeric input from the user. Its behavior can be modified with the onChangeText prop, which accepts a function.

**Example**

```
const [input, setInput] = useState('');

// example use of input
console.log(input);

return (
  <TextInput
    placeholder="What is your name?"
    onChangeText={setInput}
  />
);
```
