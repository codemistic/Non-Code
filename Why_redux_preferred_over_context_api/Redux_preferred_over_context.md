# WHY REDUX IS PREFERRED OVER CONTEXT

## Let's us begin with the introduction.

# INTRODUCTION:

### Consider a tree

### A

### / \

### B C

### /\ /\

### D E F G

The data in react always flow from parent to child component which makes it unidirectional.
So A can pass data to B same as B can also pass data to E but E cannot pass to B, which shows that data can be passed through parent to child but not child to parent.

**So how would E gets data from A**
This is what called Prop drilling.

## PROP DRILLING & CONTEXT API

If E wants to take data from A then the flow will be like A->B->E. This is known as prop drilling passing data to every component.

## DISADVANTAGE OF PROP DRILLING

For E to get data from A we have to pass data to all the components in between (here in ex it's B), even if they do not need that data.
So this problem was removed by Context api in react where data from A can directly pass to E .

### Redux also work on the same concept , passing data directly from A to E.

# WHY REDUX PREFERRED OVER CONTEXT.

## 1. Redux is used for large applications(more states) and context is used for small applications(less states).

**Reason->** When we update state of any component using context ,all components are rendered but in redux only those components are rendered whose states are changed.

**Example->** Suppose there are two states, one is counter whose value increases on clicking and the other is dark mode (theme change) and we have changed theme from dark mode to light mode but haven't updated the counter value.

Now if we have used context ,even if we have updated theme only but still both the states will be rendered.
But if we have used redux it will only render the value of theme and not the value of counter.

So in applications having large number of states(say 100) it will be very cubersome that all the states are rendered , even if we have updated only single state.

This will lead to performance issue that's why redux is preferred.

## 2. Redux have middlewares but context does not give any thing like this.

**Reason->** we know that the flow of redux is : .

Data from App----->Action----->Reducer------>Store----->Any component which wants data.

**Middlewares comes in between of action and reducers.**

They are used to execute a piece of code when a action is dispatched , before sending it to reducer.
If that piece of code executes successfully then action gets dispatced to reducer followed by store , otherwise action does not get disptached to reducer and store does not get updated.
so when there is a need of middlewares in the application then redux is preferred to use because context does not provide such a functionality.

**Example->** Redux thunk is a middleware.

## 3. Redux provide Redux-persist lib (local storage) ,but context does not.

**Reason->** Redux persist allows to save/store data in local storage and when we refresh page the state remains same and do not get lost(or come back to intial stage).

**Example->** Suppose if we have a counter button and on clicking ,its state changes means number get's increased by 1.Suppose we have increased the number upto 5,and now refresh the page, the state will remain same as 5 and does not get to its intial state that is 0, because the state gets stored in the local storage , and will never come to its intial stage even after refresh . It will come to its intial state when we will delete it from the local storage.

Context api does not support this local storage property and state always comes to its intial state after refresh.

**Example->** If we use context for Theme implementation(dark mode and light mode) , and intial value is light mode and we switched to dark mode then eveytime we refresh the site or close the site , it will again come back to light mode , but if we use redux which supports persist then our dark mode will remain same.

## 4. Debugging is hard in context but easy in redux.

**Reason->** Redux provide 'redux dev tools' for debugging which makes debugging very easy,but it can be hard in context with highly nested react component structure even with dev tools.

## 5. Adding new context requires creation from scratch but redux is easily extendible due to the ease of adding new data after the intial step.

# CONCLUSION

1. So if we want to implement such functionalities then redux is much better option.
2. React redux uses context internally ,but it does not expose this fact in public api.
3. So we should feel safer if we use context via redux than directly because if it changes , the burden of updating the code will be on redux and not us.
4. But Redux is much complex to understand and code than context.
5. So if there are less states used , and no need of middlewares and all other extra functionalities, use context because it has less time complexity , and much simpler to understand.

**This article is contributed by Nikita Gupta**.