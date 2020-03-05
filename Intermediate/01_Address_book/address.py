# This is an application that implement an address book with a CLI 
# interface and a SQLite database (managed by sqlalchemy) to mantain 
# all the information.

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Creation of database class
Base = declarative_base()

# Creation of a session class object
Session = sessionmaker()


class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    surname = Column(String(20))
    phone = Column(String(20))
    mail = Column(String(30))
    address = Column(String(40))


def modify_contact():
    session = Session()
    print("Name: n | Surname: s | Phone: p | Mail: m | Address: a | Exit: x")
    contact_id = int(input("\nInsert the ID of the contact you want to modify:\n=> "))
    while True:
        field = input("Insert the field of the contact to modify: ")
        if field.lower() == 'n':  # name
            name = input("Select the new contact name:\n=> ")
            Contact.update().where(Contact.id == contact_id).\
                values(Contact.name == name)
        elif field.lower() == 's':  # surname
            surname = input("Select the new contact surname:\n=> ")
            Contact.update().where(Contact.id == contact_id).\
                values(Contact.surname == surname)
        elif field.lower() == 'p':  # phone
            phone = input("Select che new phone number:\n=> ")
            Contact.update().where(Contact.id == contact_id).\
                values(Contact.phone == phone)
        elif field.lower() == 'm':  # mail
            mail = input("Select the new contact surname:\n=> ")
            Contact.update().where(Contact.id == contact_id).\
                values(Contact.mail == mail)
        elif field.lower() == 'a':  # address
            address = input("Select the new contact surname:\n=> ")
            Contact.update().where(Contact.id == contact_id).\
                values(Contact.address == address)
        elif field.lower() == 'x':  # exit
            break
        else:
            print("Insert a valid field! Insert 'x' to abort.")
    session.close()


def search_contact():
    session = Session()
    surname = input("\nInsert the surname of the contact you're searching for:\n=> ")
    records = session.query(Contact).filter(Contact.surname == surname).all()
    print("-"*130)
    print("{: <10} {: <20} {: <20} {: <40} {: <30} {: <20}".format(
        'ID', 'SURNAME', 'NAME', 'ADDRESS', 'EMAIL', 'PHONE'
    ))
    print("-"*130)
    for record in records:
        print("{: <10} {: <20} {: <20} {: <40} {: <30} {: <20}".format(
            record.id,
            record.surname, 
            record.name, 
            record.address, 
            record.mail, 
            record.phone))
    session.close()


def delete_contact():
    try:
        session = Session()
        contact_id = int(input("\nInsert the ID of the contact you want to delete:\n=> "))
        session.query(Contact).filter(Contact.id == contact_id).delete()
        print("\nContact deleted...DONE")
    except:
        print("Some error occurred...rollback session.")
        session.rollback()
        raise
    finally:
        session.close()


def view_contact():
    session = Session()
    records = session.query(Contact).order_by(Contact.surname).all()
    print("-"*130)
    print("{: <20} {: <20} {: <40} {: <30} {: <20}".format(
        'SURNAME', 'NAME', 'ADDRESS', 'EMAIL', 'PHONE'
    ))
    print("-"*130)
    for record in records:
        print("{: <20} {: <20} {: <40} {: <30} {: <20}".format(
            record.surname, 
            record.name, 
            record.address, 
            record.mail, 
            record.phone))
    session.close()


def insert_contact():
    try:
        session = Session()
        cname = input("Name of the contact: ")
        csurname = input("Surname of the contact: ")
        cphone = input("Insert the contact phone: ")
        cmail = input("Insert the mail address: ")
        caddress = input("Insert the address: ")
        new_contact = Contact(
            name = cname,
            surname = csurname,
            phone = cphone,
            mail = cmail,
            address = caddress
        )
        session.add(new_contact)
        session.commit()
        print("\nAdding new contact to the database... DONE")
    except:
        print("Some error occurred...rollback session.")
        session.rollback()
        raise
    finally:
        session.close()
        print("Closing session...DONE\n")


def main():
    # Setup the database engine
    engine = create_engine("sqlite:///address.db")

    # Configure the Session object
    Session.configure(bind=engine)

    # Check if the local database exists. If not, create it with all 
    # the columns. 
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(engine)  # Creates table
    
    while True:
        print("\nAdd a contact: a | Delete a contact: d | Modify a contact: m | Search a contact: s | View contacts: v")
        print("Exit: x")
        op = input("\nChoise the operation you want to do:\n=> ")
        if op.lower() == 'a':  # Add an entry //OK
            insert_contact()
        elif op.lower() == 'd':  # Delete an entry
            delete_contact() 
        elif op.lower() == 'm':  # Modify an entry 
            modify_contact()
        elif op.lower() == 's':  # Search for a contact ID //OK
            search_contact()
        elif op.lower() == 'v':  # View contact table //OK
            view_contact()
        elif op.lower() == 'x':
            print("\nExiting...")
            break
        else:
            print("\n### Insert a valid operation code! ###")


if __name__ == "__main__":
    main()    
