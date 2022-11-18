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

```py
from bytespace.interfaces import DatabaseInterface

interface = DatabaseInterface()
token = interface.connect(key, username, password)
```

### Auth Interface

```py
from bytespace.interfaces import AuthInterface

interface = AuthInterface()
interface.connect(key, token)
```

### Application Interface

```py
from bytespace.interfaces import AuthInterface

interface = ApplicationInterface()
interface.connect(key, token)
```

### APITest Interface
```py
from bytespace.interfaces import APITest

interface = APITest()
interface.connect(key, token, ...)
```

## Changing aspects of the interface

### Interface class

### Changing domain, protocol, etc

### Changing interface specific properties

## Resource download manager

### Images/icons

### CSS/JS files

## Exceptions

## Cache


## Contributors 

