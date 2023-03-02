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