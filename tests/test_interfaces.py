# Bytespace imports
from bytespace.interfaces import DatabaseInterface
from bytespace._interface import Interface
from bytespace.exceptions import *

# Testing imports
from unittest import TestCase
import requests
import random


def test_build_url_simple():
    interface = Interface()
    for _ in range(100):
        r = str(random.randint(0, 100))
        assert interface.build_url(r) == f"https://bytespace.network/Interfaces/{r}"


def test_build_url_complex():
    interface = Interface()

    interface.protocol = "ftp"
    for _ in range(100):
        r = str(random.randint(0, 100))
        assert interface.build_url(r) == f"ftp://bytespace.network/Interfaces/{r}"

    interface.domain = "bytespace.net"
    for _ in range(100):
        r = str(random.randint(0, 100))
        assert interface.build_url(r) == f"ftp://bytespace.net/Interfaces/{r}"

    interface.directory = "Testing"
    for _ in range(100):
        r = str(random.randint(0, 100))
        assert interface.build_url(r) == f"ftp://bytespace.net/Testing/{r}"


def test_bytespace_connection():
    interface = Interface()
    assert requests.get(interface.build_url()).status_code == 200


def test_database_interface_parameters_username():
    pass


def test_database_interface_parameters_password():
    pass


def test_database_interface_parameters_key():
    pass


def test_database_interface_valid():
    pass





