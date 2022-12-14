# bytespace.py
Bytespace (https://bytespace.network/) API library in Python.
This library makes connecting to the bytespace interfaces easier.

### Features
- Interface management 
- Custom Exceptions
- Automatic token verification
- Simple, fast, and easy to understand

## Interfaces

### Database Interface
This interface hosts the login API. By providing the `appID` (listed as key), `username`, and `password` you will receive a login token.
You can use the login token returned to get the unique user id which can be used to keep track of bytespace users in your database.
```py
from bytespace.interfaces import DatabaseInterface

interface = DatabaseInterface(key="a5b98043-64f8-41cc-92c2-6da6fc4ff056")
token = interface.connect(username="username", password="password")
```
If anything information you provide is incorrect an exception will be raised.
The most notable exceptions are `InvalidAppIDError` and `MissingParameterError`.
Please check the exceptions section for more information.

### Auth Interface
This interface is used to verify whether a login token is valid or not. 
By default, the `DatabaseInterface` will verify the login token for you.
However, if in any case you need to verify the token again, 
or perhaps enough time has elapsed that verifying whether the token is still valid is justified.
```py
from bytespace.interfaces import AuthInterface

interface = AuthInterface(key="a5b98043-64f8-41cc-92c2-6da6fc4ff056")
interface.verify(token)
```

### Application Interface
This interface is used to get the user's unique 25 char long user id.
You can use this to keep track of the user as it is different for each bytespace member and does not change.
You are required to give the interface your `appID` (called key here) and `token` (the login token obtained from the `DatabaseInterface`).
```py
from bytespace.interfaces import ApplicationInterface

interface = ApplicationInterface(key="a5b98043-64f8-41cc-92c2-6da6fc4ff056")
interface.connect(token)
```

## Changing aspects of the interface

### Changing domain, protocol, etc
The domain, protocol, and directory are attributes of the interface class.
These attributes are used to build the urls before making a connection to the server.
So, we modify these attributes, the url built will change.
This was created for flexibility as you can modify the domain of where you want to connect to.
This means if bytespace ever changes domain, you can change this and the library will continue to work.

This allows you to modify where, and how, the interface makes connections to.
```py
from bytespace.interfaces import AuthInterface

interface = AuthInterface(key="a5b98043-64f8-41cc-92c2-6da6fc4ff056")
print(interface.protocol)
print(interface.domain)
print(interface.directory)
```
This code creates an `AuthInterface` and prints out all the attributes that makes up the domain built by `AuthInterface`.
```
https
bytespace.network
Intefaces
```
We can change these by modifying them directly.
```py
from bytespace.interfaces import AuthInterface

interface = AuthInterface()
interface.protocol = "http"
interface.domain = "example.com"
interface.directory = "api"
```
This switches the doamin to `http://example.com/api`. 
This means the `AuthInterface` will connect to `example.com` instead of `bytespace.network`.

Every interface also has the attribute `name` which is the name of the interface they are connecting to.
For AuthDatabase, this attribute is set to `"AuthInterface"`.
You can also modify this, although it is not recommended.

## Contributors
Contributing helps keep this library safe and up to date. 
If you want to help, why not create an issue?

<a href="https://github.com/hrszpuk/bytespace.py/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=hrszpuk/bytespace.py" />
</a>


