# react

You should NOT use `create-react-app`. See the docs on what they recomend you do instead <https://react.dev/learn/start-a-new-react-project>

Anyway, you'd do it like this

```shell
# npx create-react-app <app_name>
npx create-react-app . 

# run the development server
npm run start
```

install types

```shell
npm i --save-dev @types/react
```

* passing data using props

```js
// src/Welcome.js
import React from 'react'

function Welcome(props) {
    return <h1>Hello, {props.name}!</h1>
}

export default Welcome;
```

```js
// src/App.js
import React from 'react'
import Welcome from './Welcome'

function App() {
    return (
        <div>
            <Welcome name="Alice"/>
            <Welcome name="Bob"/>
            <Welcome name="Charlie"/>
        </div>
    )
}

export default App;
```

* using state

```js
import React, { useState } from "react";

function Counter() {
  // Define state using the useState hook
  const [count, setCount] = useState(0);

  // Handlers to increment and decrement the count
  const increment = () => setCount(count + 1);
  const decrement = () => setCount(count - 1);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Counter</h1>
      <p className="text-lg">Current Count: {count}</p>
      <div className="space-x-2">
        <button
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          onClick={increment}
        >
          Increment
        </button>
        <button
          className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
          onClick={decrement}
        >
          Decrement
        </button>
      </div>
    </div>
  );
}

export default Counter;
```
