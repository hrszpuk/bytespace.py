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
    pass


class ApplicationInterface(Interface):
    pass


class APITest(Interface):
    pass








