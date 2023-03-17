# Bytespace imports
from bytespace.interface import Interface


def test_build_url_simple():
    interface = Interface()

    test_names = ["test1", "test2", "test_test_3", "103432", ""]

    for test_thing in test_names:
        assert interface.build_url(test_thing) == f"https://bytespace.network/Interfaces/{test_thing}"


def test_build_url_protocol_change():
    interface = Interface()

    protocols = ["ftp", "http", "https", "smtp", "tcp", "udp"]
    test_names = ["test1", "test2", "test_test_3", "103432", ""]

    for protocol in protocols:

        interface.protocol = protocol
        for test_thing in test_names:
            assert interface.build_url(test_thing) == f"{protocol}://bytespace.network/Interfaces/{test_thing}"


def test_build_url_domain_change():
    interface = Interface()

    domains = ["example", "google", "amazing", "amazon", "borgor", "bytespace"]
    test_names = ["test1", "test2", "test_test_3", "103432", ""]

    for domain in domains:
        domain = domain + ".network"
        interface.domain = domain
        for test_thing in test_names:
            assert interface.build_url(test_thing) == f"https://{domain}/Interfaces/{test_thing}"


def test_build_url_multi_change():
    interface = Interface()

    protocols = ["ftp", "http", "https", "smtp", "tcp", "udp"]
    domains = ["example", "google", "amazing", "amazon", "borgor", "bytespace"]
    test_names = ["test1", "test2", "test_test_3", "103432", ""]

    for protocol in protocols:
        interface.protocol = protocol
        for domain in domains:
            domain = domain + ".network"
            interface.domain = domain
            for test_thing in test_names:
                assert interface.build_url(test_thing) == f"{protocol}://{domain}/Interfaces/{test_thing}"
