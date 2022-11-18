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
from bytespace.interfaces import ApplicationInterface

interface = ApplicationInterface()
interface.connect(key, token)
```

### APITest Interface
```py
from bytespace.interfaces import APITest

interface = APITest()
interface.connect(...)
```

## Changing aspects of the interface

### Interface class

### Changing domain, protocol, etc

### Changing interface specific properties

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

