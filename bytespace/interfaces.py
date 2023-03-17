import logging
import requests

from bytespace.exceptions import *
from bytespace.interface import Interface


class DatabaseInterface(Interface):
    """
    DatabaseInterface:
    Makes connections to the bytespace server (bytespace.network) api interfaces.

    Pass the key with DatabaseInterface initialisation.
    Use the `connect()` method to connect to the DatabaseInterface.
    """
    count = 0

    def __init__(self, key):
        super().__init__(key)
        self.name = "DatabaseInterface"
        self.url = self.build_url(f"{self.name}.php")
        logging.debug(f"{self.name}: Created object (count = {DatabaseInterface.count})")

    def connect(self, username=None, password=None, verify=True):
        """
        Makes a connection to the DatabaseInterface.
        If the response is an error an appropriate exception will be raised.
        Otherwise, a login token is returned.

        Automatic verification of login token is conducted via AuthInterface.
        """
        data = {"appID": self._key}

        if username is not None:
            data["username"] = username
        else:
            logging.warning(f"{self.name}: With username=None connection attempt could fail")

        if password is not None:
            data["password"] = password
        logging.warning(f"{self.name}: With password=None connection attempt could fail")

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

        token = res.text.replace("[SUCCESS]", "")

        if verify:
            if AuthInterface(self._key).verify(token=token):
                return token
            else:
                raise InvalidTokenError

        return token

    def __del__(self):
        logging.debug(f"{self.name}: Deleted object (count = {DatabaseInterface.count})")


class AuthInterface(Interface):
    """
    This interface is used to validate a login token.
    This interface is used automatically by the DatabaseInterface,
     so you do not need to verify your tokens when fetching them in this method.
    """
    count = 0

    def __init__(self, key):
        super().__init__(key)
        self.name = "AuthInterface"
        self.url = self.build_url(f"{self.name}.php")
        logging.debug(f"{self.name}: Created object (count = {AuthInterface.count})")

    def connect(self, token=None):

        data = {"appID": self._key}

        if token is not None:
            data["token"] = token
        else:
            logging.warning(f"{self.name}: With token=None connection attempt could fail")

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

    def __del__(self):
        logging.debug(f"{self.name}: Deleted object (count = {AuthInterface.count})")


class ApplicationInterface(Interface):
    """
    The application interface is used for getting user information from bytespace servers.
    By default, this interface get the user's unique id.
    """
    count = 0

    def __init__(self, key):
        super().__init__(key)
        self.name = "ApplicationInterface"
        self.head = "unique"
        self.mode = "READUNIQUE"
        self.url = self.build_url(f"{self.name}.php")
        logging.debug(f"{self.name}: Created object (count = {ApplicationInterface.count})")

    def connect(self, token=None, head="unique", mode="READUNIQUE"):

        data = {"appID": self._key}

        if token is not None:
            data["token"] = token
        else:
            logging.warning(f"{self.name}: With token=None connection attempt could fail")

        data["head"] = head
        data["mode"] = mode

        res = requests.post(self.url, data=data)

        # Checking response
        if "[SUCCESS]" not in res:
            if res.text == "No Token supplied!":
                raise InvalidTokenError()

            elif res.text == "Requested Application couldnt be found!":
                raise InvalidAppIDError()

            else:
                raise BaseInterfaceException()

        logging.debug(f"{self.name}: Connection successful with mode={mode} and head={head}")
        return res.text.replace("[SUCCESS]", "")

    def __del__(self):
        logging.debug(f"{self.name}: Deleted object (count = {ApplicationInterface.count})")

