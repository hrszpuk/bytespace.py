## Database Interface
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