# Small contact app with the time tracker and session history

import pickle
import time
from MAZIbox import *

# Create the session class
class Session:

    _min_session_length = 0.5
    _max_session_length = 4.0

    @staticmethod
    def validate_session_length(session_length):
        """
        Validates a session length and returns
        True if the session is valid or False if not.
        """
        if session_length < Session._min_session_length:
            return False
        if session_length > Session._max_session_length:
            return False
        return True

    def __init__(self, session_length):
        if not Session.validate_session_length:
            raise Exception("Invalid session length")
        self.__session_length = session_length
        self.__session_end_time = time.localtime()
        self.__version = 1

    @property
    def session_length(self):
        return self.__session_length

    @property
    def session_end_time(self):
        return self.__session_end_time

    def check_version(self):
        """
        Checks the version number of this instance of
        Session and upgrades the object if requried.
        """
        pass

    def __str__(self):
        template = "Date: {0}, Length: {1}"
        date_string = time.asctime(self.__session_end_time)
        return template.format(date_string, self.__session_length)


# Create the contact class


class Contact:

    __min_text_length = 1

    __open_fee = 30
    __hourly_fee = 50

    @staticmethod
    def validate_text(text):
        """
        Validates text to be stored in the contact storage.
        True if the text is valid, False if not.
        """
        if len(str(text)) < Contact.__min_text_length:
            return False
        else:
            return True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not Contact.validate_text(name):
            raise Exception("Invalid name")
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if not Contact.validate_text(address):
            raise Exception("Invalid address")
        self.__address = address

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        if not Contact.validate_text(telephone):
            raise Exception("Invalid telephone")
        self.__telephone = telephone

    @property
    def hours_worked(self):
        return self.__hours_worked

    @property
    def billing_amount(self):
        return self.__billing_amount

    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.__hours_worked = 0
        self.__billing_amount = 0
        self.__sessions = []
        self.__version = 3

    @property
    def session_report(self):
        # Convert the list of sessions into a list of strings
        report_strings = map(str, self.__sessions)
        # Convert the list of strings into one string
        # separated by newline characters
        report_result = "\n".join(report_strings)
        return report_result

    def __str__(self):
        template = """
Name: {0}
Address: {1}
Telephone: {2}
Hours on the case: {3}
Amount to bill: {4}
Sessions:
{5}"""
        return template.format(
            self.name,
            self.address,
            self.telephone,
            self.hours_worked,
            self.billing_amount,
            self.session_report,
        )

    def check_version(self):
        """
        Checks the version number of this instance of
        Contact and upgrades the object if required.
        """
        if self.__version == 1:
            # Version 1 of this class does not have a billing amount
            # create a billing amount attribute of zero
            self.__billing_amount = 0
            # Upgrade the Contact to version 2
            self.__version = 2

        if self.__version == 2:
            # Version 2 of this class does not have a session list
            self.__sessions = []
            # Upgrate the Contact to version 3
            self.__version = 3
        # Now check the version of each of the sessions
        for session in self.__sessions:
            session.check_version()

    def add_session(self, session_length):
        """
        Adds the value of the parameter
        onto the hours spent with this contact.
        Raises an exception if the session length is invalid.
        """
        if not Session.validate_session_length(session_length):
            raise Exception("Invalid session length")
        self.__hours_worked = self.__hours_worked + session_length
        amount_to_bill = Contact.__open_fee + (Contact.__hourly_fee * session_length)
        self.__billing_amount = self.__billing_amount + amount_to_bill
        session_record = Session(session_length)
        self.__sessions.append(session_record)


def new_contact():
    """
    Reads in a new contact and stores it.
    """
    print("Create a new contact")
    # Add the data attributes
    name = mazi_text("Enter name: ")
    address = mazi_text("Enter address: ")
    telephone = mazi_text("Enter telephone: ")
    # Create a new instance
    try:
        new_contact = Contact(name=name, address=address, telephone=telephone)
    except Exception as e:
        print("Invalid contact: ", e)
        return
    # Add the new contact to the contacts list
    try:
        contacts.append(new_contact)
    except Exception as e:
        print("Contact failed,", e, "so try to load file.\nPlease try it again.")
        where_is_my_save()


def find_contact(search_name):
    """
    Finds the contact with the matching name.
    Returns a contact instance or None if there is
    no contact with the given name.
    """
    # Remove any whitespace from around the search name
    search_name = search_name.strip()
    # Convert the search name to lower case
    search_name = search_name.lower()
    for contact in contacts:
        # Get the name out of the contact
        name = contact.name
        # Remove the whitespace from around the name
        name = name.strip()
        # Convert the name to lower case
        name = name.lower()
        # See if the name match
        if name.startswith(search_name):
            # Return the contact that was found
            return contact
    # If we get here no contact was found
    # with the given name
    return None


def display_contact():
    """
    Reads in a name to search for and then displays
    the content information for that name or
    a message that the name was not found.'
    """
    print("Find contact")
    search_name = mazi_text("Enter name: ")
    contact = find_contact(search_name)
    if contact != None:
        # We found a contact
        print(contact)
    else:
        print("This name was not found.")


def edit_contact():
    """
    Reads in a name to search for and then allows
    the user to edit the details of that contact.
    If there is no contact the function displays
    a message that the name was not found.
    """
    print("Edit contact")
    search_name = mazi_text("Enter name: ")
    contact = find_contact(search_name)
    if contact != None:
        # We found a contact
        try:
            print("Name: ", contact.name)
            new_name = mazi_text("Enter new name or * to leave unchanged: ")
            if new_name != "*":
                contact.name = new_name
            new_address = mazi_text("Enter new address or * to leave unchanged: ")
            if new_address != "*":
                contact.address = new_address
            new_telephone = mazi_text("Enter new telephone or * to leave unchanged: ")
            if new_telephone != "*":
                contact.telephone = new_telephone
        except Exception as e:
            print("Edit failed: ", e)
    else:
        print("This name was not found. Please check the name again.")


def add_session_to_contact():
    """
    Reads in a name to search for and then allows
    the user to add a session hours for that contact.
    """
    print("Add session")
    search_name = mazi_text("Enter name: ")
    contact = find_contact(search_name)
    if contact != None:
        # We found a contact
        print("Name: ", contact.name)
        print("Previous hours worked: ", contact.hours_worked)
        session_length = mazi_float(prompt="Session length: ")
        try:
            contact.add_session(session_length)
            print("Session hours updated: ", contact.hours_worked)
        except Exception as e:
            print("Add hours failed: ", e)
    else:
        print("This name was not found.")


def save_contacts(file_name):
    """
    Saves the contacts to the given file name.
    Contacts are stored in binary format as pickle file.
    Exceptions will be raised if the save fails.
    """
    print("Save contacts")
    try:
        with open(file_name, "wb") as out_file:
            pickle.dump(contacts, out_file)
    except Exception as e:
        print("Save have failed: ", e)


def load_contacts(file_name):
    """
    Loads the contacts from the given file name.
    Contacts are stored in binary format as pickle file.
    Exceptions will be rised if the load fails.
    """
    global contacts
    print("Load contacts")
    with open(file_name, "rb") as input_file:
        contacts = pickle.load(input_file)
    # Now update the versions of the loaded contacts
    for contact in contacts:
        contact.check_version()


def my_contacts(contacts):
    """
    Displays a list of all stored contacts
    with all relevant details that user had saved.
    """
    print("List of my contacts:")
    try:
        for contact in contacts:
            print(contact)
    except NameError as e:
        print("Contact have been not found,", e, ".")


def where_is_my_save():
    """
    Trys to locate the file previously saved.
    Loads the contacts list from the given file
    if file not found, crates a new contacts list.
    """
    try:
        load_contacts(file_name)
    except:
        print("Contacts file not found.")
        contacts = []


menu = """
Small Contact App

1. New Contact.
2. Find Contact.
3. Edit Contact.
4. Add Session.
5. My Contacts.
6. Exit Program and Save.
7. Exit Program without Save.
8. Load File.

Enter your command: """

file_name = "smacontacts.pickle"

# load_contacts(file_name)


while True:
    command = mazi_int_ranged(prompt=menu, min_value=1, max_value=8)
    if command == 1:
        new_contact()
    elif command == 2:
        display_contact()
    elif command == 3:
        edit_contact()
    elif command == 4:
        add_session_to_contact()
    elif command == 5:
        my_contacts(contacts)
    elif command == 6:
        save_contacts(file_name)
        print("Contacts saved. Thank you and see you soon.")
        time.sleep(2)
        break
    elif command == 7:
        print("No save has been made. Bye.")
        break
    elif command == 8:
        where_is_my_save()
