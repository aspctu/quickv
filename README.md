[![Try on repl.it](https://repl-badge.jajoosam.repl.co/try.png)](https://repl.it/@abuqader/quickv-demo)


quickv
----
quickv is a REST API for a simple key-value store that takes advantage of the internal KV store in Replit. Because of this, quickv only works when deployed on a Replit instance.

It's been particularly useful when I deploy to serverless enviroments (like Vercel) and need a place to store some user-inputted data. 

## How to use 
Fork this repository and import it into Replit. You can sign up for a free account [here](https://replit.com/~). Click "Run" and if you're on the __Hacker__ plan, you can set the Repl to be "always on" meaning faster response times. 

### add
To add a key, make a POST request to `quickv.[your repl username].repl.co/add` with a body that includes a `key` and `value`. If you'd like the value to be a list, set `value` to `[]`. 

If the key already exists, the response will 500, the `success` key wll be set to false and there will be an `error` message `key already exists` 

### get
To get the value for a certain key, make a GET request to `quickv.[your repl username].repl.co/get` with a URL param `key` of the key of interest. For example, if I want to get the value of `names`, I can make a GET request to `quickv.[your repl username].repl.co/get?key=names`. 

If the key doesn't exist, the response will 500, the `success` key wll be set to false and there will be an `error` message `key doesn't exist` 

### update 
To update the value of a certain key, make a POST request to `quickv.[your repl username].repl.co/update` with a body that includes a `key` and `value`. If the initial value was a list, quickv will append the new value instead of overwriting the value. 

If the key doesn't exist, the response will 500, the `success` key wll be set to false and there will be an `error` message `key doesn't exist` 

### delete 
To update the value of a certain key, make a POST request to `quickv.[your repl username].repl.co/delete` with a body that includes a `key`. 

If the key doesn't exist, the response will 500, the `success` key wll be set to false and there will be an `error` message `key doesn't exist` 
