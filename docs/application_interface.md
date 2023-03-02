## Application Interface
This interface is used to get the user's unique 25 char long user id.
You can use this to keep track of the user as it is different for each bytespace member and does not change.
You are required to give the interface your `appID` (called key here) and `token` (the login token obtained from the `DatabaseInterface`).
```py
from bytespace.interfaces import ApplicationInterface

interface = ApplicationInterface(key="a5b98043-64f8-41cc-92c2-6da6fc4ff056")
interface.connect(token)
```