# Runs app tests on Small Contact app.

import unittest

from smallcontact import *
from MAZIbox import *


class TestContact(unittest.TestCase):
    def test_load_contacts(self):
        file = load_contacts(file_name="smacontacts.pickle")
        self.assertEqual(file, file_name="smacontacts.pickle")

    def test_Contact_init(self):
        test_1 = Contact(name="Mario", address="Sydney", telephone=555)
        self.assertEqual(test_1.name, "Mario")
        self.assertEqual(test_1.address, "Sydney")
        self.assertEqual(test_1.telephone, 555)

    def test_Session_init(self):
        test_2 = Session(session_length=2)
        self.assertEqual(test_2.session_length, 2)


class TestBox(unittest.TestCase):
    def test_mazi_int(self):
        first = mazi_int(prompt=2)
        self.assertEqual(first, 2)

    def test_mazi_text(self):
        second = mazi_text(prompt="mario")
        self.assertEqual(second, "mario")


if __name__ == "__main__":
    unittest.main(verbosity=2)
