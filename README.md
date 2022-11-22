# bytespace.py
Bytespace (https://bytespace.network/) API library in Python.
This library makes connecting to the bytespace interfaces easier.

### Features
- Interface management 
- Custom Exceptions
- Request/Response cache
- Automatic token verification
- Resource download manager

## Interfaces

### Database Interface
This interface hosts the login API. By providing the `appID` (listed as key), `username`, and `password` you will receive a login token.
You can use the login token returned to get the unique user id which can be used to keep track of bytespace users in your database.
```py
from bytespace.interfaces import DatabaseInterface

interface = DatabaseInterface()
token = interface.connect(key, username, password)
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

interface = AuthInterface()
interface.connect(key, token)
```

### Application Interface
This interface is used to get the user's unique 25 char long user id.
You can use this to keep track of the user as it is different for each bytespace member and does not change.
You are required to give the interface your `appID` (called key here) and `token` (the login token obtained from the `DatabaseInterface`).
```py
from bytespace.interfaces import ApplicationInterface

interface = ApplicationInterface()
interface.connect(key, token)
```

### APITest Interface
This interface is purely for testing the api. 
All arguments passed into this function are embedded into the url.
For POST requests, you must provide a `data` argument that must be a dictionary.
```py
from bytespace.interfaces import APITest

interface = APITest()
interface.connect("test", data={"message": "hello"})
```

## Changing aspects of the interface

### Changing domain, protocol, etc
The domain, protocol, and directory are attributes of the interface class.
These attributes are used to build the urls before making a connection to the server.
So, we modify these attributes, the url built will change.
This was created for flexibility as you can modify the domain of where you want to connect to.
This means if bytespace ever changes domain, you can change this and the library will continue to work.

This allows you to modify where, and how, the interfere makes connections to.
```py
from bytespace.interfaces import AuthInterface

interface = AuthInterface()
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
For AuthDatabase, this attribute is set to `"AuthInterface.php"`.
You can also modify this, although it is not recommended.

### Changing interface specific properties

### Interface class

## Resource download manager

### Images/icons

```py
from bytespace.res import ResourceManager

rm = ResounceManager()
filenames = rm.scan("regex", resource=ICONS)
rm.download(filenames[0])
```

### CSS/JS files
```py
from bytespace.res import ResourceManager

rm = ResounceManager()
filenames = rm.scan("regex", resource=CSS)
rm.download(filenames[0])
```

## Exceptions

## Cache
Internal library cache keeps track of certain request/response pairs, detects when the same parameters are being used, and then instantly delivers the prior response. This is only enabled with certain interfaces, and can be disabled by the user. 

## Contributors 

