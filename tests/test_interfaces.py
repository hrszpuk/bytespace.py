from bytespace.interfaces import DatabaseInterface

def test_database_interface_connect():
    interface = DatabaseInterface("Not a real key")
    assert interface.connect() == "No username supplied!"
    assert interface.connect(username="tokorv") == "No password supplied!"
    assert interface.connect(password="pass34") == "No username supplied!"
    assert interface.connect(username="ugly", password="nam") == "Requested Application couldnt be found!"

