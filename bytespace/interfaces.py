from bytespace._interface import Interface
from bytespace.exceptions import *
import requests


class DatabaseInterface(Interface):
    def __init__(self, key):
        super().__init__(key)
        self.name = "DatabaseInterface"
        self.url = self.build_url(f"{self.name}.php")

    def connect(self, username=None, password=None):

        # Making the connection
        data = {"appID": self._key}

        if username is not None:
            data["username"] = username

        if password is not None:
            data["password"] = password

        res = requests.post(self.url, data=data)

        # Checking response
        if "[SUCCESS]" not in res:
            if res.text == "No username supplied!":
                raise MissingUsernameParameterError()

            elif res.text == "No password supplied!":
                raise MissingPasswordParameterError()

            elif res.text == "Requested Application couldnt be found!":
                raise InvalidAppIDError()

            else:
                raise BaseInterfaceException()

        return res.text.replace("[SUCCESS]", "")


class AuthInterface(Interface):
    def __init__(self, key):
        super().__init__(key)
        self.name = "AuthInterface"
        self.url = self.build_url(f"{self.name}.php")

    def connect(self, token=None):

        data = {"appID": self._key}

        if token is not None:
            data["token"] = token

        res = requests.post(self.url, data=data)

        return res.text.replace("[SUCCESS] ", "")

    def verify(self, token=None):
        text = self.connect(token)

        if text == "No Token supplied!":
            raise InvalidTokenError()
        elif text == "Requested Application couldnt be found!":
            raise InvalidAppIDError()
        else:
            return True


class ApplicationInterface(Interface):
    def __init__(self, key):
        super().__init__(key)
        self.name = "ApplicationInterface"
        self.head = "unique"
        self.mode = "READUNIQUE"
        self.url = self.build_url(f"{self.name}.php")

    def connect(self, token=None):

        data = {"appID": self._key}

        if token is not None:
            data["token"] = token

        res = requests.post(self.url, data=data)

        # Checking response
        if "[SUCCESS]" not in res:
            if res.text == "No Token supplied!":
                raise InvalidTokenError()

            elif res.text == "Requested Application couldnt be found!":
                raise InvalidAppIDError()

            else:
                raise BaseInterfaceException()

        return res.text.replace("[SUCCESS]", "")










