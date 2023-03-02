## Auth Interface
This interface is used to verify whether a login token is valid or not. 
By default, the `DatabaseInterface` will verify the login token for you.
However, if in any case you need to verify the token again, 
or perhaps enough time has elapsed that verifying whether the token is still valid is justified.
```py
from bytespace.interfaces import AuthInterface

interface = AuthInterface(key="a5b98043-64f8-41cc-92c2-6da6fc4ff056")
interface.verify(token)
```